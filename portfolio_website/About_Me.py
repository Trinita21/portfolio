import streamlit as st

# --- Page Config ---
st.set_page_config(
    page_title="Trinita Roy - Portfolio",
    page_icon="🌟",
    layout="wide"
)

# --- Always Dark Mode ---
bg_color = "#0e1117"
text_color = "#ffffff"

# --- Custom CSS ---
st.markdown(f"""
    <style>
    .main {{
        background-color: {bg_color};
        color: {text_color};
        padding: 2rem;
    }}
    .profile-img {{
    border-radius: 50%;
    width: 250px;
    height: 250px;
    margin-top: 40px;
    object-fit: cover;
    border: 3px solid #ff9800;
    animation: fadeIn 2s ease-in;
    }}
    .title {{
        font-size: 3rem;
        font-weight: bold;
        color: {text_color};
        animation: fadeIn 1.2s ease-in;
    }}
    .subtitle {{
        font-size: 1.3rem;
        color: #bbbbbb;
    }}
    .social-icons a {{
        margin-right: 15px;
        font-size: 1.2rem;
        text-decoration: none;
        color: {text_color};
        transition: 0.3s;
    }}
    .social-icons a:hover {{
        color: #ff9800;
    }}
    @keyframes fadeIn {{
        0% {{opacity: 0; transform: translateY(20px);}}
        100% {{opacity: 1; transform: translateY(0);}}
    }}
    html {{
        scroll-behavior: smooth;
    }}
    </style>
""", unsafe_allow_html=True)

# st.markdown('<div class="title">Hi, I\'m Trinita Roy</div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="title" style="text-align: center;">
        Hi, I'm Trinita Roy
    </div>
    """,
    unsafe_allow_html=True
)

# --- Header ---
col1, col2 = st.columns([1, 3])

with col1:
    st.image(
        "https://raw.githubusercontent.com/Trinita21/portfolio/main/portfolio_website/profile_image.jpeg",
        use_container_width=False,
        output_format="auto",
    )


with col2:
    st.markdown('<div class="subtitle"> Generative AI | Advanced Deep Learning | Agentic AI | Multi-modal Models | LLMs | LLM-Ops | Speech and Language Technology | AI Safety and Security | Natural Language Processing | Machine Learning | Software Development |</div>', unsafe_allow_html=True)
    st.write("""
    Hey there 👋 I'm an AI developer/researcher who spends far too much time thinking about how to make machines *think responsibly* and how they work.  
    My core interests orbit around **Gen AI**, and everything mentioned above, especially, teaching intelligent systems how *not* to break things (or ethics).
    I work at the intersection of **deep learning**, **natural language processing**, and **generative AI**, building systems that are not only powerful but also **interpretable, responsible, and aligned** with human intent.  
    Beyond research, I learn and write about the *quirks and paradoxes* of AI, from alignment puzzles to the evolving behavior of generative models.  
    This portfolio is my living lab notebook - a space where theory meets code, and curiosity occasionally breaks into production.
    """)

# --- Social Links ---
st.markdown("### 🌐 Connect with me")
st.markdown(f"""
<div class="social-icons">
    <a href="https://www.linkedin.com/in/trinita-roy/" target="_blank">🔗 LinkedIn</a>
    <a href="https://github.com/Trinita21" target="_blank">💻 GitHub</a>
    <a href="https://scholar.google.com/citations?user=MXdYymEAAAAJ&hl=en" target="_blank">👩🏽‍🎓 Google Scholar</a>
    <a href="https://x.com/trinita_roy" target="_blank">🐦 Twitter</a>
</div>
""", unsafe_allow_html=True)

# # --- Navigation ---
st.markdown("### ✨ Step into my world")

st.markdown("""
<style>
.nav-buttons {
    display: flex;
    justify-content: center;
    gap: 20px;
    margin-top: 1.5rem;
    margin-bottom: 2rem;
    flex-wrap: wrap;
}

.nav-buttons a {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    text-decoration: none;
    color: white;
    background: linear-gradient(135deg, #0072b1, #00bfa5);
    padding: 0.8em 1.2em;
    border-radius: 12px;
    font-weight: 600;
    width: 180px;
    height: 55px;
    transition: all 0.3s ease;
    box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    text-align: center;
}

.nav-buttons a:hover {
    background: linear-gradient(135deg, #00bfa5, #0072b1);
    transform: translateY(-3px);
    box-shadow: 0 6px 14px rgba(0,0,0,0.25);
}
</style>

<div class="nav-buttons">
    <a href="Blogs">📝 Blogs</a>
    <a href="Projects">💼 Projects</a>
    <a href="Work_Experience">📜 Work Experience</a>
    <a href="Notes">🗒️ Notes</a>
</div>
""", unsafe_allow_html=True)




# --- Newsletter Signup ---
st.markdown("### 📩 Subscribe to my Newsletter")
email = st.text_input("Enter your email address")
if st.button("Subscribe"):
    if email:
        st.success(f"Thanks for subscribing, {email}!")
        with open("emails.txt", "a") as f:
            f.write(email + "\n")
    else:
        st.error("Please enter a valid email address.")
