.PHONY: init run-hello run-graph run-faq ingest-pdf rag-cli

init:
	python -m venv venv &&     	./venv/Scripts/pip install -r requirements.txt ||     	( source venv/bin/activate && pip install -r requirements.txt )

run-hello:
	python 01_basics/01_hello_world_llm.py

run-graph:
	python 04_langgraph_workflows/01_hello_graph.py

run-faq:
	python 05_projects/faq_bot/app.py

ingest-pdf:
	python 02_rag/10_ingest_pdf.py

rag-cli:
	python 02_rag/11_rag_cli.py
