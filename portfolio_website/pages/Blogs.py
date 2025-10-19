import streamlit as st

st.set_page_config(page_title="Blogs", page_icon="📝", layout="wide")

st.title("📝 My Blogs")
st.write("""
Welcome to my little corner of the internet, a space where I share my thoughts, learnings and make useful information accessible and understandable to people who need it.
I break down concepts from **Large Language Models** to **Mixture of Experts**, share insights from my projects, and explore the practical side of Generative AI, Advanced Deep Learning, Speech Processing, Natural Language Processing and Machine Learning.  
If you’re interested in **understanding AI deeply**, seeing how research translates into real applications, or just want a clear perspective on cutting-edge developments in the field, you’re in the right place.  

Think of this as a mix of **technical clarity**, **practical insights**, and a touch of **nerdy enthusiasm**, designed for everyone looking to explore AI thoughtfully.
""")

st.markdown("### 🚀 Dive Into the Articles")


blogs = [
    {"title": "Everything You Should Know About Anthropic's Model Context Protocol (MCP)", "link": "https://nlp-nerd.hashnode.dev/everything-you-should-know-about-anthropics-model-context-protocol-mcp"},
    {"title": "Mixture of Experts (MoE) Explained", "link": "https://nlp-nerd.hashnode.dev/mixture-of-experts-moe-explained"},
    {"title": "Faster Inference in Large Language Models (LLMs)", "link": "https://nlp-nerd.hashnode.dev/faster-inference-in-large-language-models-llms"},
    {"title": "Machine Learning Fundamentals", "link": "https://nlp-nerd.hashnode.dev/machine-learning-fundamentals"},
    {"title": "Look into a News AI Agent Project", "link": "https://nlp-nerd.hashnode.dev/look-into-a-news-ai-agent-project"},
    {"title": "Lost in Translation Understanding Parallel Corpora in Machine Translations", "link": "https://nlp-nerd.hashnode.dev/lost-in-translation-understanding-parallel-corpora-in-machine-translation"}
]

for blog in blogs:
    st.markdown(f"#### [{blog['title']}]({blog['link']})")

# Back to home button
st.markdown("[🏠 Back to Home](../)")