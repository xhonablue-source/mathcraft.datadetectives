import streamlit as st
import random
import base64
from PIL import Image

# Function to encode images to base64
def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()
    return f"data:image/png;base64,{encoded}"

# Paths to detective images
amirah_image_path = "images/amirah.png"
amari_image_path = "images/amari.png"

# Encode images
amirah_image = get_base64_image(amirah_image_path)
amari_image = get_base64_image(amari_image_path)

# Page configuration
st.set_page_config(
    page_title="MathCraft Detective Academy",
    page_icon="🕵️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown(f"""
<style>
    .main-header {{
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        color: white;
        margin-bottom: 2rem;
    }}
    .detective-profile {{
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #667eea;
        margin: 1rem 0;
        text-align: center;
    }}
    .math-problem {{
        background: #e3f2fd;
        padding: 1.5rem;
        border-radius: 8px;
        border-left: 4px solid #2196f3;
        margin: 1rem 0;
        font-size: 1.2em;
    }}
    .success-badge {{
        background: linear-gradient(45deg, #4CAF50, #45a049);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        display: inline-block;
        font-weight: bold;
        margin: 0.5rem;
    }}
    .detective-avatar {{
        width: 100px;
        height: 100px;
        border-radius: 50%;
        margin: 0 auto 1rem auto;
        display: block;
        background-size: cover;
        background-position: center;
    }}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown(f"""
<div class="main-header">
    <img src="{amirah_image}" width="60" style="border-radius: 50%;"><br>
    <h1>MathCraft Detective Academy</h1>
    <p><em>Hands-On Mathematical Thinking</em></p>
    <p>Join Detectives Amirah and Amari on mathematical adventures!</p>
    <p>© All Rights Reserved - Xavier Honablue M.Ed</p>
</div>
""", unsafe_allow_html=True)

# Sidebar - Student Profile
st.sidebar.title("🎓 Student Detective Profile")
if 'student_name' not in st.session_state:
    st.session_state.student_name = ""
if not st.session_state.student_name:
    name = st.sidebar.text_input("Enter your detective name:")
    if st.sidebar.button("Join the Academy"):
        if name:
            st.session_state.student_name = name
            st.session_state.points = 0
            st.session_state.current_level = 1
            st.session_state.problems_solved = 0
            st.session_state.current_problem = None
            st.rerun()
else:
    st.sidebar.markdown(f"**Detective:** {st.session_state.student_name}")
    st.sidebar.markdown(f"**Level:** {st.session_state.current_level}")
    st.sidebar.markdown(f"**Points:** {st.session_state.points}")
    st.sidebar.markdown(f"**Cases Solved:** {st.session_state.problems_solved}")

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["🏠 Home", "🧮 Missions", "📊 Progress Tracker", "🏆 Achievements"])

with tab1:
    st.markdown("## Welcome to MathCraft Detective Academy!")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div class="detective-profile">
            <div class="detective-avatar" style="background-image: url('{amirah_image}');"></div>
            <h3>Detective Amirah</h3>
            <p><strong>Specialty:</strong> Addition & Multiplication Mysteries</p>
            <p><em>"Every math problem is a puzzle waiting to be solved!"</em></p>
            <p><strong>Superpower:</strong> Pattern Recognition</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="detective-profile">
            <div class="detective-avatar" style="background-image: url('{amari_image}');"></div>
            <h3>Detective Amari</h3>
            <p><strong>Specialty:</strong> Subtraction & Division Cases</p>
            <p><em>"Math is everywhere - let's investigate together!"</em></p>
            <p><strong>Superpower:</strong> Logical Reasoning</p>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("### 🔍 How to Be a Math Detective:")
    st.markdown("""
    1. **Read Carefully** - Every word is a clue
    2. **Think Step by Step** - Break down the problem
    3. **Show Your Work** - Explain your reasoning
    4. **Check Your Answer** - Does it make sense?
    """)

# Additional tabs (Missions, Progress Tracker, Achievements) would be implemented here, following the same structure and incorporating interactive elements as per your prior lessons.
