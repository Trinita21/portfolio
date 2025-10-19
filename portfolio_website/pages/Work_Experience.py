import streamlit as st

st.set_page_config(page_title="Work Experience", page_icon="📜", layout="wide")

st.title("📜 My Work Experience")
st.write("Professional roles and research positions I have held.")

with st.expander("AI Research Intern - XYZ Research Lab"):
    st.write("""
    - Worked on developing privacy-preserving AI techniques.
    - Conducted experiments on adversarial robustness in speech models.
    - Published findings in a peer-reviewed journal.
    """)

with st.expander("Teaching Assistant - University of ABC"):
    st.write("""
    - Assisted in teaching courses on Computational Linguistics and Deep Learning.
    - Mentored students on NLP projects.
    - Helped design assignments focused on ethical AI development.
    """)

with st.expander("Freelance AI Developer"):
    st.write("""
    - Built custom AI models for startups.
    - Worked on real-time speech recognition and chatbot systems.
    - Implemented model deployment pipelines.
    """)
