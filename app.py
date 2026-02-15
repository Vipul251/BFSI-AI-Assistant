import streamlit as st
from src.similarity import SimilarityEngine
from src.ollama_client import OllamaLLM
from src.rag_pipeline import RAGEngine
from src.guardrails import Guardrails

st.set_page_config(page_title="BFSI AI Assistant")

@st.cache_resource
def load_system():
    return (
        SimilarityEngine("data/alpaca_bfsi.json"),
        OllamaLLM(),
        RAGEngine(),
        Guardrails(),
    )

sim, llm, rag, guard = load_system()

st.title("🏦 BFSI Call Center AI Assistant")

query = st.text_input("Ask your banking question:")

if query:
    if guard.contains_pii(query):
        st.error("Please do not share sensitive information.")
        st.stop()

    if guard.is_out_of_scope(query):
        st.warning("I can assist only with BFSI queries.")
        st.stop()

    found, response, score = sim.search(query)
    st.caption(f"Similarity Score: {score:.3f}")

    if found:
        st.success("✅ Answer from dataset")
        st.write(response)
    else:
        if any(k in query.lower() for k in ["emi", "interest", "penalty"]):
            context = rag.retrieve(query)
            answer = llm.generate(query, context=" ".join(context))
            st.info("📚 Answer using RAG")
        else:
            answer = llm.generate(query)
            st.info("🤖 Answer from Local Model")

        st.write(answer)
