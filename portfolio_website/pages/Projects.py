import streamlit as st

st.set_page_config(page_title="Projects", page_icon="💼", layout="wide")

st.title("💼 My Projects")
st.write("A collection of my work in AI, Responsible AI, and Computational Linguistics.")

with st.expander("Responsible AI using Adversarial Learning"):
    st.write("""
    Developed a robust defense mechanism against backdoor attacks in NLP models
    by using adversarial training and model fine-tuning.
    The approach reduced vulnerability while maintaining model accuracy.
    """)

with st.expander("Multiagent Speech Systems Vulnerability Analysis"):
    st.write("""
    Investigated security flaws in AI-driven speech systems with multiple agents.
    Designed methods to detect and mitigate harmful voice injections and 
    prompt-based attacks.
    """)

with st.expander("Privacy-Aware Speech Transcription"):
    st.write("""
    Created a speech-to-text system that automatically detects and redacts
    sensitive information before storing or displaying transcripts.
    Implemented using Whisper and custom privacy filters.
    """)
