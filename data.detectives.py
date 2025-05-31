import streamlit as st
import base64
import random

# Function to load images as base64
def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        return f"data:image/png;base64,{base64.b64encode(image_file.read()).decode()}"

# Load detective avatars
amirah_img_path = "/mnt/data/6695cdf7-a04a-4f68-b0c3-5c342a209160.png"
amari_img_path = "/mnt/data/6695cdf7-a04a-4f68-b0c3-5c342a209160.png"  # Replace with different image if available

amirah_img = get_base64_image(amirah_img_path)
amari_img = get_base64_image(amari_img_path)

# Page setup
st.set_page_config(page_title="MathCraft Detective Academy", layout="wide")

# Header
st.markdown(f"""
<style>
    .main-header {{
        background: linear-gradient(135deg, #667eea, #764ba2);
        padding: 2rem;
        text-align: center;
        color: white;
        border-radius: 12px;
    }}
    .detective-avatar {{
        width: 100px;
        height: 100px;
        border-radius: 50%;
        background-size: cover;
        background-position: center;
        margin: 0 auto 10px auto;
    }}
    .detective-card {{
        background: #f9f9f9;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        border: 2px solid #d0d0ff;
    }}
</style>

<div class="main-header">
    <img src="{amirah_img}" width="60" style="border-radius: 50%;">
    <h1>MathCraft Detective Academy</h1>
    <p><em>Hands On Mathematical Thinking</em></p>
    <p>Join Detectives Amirah and Amari on mathematical adventures!</p>
    <p>© All Rights Reserved - Xavier Honablue M.Ed</p>
</div>
""", unsafe_allow_html=True)

# Sidebar - Profile setup
st.sidebar.title("🎓 Student Detective Profile")
if 'student_name' not in st.session_state:
    st.session_state.student_name = ""
if not st.session_state.student_name:
    name = st.sidebar.text_input("Enter your detective name:")
    if st.sidebar.button("Join Academy"):
        st.session_state.student_name = name
        st.session_state.points = 0
        st.session_state.level = 1
        st.session_state.solved = 0
        st.session_state.current_problem = None
        st.rerun()
else:
    st.sidebar.markdown(f"**Detective:** {st.session_state.student_name}")
    st.sidebar.markdown(f"**Points:** {st.session_state.points}")
    st.sidebar.markdown(f"**Level:** {st.session_state.level}")
    st.sidebar.markdown(f"**Cases Solved:** {st.session_state.solved}")

# Tabs
home, missions = st.tabs(["🏠 Home", "🧮 Missions"])

# --- Home ---
with home:
    st.markdown("## Meet Your MathCraft Mentors")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div class="detective-card">
            <div class="detective-avatar" style="background-image: url('{amirah_img}')"></div>
            <h3>Detective Amirah</h3>
            <p><strong>Specialty:</strong> Addition & Multiplication</p>
            <p><em>"Every math problem is a puzzle waiting to be solved!"</em></p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="detective-card">
            <div class="detective-avatar" style="background-image: url('{amari_img}')"></div>
            <h3>Detective Amari</h3>
            <p><strong>Specialty:</strong> Subtraction & Division</p>
            <p><em>"Math is everywhere—let’s investigate!"</em></p>
        </div>
        """, unsafe_allow_html=True)

# --- Missions ---
def generate_problem(level):
    op = random.choice(["+", "-", "*", "/"])
    if op == "+":
        a, b = random.randint(1, 10*level), random.randint(1, 10*level)
        return f"{a} + {b}", a + b, "Amirah"
    elif op == "-":
        a, b = sorted([random.randint(1, 10*level), random.randint(1, 10*level)], reverse=True)
        return f"{a} - {b}", a - b, "Amari"
    elif op == "*":
        a, b = random.randint(1, 5*level), random.randint(1, 5*level)
        return f"{a} × {b}", a * b, "Amirah"
    else:
        b = random.randint(1, 5*level)
        a = b * random.randint(1, 5*level)
        return f"{a} ÷ {b}", a // b, "Amari"

with missions:
    st.header("🧮 Mission Assignment")
    if st.session_state.student_name:
        if st.session_state.current_problem is None or st.button("🔄 New Case"):
            expr, answer, detective = generate_problem(st.session_state.level)
            st.session_state.current_problem = {"expr": expr, "answer": answer, "detective": detective}
        current = st.session_state.current_problem
        st.markdown(f"### Case from Detective **{current['detective']}**:")
        st.latex(current["expr"])
        guess = st.number_input("📝 Your Answer:", step=1, format="%i")
        if st.button("Check Answer"):
            if guess == current["answer"]:
                st.success("✅ Case Solved! Excellent work!")
                st.session_state.points += 10
                st.session_state.solved += 1
                if st.session_state.solved % 5 == 0:
                    st.session_state.level += 1
                    st.balloons()
                    st.success(f"🎉 You’ve been promoted to Level {st.session_state.level}!")
                st.session_state.current_problem = None
            else:
                st.error(f"❌ Not quite. Try the next one!")
                st.info(f"💡 Tip from Detective {current['detective']}: Break it down step-by-step.")
    else:
        st.warning("🔒 Please enter your name in the sidebar to begin your detective training.")

