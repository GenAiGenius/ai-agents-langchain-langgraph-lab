from langgraph.graph import StateGraph, END

class State(dict):
    pass

def step1(state: State):
    state["msg"] = "Hello from step1"
    return state

def step2(state: State):
    state["msg"] += " -> step2"
    return state

graph = StateGraph(State)
graph.add_node("step1", step1)
graph.add_node("step2", step2)

graph.set_entry_point("step1")
graph.add_edge("step1", "step2")
graph.add_edge("step2", END)

if __name__ == "__main__":
    app = graph.compile()
    print(app.invoke({}))
