# ai-agents-langchain-langgraph-lab

A hands-on learning lab for **LangChain** and **LangGraph**. Start simple, add features incrementally, and grow into multi-agent, production-style workflows.

## 🔧 Setup

```bash
git clone <your-repo-url> ai-agents-langchain-langgraph-lab
cd ai-agents-langchain-langgraph-lab

python -m venv venv
# Windows:
# venv\Scripts\activate
# macOS/Linux:
# source venv/bin/activate

pip install -r requirements.txt
cp .env.example .env  # set OPENAI_API_KEY inside
```

## ▶️ First run

```bash
python 01_basics/01_hello_world_llm.py
python 04_langgraph_workflows/01_hello_graph.py
python 05_projects/faq_bot/app.py
```

---

## 📚 Folder Structure

```text
ai-agents-langchain-langgraph-lab/
├── 01_basics/                 # LLM calls, prompts, chains, memory
├── 04_langgraph_workflows/    # Graph-based agent workflows
├── 05_projects/faq_bot/       # Mini RAG project
└── utils/                      # Reusable helpers
```

---

## 🗺️ 7-Day Learning Roadmap

**Day 1 – Foundations**
- Understand LLMs, prompts, tokens, temperature vs. top_p
- Run `01_hello_world_llm.py`
- Exercise: create a new script that summarizes a paragraph in 3 styles

**Day 2 – Prompt Engineering & Chains**
- Study `ChatPromptTemplate`, `LLMChain`, and output parsers
- Run `02_prompt_chain.py`
- Exercise: build a two-step chain (outline → expand)

**Day 3 – Memory & State**
- Add short-term memory to a chain (ConversationBufferMemory)
- Exercise: build a CLI chatbot with memory

**Day 4 – RAG Basics**
- Create embeddings, store in Chroma, and query with `RetrievalQA`
- Run `05_projects/faq_bot/app.py`
- Exercise: index a small PDF of your choice

**Day 5 – Tools & Agents (LangChain)**
- Add a tool (e.g., math or web request) to an agent
- Exercise: multi-tool agent for search + summarize

**Day 6 – Workflows (LangGraph)**
- Build a branching graph with retries/guards
- Run `04_langgraph_workflows/01_hello_graph.py`
- Exercise: add a loop with a stop condition

**Day 7 – Mini Project**
- Combine RAG + approval step (human-in-the-loop)
- Write a short README on what you built and what to improve next

---

## 🧭 Tips
- Keep adding folders like `02_rag/`, `03_tools_and_agents/`, etc. as you progress.
- Each folder should contain a small README of what you learned.
- Commit often with clear messages.

## 🧩 Quick Commands (Makefile)
```bash
make init         # create venv + install
make run-hello    # basics
make run-graph    # langgraph hello
make run-faq      # mini RAG project
make ingest-pdf   # add PDFs from data/
make rag-cli      # ask questions over your ingested PDFs
```

## 📂 New Folders
- `data/` — put your PDFs here
- `docs/` — place notes/diagrams
- `utils/rag_helpers.py` — shared RAG utilities

## 🧪 New Examples
- `03_tools_and_agents/02_multi_tool_agent.py` — Multi-tool agent (Calculator + RAGSearch)
- `04_langgraph_workflows/02_approval_workflow.py` — Planner → Executor → Approval → Finalize workflow

## 🧰 Dev Container
- Folder: `.devcontainer/`
- Open in VS Code → **Reopen in Container** for a pre-configured environment.
