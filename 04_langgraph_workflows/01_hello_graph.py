# 04_langgraph_workflows/01_hello_graph.py
from typing import TypedDict, Optional
from langgraph.graph import StateGraph, END

class State(TypedDict, total=False):
    msg: str

def step1(state: State) -> State:
    # Return only the updated keys (delta)
    return {"msg": "Hello from step1"}

def step2(state: State) -> State:
    msg = state.get("msg", "Hello")
    return {"msg": f"{msg} -> step2"}

graph = StateGraph(State)
graph.add_node("step1", step1)
graph.add_node("step2", step2)

graph.set_entry_point("step1")
graph.add_edge("step1", "step2")
graph.add_edge("step2", END)

if __name__ == "__main__":
    app = graph.compile()
    out = app.invoke({})
    print(out)  # expected: {'msg': 'Hello from step1 -> step2'}
