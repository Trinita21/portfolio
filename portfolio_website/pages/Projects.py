import streamlit as st

st.set_page_config(page_title="Projects", page_icon="💼", layout="wide")

# PROJECTS SECTION

st.title("💼 My Projects")
st.write("Here is a collection of some of my work in AI, Responsible AI, and Computational Linguistics. The rest of the projects with codes can be found in my github link. Feel free to take a look!")

with st.expander("Adversarial Robustness (Ongoing)"):
    st.write("""
    - Research project focused on improving adversarial robustness of production-grade LLMs.
    - Aims to prevent model jailbreaking and adversarial prompt injection through fine-tuned guardrails.
    - Explores privacy-preserving inference and differential noise injection for robustness.
    """)

with st.expander("GoBot - Agentic AI Travel Planner"):
    st.write("""
    - Built an agentic AI system that generates personalized travel itineraries based on user prompts.
    - Developed with FastAPI (backend) and Streamlit (frontend), integrating agent graph reasoning and workflow tracing.
    - Implements context chaining and retrieval-based reasoning for dynamic trip planning.
    """)

with st.expander("Curator Agent (AI Tech Digest)"):
    st.write("""
    - Designed an autonomous assistant to collect, summarize, and email trending AI research and news.
    - Integrated LangGraph, summarization models, and RAG pipelines for knowledge curation.
    - Currently expanding with voice-based delivery via TTS pipelines.
    """)

with st.expander("AI Video Slide Generator"):
    st.write("""
    - Developed an NLP-to-Video AI pipeline that transforms PDFs into avatar-based lip-synced videos.
    - Combined text understanding, summarization, speech synthesis, and generative avatars.
    - Used in production at SciSpace as part of the AI communication toolkit.
    """)

with st.expander("Agentic AI Projects Collection (Agno Framework)") :
    st.write("""
    - Repository showcasing multiple autonomous AI agents built using Agno framework.
    - Includes:
        - **Travel Agent:** destination planning and itinerary generation.
        - **Movie Recommender:** personalized film suggestions.
        - **Research Agent:** information retrieval and summarization for research workflows.
    """)

with st.expander("Financial Analyst AI Agent"):
    st.write("""
    - Built a financial data analysis agent using PhiData and Groq for forecasting and risk modeling.
    - Performs automated financial modeling and provides actionable insights via intelligent analysis.
    - Demonstrates integration of structured data reasoning with LLM-based interpretation.
    """)

with st.expander("Video Summarizer using Google Gemini & Phidata"):
    st.write("""
    - Streamlit-based video summarization tool leveraging Google Gemini API and Phidata.
    - Generates concise lecture or meeting summaries from long-form video content.
    - Designed for accessibility and efficient information extraction.
    """)

with st.expander("Coding Assistant with DeepSeek & LangChain"):
    st.write("""
    - Developed an AI coding assistant using DeepSeek LLM integrated with LangChain.
    - Enables intelligent code generation, debugging, and conversational programming.
    - Showcases real-time LLM integration in Streamlit UI for enhanced developer experience.
    """)

with st.expander("RAG-Based Code Assistant using Weaviate & Ollama"):
    st.write("""
    - Built a Retrieval-Augmented Generation (RAG) system for test case generation.
    - Uses Weaviate for vector search and Ollama (LLaMA models) for context-driven code synthesis.
    - Designed to automatically suggest and generate unit tests from project repositories.
    """)

with st.expander("Patents Agent - IdeaDev"):
    st.write("""
    - AI-powered system for idea generation and patent drafting using RAG + Agentic reasoning.
    - Integrates Weaviate-based patent search and structured prompt refinement.
    - Automates early-stage invention ideation and documentation workflows.
    """)

with st.expander("RotavirusPred"):
    st.write("""
    - Machine learning-based model predicting virulence of Rotavirus using genome and protein sequence data.
    - Designed to assist in identifying high-risk viral strains for public health research.
    - Combines sequence analysis, feature engineering, and ensemble ML models.
    """)

with st.expander("FluSPred - Influenza A Host Tropism Prediction"):
    st.write("""
    - Predicts zoonotic host tropism of Influenza A strains using genome and protein sequence features.
    - Developed ML models to assess human infection potential of novel viral strains.
    - Aids virology researchers in prioritizing surveillance and pandemic preparedness.
    """)


# PUBLICATIONS SECTION


st.markdown("---")
st.title("📄 Research Publications")
st.write("Here are my selected research publications in AI, NLP, and Information Retrieval:")

with st.expander("AAAI 2024 – SciSpace Copilot: Empowering Researchers Through Intelligent Reading Assistance"):
    st.write("""
    - Published at **AAAI Conference on Artificial Intelligence (AAAI 2024)**.
    - Introduces an intelligent reading assistant leveraging LLMs and RAG to enhance scientific comprehension.
    - Focuses on context reasoning, adaptive summarization, and literature exploration.
    - Demonstrates the role of generative models in improving research workflows.
    """)
    st.markdown("[Read Paper](https://ojs.aaai.org/index.php/AAAI/article/view/30578)")

with st.expander("ECIR 2024 – Harnessing AI for Effortless Scientific Discovery"):
    st.write("""
    - Published at **European Conference on Information Retrieval (ECIR 2024)**.
    - Proposes an AI system for automating literature review through semantic retrieval and abstractive summarization.
    - Combines knowledge graph integration with transformer-based retrieval pipelines.
    - Achieved improved clustering and relevance in large-scale scientific corpora.
    """)
    st.markdown("[Read Paper](https://link.springer.com/chapter/10.1007/978-3-031-56069-9_28)")

with st.expander("ACL Anthology 2022 – Multi-document Summarization of Scientific Articles"):
    st.write("""
    - Published in **ACL Anthology (SDP Workshop 2022)**.
    - Developed a hybrid extractive–abstractive summarization framework for multi-document scientific corpora.
    - Used Transformer-based sentence ranking with BART for abstractive generation.
    - Improved coherence, informativeness, and factual alignment in evaluation benchmarks.
    """)
    st.markdown("[Read Paper](https://aclanthology.org/2022.sdp-1.25/)")

with st.expander("Journal of General Virology – Genome-based Prediction of Influenza A Infectivity"):
    st.write("""
    - Published in the **Journal of General Virology**.
    - Designed machine learning models to predict human infectivity of Influenza A based on genomic and proteomic data.
    - Supported early detection of high-risk viral strains and zoonotic potential.
    - Demonstrated the effectiveness of computational genomics for pandemic preparedness.
    """)
    st.markdown("[Read Paper](https://www.microbiologyresearch.org/)")