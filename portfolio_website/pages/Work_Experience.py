import streamlit as st

st.set_page_config(page_title="Work Experience", page_icon="📜", layout="wide")

st.title("📜 My Work Experience")
st.write("Professional roles and research positions I have held.")

with st.expander("Working Student - Digital Transformations, Robert Bosch GmbH (Apr 2025 - Present, Abstatt, Germany)"):
    st.write("""
    - Designed large-scale time-series modeling pipelines for automotive sensor data, enabling real-time signal analysis at scale.
    - Built interactive dashboards and auto-generated analytics pipelines, reducing engineering effort by 70% and supporting deployment of domain-specific predictors.
    - Set up CI/CD pipelines (GitHub Actions)
    """)

with st.expander("Working Student - Generative AI, Fraunhofer IPA (Jul 2024 - Mar 2025, Stuttgart, Germany)"):
    st.write("""
    - Led development of a multi-modal medical AI assistant integrating vision, language, and structured data for diagnosis and treatment planning.
    - Optimized RAG and GraphRAG architectures, improving retrieval and reasoning performance by 20%.
    - Built an ETL pipeline using Azure Data Factory, Databricks, or Synapse.
    - Designed data models or dashboards using Power BI, SQL, or Cosmos DB.
    - Deployed an AI/ML model integrated into a cloud data workflow.
    - Worked with real-time analytics (Event Hubs, Stream Analytics, Kafka).
    - Scaled retrieval models to multi-million document corpora while maintaining low inference latency and high accuracy.
    """)

with st.expander("AI/ML Research Scientist - SciSpace (Aug 2022 - May 2024, Bengaluru, India)"):
    st.write("""
    - Led end-to-end development of AI products using LLMs, NLP, and ML, driving +40% user engagement and +30% user acquisition.
    - Designed and deployed foundation model-driven systems for semantic search, summarization, and translation used by millions globally.
    - Fine-tuned and optimized large-scale LLMs (LLaMA-2, OPT, GPT) using parameter-efficient training and distributed optimization.
    - Built GPU-accelerated semantic similarity search engines with CUDA C++, outperforming traditional RAG systems.
    - Built REST APIs in Python and  integrated with AI services.
    - Automated testing and deployment with GitHub Actions or Azure DevOps.
    - Worked on developer productivity tools or custom extensions/plugins.
    - Collaborated with backend and UI teams to deliver multi-agent LLM applications integrating orchestration frameworks and distributed inference.
    - Developed generative AI pipelines for slide and avatar-based video generation. → [Work Sample](https://typeset.io/pdf-to-video)
    - Enhanced semantic search accuracy by 20% using Transformer-based NLP systems. → [Work Sample](https://typeset.io/search)
    - Executed PoCs in multimodal AI, including speech/audio processing and GAN-based image/video editing, leading cross-functional teams to deployment.
    """)

with st.expander("AI/ML Research Intern - SciSpace (May 2022 - Aug 2022, Bengaluru, India)"):
    st.write("""
    - Conducted research on user acquisition and implemented AI/ML-driven NLP projects increasing web traffic by 15% and improving SEO by 10%.
    - Delivered citation classification, lexical FAQ generation, and blog automation pipelines, improving engagement by 20%.
    - Built APIs for Named Entity Recognition and Abstractive Summarization, contributing to a 30% rise in organic search traffic.
    """)
