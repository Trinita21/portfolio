import streamlit as st
import os

st.set_page_config(page_title="Notes", page_icon="🗒️", layout="wide")

st.title("🗒️ My Notes")

st.write("""
This is my **Notes section** where I capture ideas, concepts, and insights in a **handwritten, visual format**.  
Each note is a personal reflection, designed to **help me understand concepts deeply**, organize thoughts efficiently, and make learning easier.  
I upload **one interesting concept each day**, ranging from AI theory to deep learning techniques. The notes are typically **scanned pages, images, or PDFs** written to clarify ideas and structure knowledge.  
Writing is a powerful tool to **solidify understanding**, and I believe sharing knowledge makes learning more impactful.  
Whether you’re a student, researcher, or just curious about AI, feel free to browse and learn from these notes.
""")

st.markdown("### 📚 Explore the Notes")

# Directory and file setup
notes_dir = "notes"
pdf_file = os.path.join(notes_dir, "linear_regression.pdf")

# Check if file exists
if os.path.exists(pdf_file):
    with st.expander("📄 Linear Regression", expanded=False):
        st.write("Click below to open the Linear Regression notes in a new tab:")
        
        # Create a relative path for the PDF
        pdf_path = f"/{pdf_file}"  # Works if running with `streamlit run`
        
        # Add a link that opens in a new tab
        st.markdown(
            f'<a href="{pdf_path}" target="_blank" style="text-decoration:none;">'
            f'<button style="padding:10px 18px; background-color:#4CAF50; color:white; border:none; border-radius:8px; cursor:pointer;">📖 Open Linear Regression PDF</button>'
            '</a>',
            unsafe_allow_html=True
        )
else:
    st.warning("PDF file not found. Please ensure linear_regression.pdf is in the notes folder.")

# Back to home button
st.markdown("[🏠 Back to Home](../)")

