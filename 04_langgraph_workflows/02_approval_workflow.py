import os
from typing import Dict, Any
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from utils.config import OPENAI_API_KEY

class State(dict):
    """State structure:
    {
      'question': str,
      'plan': str,
      'draft': str,
      'approved': bool,
      'final': str
    }
    """

llm = ChatOpenAI(model="gpt-4o-mini", api_key=OPENAI_API_KEY)

def plan_node(state: State) -> State:
    q = state.get('question', '')
    plan = llm.invoke(f"Create a concise 2-step plan to answer: {q}").content
    state['plan'] = plan
    return state

def execute_node(state: State) -> State:
    q = state.get('question', '')
    plan = state.get('plan', '')
    draft = llm.invoke(f"Follow this plan to draft an answer. Be precise.\nPlan:\n{plan}\nQuestion:\n{q}").content
    state['draft'] = draft
    return state

def approval_gate(state: State) -> State:
    auto = os.environ.get('AUTO_APPROVE', '0') == '1'
    # Simple heuristic: require approval if draft is long
    needs = (not auto) and (len(state.get('draft','')) > 600)
    state['approved'] = not needs
    return state

def human_approval(state: State) -> State:
    # Simulate human approval in console
    draft = state.get('draft','')
    print("\n--- DRAFT FOR APPROVAL ---\n", draft, "\n---------------------------\n")
    choice = input("Approve draft? (y/n) ").strip().lower()
    state['approved'] = (choice == 'y')
    return state

def finalize_node(state: State) -> State:
    if state.get('approved'):
        state['final'] = state.get('draft','')
    else:
        # Ask model to revise shorter and clearer
        draft = state.get('draft','')
        state['final'] = llm.invoke(f"Revise the following to be shorter, clearer, and ready for end users:\n{draft}").content
    return state

# Build graph
graph = StateGraph(State)
graph.add_node('plan', plan_node)
graph.add_node('execute', execute_node)
graph.add_node('approval_gate', approval_gate)
graph.add_node('human_approval', human_approval)
graph.add_node('finalize', finalize_node)

graph.set_entry_point('plan')
graph.add_edge('plan', 'execute')
graph.add_edge('execute', 'approval_gate')
# Conditional path: if approved==False -> human_approval -> finalize
def route_after_gate(state: State) -> str:
    return 'finalize' if state.get('approved') else 'human_approval'

graph.add_conditional_edges('approval_gate', route_after_gate, {'finalize': 'finalize', 'human_approval': 'human_approval'})
graph.add_edge('human_approval', 'finalize')
graph.add_edge('finalize', END)

if __name__ == "__main__":
    app = graph.compile()
    question = "Explain LangGraph in one paragraph and when to use it over LangChain."
    # Set AUTO_APPROVE=1 to skip manual approval
    result = app.invoke({'question': question})
    print("\n=== FINAL ANSWER ===\n", result.get('final',''))
