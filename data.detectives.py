import streamlit as st
import base64
import random
import plotly.express as px
import pandas as pd
from datetime import datetime

# --- Encode image to base64 string ---
def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()
    return f"data:image/png;base64,{encoded}"

# ✅ Update to use your uploaded image path
amirah_image_path = "/mnt/data/6695cdf7-a04a-4f68-b0c3-5c342a209160.png"
amari_image_path = amirah_image_path  # Using same image for both for now

# Convert image to base64
try:
    amirah_image = get_base64_image(amirah_image_path)
    amari_image = get_base64_image(amari_image_path)
except:
    # Fallback if images not found
    amirah_image = "data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTAwIiBoZWlnaHQ9IjEwMCIgdmlld0JveD0iMCAwIDEwMCAxMDAiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PGNpcmNsZSBjeD0iNTAiIGN5PSI1MCIgcj0iNTAiIGZpbGw9IiM4QjQ1MTMiLz48dGV4dCB4PSI1MCIgeT0iNTUiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSIzMCIgZmlsbD0id2hpdGUiIHRleHQtYW5jaG9yPSJtaWRkbGUiPvCfj6c8L3RleHQ+PC9zdmc+"
    amari_image = "data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTAwIiBoZWlnaHQ9IjEwMCIgdmlld0JveD0iMCAwIDEwMCAxMDAiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PGNpcmNsZSBjeD0iNTAiIGN5PSI1MCIgcj0iNTAiIGZpbGw9IiM4QjQ1MTMiLz48dGV4dCB4PSI1MCIgeT0iNTUiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSIzMCIgZmlsbD0id2hpdGUiIHRleHQtYW5jaG9yPSJtaWRkbGUiPvCfj6Y8L3RleHQ+PC9zdmc+"

# --- Page setup ---
st.set_page_config(
    page_title="MathCraft Detective Academy",
    page_icon="🕵️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Initialize session state ---
if 'student_name' not in st.session_state:
    st.session_state.student_name = ""
if 'points' not in st.session_state:
    st.session_state.points = 0
if 'current_level' not in st.session_state:
    st.session_state.current_level = 1
if 'problems_solved' not in st.session_state:
    st.session_state.problems_solved = 0
if 'current_problem' not in st.session_state:
    st.session_state.current_problem = None
if 'problem_history' not in st.session_state:
    st.session_state.problem_history = []
if 'correct_streak' not in st.session_state:
    st.session_state.correct_streak = 0
if 'show_hint' not in st.session_state:
    st.session_state.show_hint = False

# --- Custom CSS ---
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
    .detective-avatar {{
        width: 80px;
        height: 80px;
        border-radius: 50%;
        margin: 0 auto 1rem auto;
        display: block;
        background-size: cover;
        background-position: center;
        border: 3px solid #667eea;
    }}
    .detective-profile {{
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #667eea;
        margin: 1rem 0;
        text-align: center;
    }}
    .mission-card {{
        background: #e3f2fd;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #2196f3;
        margin: 1rem 0;
    }}
    .achievement-badge {{
        background: linear-gradient(45deg, #4CAF50, #45a049);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        display: inline-block;
        font-weight: bold;
        margin: 0.25rem;
        font-size: 0.9em;
    }}
    .hint-box {{
        background: #fff3cd;
        border: 1px solid #ffeaa7;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }}
    .stats-card {{
        background: #f1f3f4;
        padding: 1rem;
        border-radius: 8px;
        text-align: center;
        margin: 0.5rem 0;
    }}
</style>
<div class="main-header">
    <img src="{amirah_image}" width="60" style="border-radius: 50%; border: 3px solid white;"><br>
    <h1>🕵️ MathCraft Detective Academy</h1>
    <p><em>Hands-On Mathematical Thinking</em></p>
    <p>Join Detectives Amirah and Amari on mathematical adventures!</p>
    <p>© All Rights Reserved - Xavier Honablue M.Ed</p>
</div>
""", unsafe_allow_html=True)

# --- Enhanced Sidebar ---
st.sidebar.title("🎓 Detective Profile")
if not st.session_state.student_name:
    name = st.sidebar.text_input("Enter your detective name:")
    if st.sidebar.button("🚀 Join the Academy"):
        if name:
            st.session_state.student_name = name
            st.rerun()
else:
    st.sidebar.markdown(f"**🕵️ Detective:** {st.session_state.student_name}")
    
    # Stats in sidebar
    col1, col2 = st.sidebar.columns(2)
    with col1:
        st.metric("Level", st.session_state.current_level)
        st.metric("Cases", st.session_state.problems_solved)
    with col2:
        st.metric("Points", st.session_state.points)
        st.metric("Streak", st.session_state.correct_streak)
    
    # Progress bar
    progress_to_next = (st.session_state.problems_solved % 5) / 5
    st.sidebar.progress(progress_to_next)
    st.sidebar.caption(f"Progress to Level {st.session_state.current_level + 1}")
    
    # Reset button
    if st.sidebar.button("🔄 New Detective Profile"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

# --- Enhanced Problem Generator ---
def generate_problem(level):
    """Generate a math problem based on difficulty level"""
    difficulty_multiplier = min(level, 10)  # Cap at level 10 for reasonable numbers
    
    # Base ranges that scale with level
    base_min = 1 + (difficulty_multiplier - 1) * 5
    base_max = 10 + (difficulty_multiplier - 1) * 10
    
    operations = ["+", "-", "×", "÷"]
    operation = random.choice(operations)
    
    if operation == "+":
        a = random.randint(base_min, base_max)
        b = random.randint(base_min, base_max)
        question = f"Detective Amirah collected {a} pieces of evidence on Monday and {b} pieces on Tuesday. How many pieces did she collect in total?"
        answer = a + b
        hint = "💡 **Amirah's Tip:** Add the numbers together to find the total!"
        
    elif operation == "-":
        a = random.randint(base_max, base_max * 2)
        b = random.randint(base_min, a - 1)
        question = f"Detective Amari had {a} case files. She solved {b} cases. How many case files are still open?"
        answer = a - b
        hint = "💡 **Amari's Tip:** Start with the first number and count backwards!"
        
    elif operation == "×":
        a = random.randint(2, base_min + 5)
        b = random.randint(2, base_min + 3)
        question = f"Detective Amirah organized evidence into {a} boxes with {b} items in each box. How many items total?"
        answer = a * b
        hint = "💡 **Amirah's Tip:** Think of it as adding the same number multiple times!"
        
    else:  # division
        b = random.randint(2, base_min + 3)
        a = b * random.randint(2, base_min + 5)
        question = f"Detective Amari needs to distribute {a} clues equally among {b} investigation teams. How many clues per team?"
        answer = a // b
        hint = "💡 **Amari's Tip:** How many groups of the smaller number fit into the larger number?"
    
    return {
        'question': question,
        'expression': f"{a} {operation} {b}",
        'answer': answer,
        'hint': hint,
        'operation': operation,
        'level': level
    }

# --- Main Layout ---
tab1, tab2, tab3, tab4 = st.tabs(["🏠 Detective HQ", "🧮 Math Missions", "📊 Progress", "🏆 Achievements"])

with tab1:
    st.markdown("## Meet Your MathCraft Detective Mentors")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div class="detective-profile">
            <div class="detective-avatar" style="background-image: url('{amirah_image}');"></div>
            <h3>🕵️‍♀️ Detective Amirah</h3>
            <p><strong>Specialty:</strong> Addition & Multiplication Mysteries</p>
            <p><em>"Every math problem is a puzzle waiting to be solved!"</em></p>
            <p><strong>Detective Badge:</strong> Pattern Recognition Expert</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="detective-profile">
            <div class="detective-avatar" style="background-image: url('{amari_image}');"></div>
            <h3>🕵️‍♂️ Detective Amari</h3>
            <p><strong>Specialty:</strong> Subtraction & Division Cases</p>
            <p><em>"Math is everywhere—let's investigate together!"</em></p>
            <p><strong>Detective Badge:</strong> Logic & Reasoning Master</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### 🕵️ How to Be a MathCraft Detective:")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **🔍 Investigation Steps:**
        1. 📖 Read the case carefully
        2. 🧠 Identify what you need to find
        3. 🔢 Choose the right mathematical operation
        4. ✅ Check if your answer makes sense
        """)
    with col2:
        st.markdown("""
        **🎯 Detective Skills:**
        - 🕵️ Pay attention to details
        - 🤔 Think step by step
        - 📝 Show your work
        - 🔄 Learn from mistakes
        """)

with tab2:
    st.markdown("## 🧮 Math Detective Missions")

    if st.session_state.student_name:
        # Mission controls
        col1, col2, col3 = st.columns([2, 1, 1])
        with col1:
            if st.button("🆕 New Mission Assignment", type="primary"):
                st.session_state.current_problem = generate_problem(st.session_state.current_level)
                st.session_state.show_hint = False
        
        with col2:
            if st.button("💡 Detective Hint"):
                st.session_state.show_hint = True
        
        with col3:
            difficulty = st.selectbox("Mission Level:", 
                                    options=list(range(1, 11)), 
                                    index=st.session_state.current_level-1,
                                    key="manual_level")
        
        # Generate initial problem if none exists
        if st.session_state.current_problem is None:
            st.session_state.current_problem = generate_problem(st.session_state.current_level)

        problem = st.session_state.current_problem
        
        # Display mission
        st.markdown(f"""
        <div class="mission-card">
        <h4>🕵️ Case File #{st.session_state.problems_solved + 1} - Level {problem['level']}</h4>
        <p><strong>Mission Brief:</strong></p>
        <p>{problem['question']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Show the mathematical expression
        st.markdown(f"### 🔢 Mathematical Expression:")
        st.latex(problem['expression'])
        
        # Show hint if requested
        if st.session_state.show_hint:
            st.markdown(f"""
            <div class="hint-box">
            {problem['hint']}
            </div>
            """, unsafe_allow_html=True)
        
        # Answer input
        col1, col2 = st.columns([2, 1])
        with col1:
            guess = st.number_input("🎯 Your Detective Solution:", 
                                  step=1, 
                                  format="%i", 
                                  key="answer_input")
        
        with col2:
            st.markdown("<br>", unsafe_allow_html=True)  # Spacing
            submit_answer = st.button("🔍 Submit Solution", type="primary")
        
        # Check answer
        if submit_answer:
            if guess == problem['answer']:
                st.success("🎉 **Case Solved!** Excellent detective work!")
                
                # Award points based on level and streak
                base_points = 10 * st.session_state.current_level
                streak_bonus = min(st.session_state.correct_streak * 2, 20)
                total_points = base_points + streak_bonus
                
                st.session_state.points += total_points
                st.session_state.problems_solved += 1
                st.session_state.correct_streak += 1
                
                # Add to history
                st.session_state.problem_history.append({
                    'problem': problem['expression'],
                    'correct': True,
                    'level': problem['level'],
                    'points': total_points,
                    'timestamp': datetime.now()
                })
                
                if streak_bonus > 0:
                    st.info(f"🔥 **Streak Bonus:** +{streak_bonus} points for {st.session_state.correct_streak} correct answers in a row!")
                
                # Level up check
                if st.session_state.problems_solved % 5 == 0:
                    st.session_state.current_level += 1
                    st.balloons()
                    st.success(f"🚀 **PROMOTED!** Welcome to Detective Level {st.session_state.current_level}!")
                
                # Generate new problem
                st.session_state.current_problem = generate_problem(st.session_state.current_level)
                st.session_state.show_hint = False
                
            else:
                st.error(f"❌ **Not quite right!** The correct answer is **{problem['answer']}**")
                st.info("🕵️ Keep investigating! Every great detective learns from each case.")
                
                # Reset streak and add to history
                st.session_state.correct_streak = 0
                st.session_state.problem_history.append({
                    'problem': problem['expression'],
                    'correct': False,
                    'level': problem['level'],
                    'points': 0,
                    'timestamp': datetime.now()
                })
                
                # Show the hint automatically after wrong answer
                st.session_state.show_hint = True
    
    else:
        st.warning("🕵️ **Join the Detective Academy** by entering your name in the sidebar to start solving mathematical mysteries!")

with tab3:
    st.markdown("## 📊 Detective Progress Dashboard")
    
    if st.session_state.student_name and st.session_state.problem_history:
        # Performance metrics
        col1, col2, col3, col4 = st.columns(4)
        
        total_problems = len(st.session_state.problem_history)
        correct_problems = sum(1 for p in st.session_state.problem_history if p['correct'])
        accuracy = (correct_problems / total_problems * 100) if total_problems > 0 else 0
        
        with col1:
            st.metric("Total Cases", total_problems)
        with col2:
            st.metric("Solved Cases", correct_problems)
        with col3:
            st.metric("Accuracy Rate", f"{accuracy:.1f}%")
        with col4:
            st.metric("Current Streak", st.session_state.correct_streak)
        
        # Progress visualization
        if len(st.session_state.problem_history) >= 5:
            # Recent performance chart
            recent_history = st.session_state.problem_history[-10:]  # Last 10 problems
            df = pd.DataFrame(recent_history)
            df['Problem_Number'] = range(len(df))
            df['Success_Rate'] = df['correct'].astype(int)
            
            fig = px.line(df, x='Problem_Number', y='Success_Rate', 
                         title="Recent Case Success Rate",
                         labels={'Problem_Number': 'Recent Cases', 'Success_Rate': 'Solved (1) or Not (0)'})
            fig.update_traces(mode='markers+lines')
            st.plotly_chart(fig, use_container_width=True)
            
            # Points earned over time
            df['Cumulative_Points'] = df['points'].cumsum()
            fig2 = px.bar(df, x='Problem_Number', y='points',
                         title="Points Earned per Case",
                         labels={'Problem_Number': 'Case Number', 'points': 'Points Earned'})
            st.plotly_chart(fig2, use_container_width=True)
    
    elif st.session_state.student_name:
        st.info("🕵️ Start solving cases to see your progress statistics!")
    else:
        st.warning("👮‍♀️ Sign in to view your detective progress!")

with tab4:
    st.markdown("## 🏆 Detective Academy Achievements")
    
    if st.session_state.student_name:
        # Achievement logic
        achievements = []
        
        if st.session_state.problems_solved >= 1:
            achievements.append(("🥉", "First Case", "Solved your first mystery"))
        if st.session_state.problems_solved >= 5:
            achievements.append(("🥈", "Junior Detective", "Reached Level 2"))
        if st.session_state.problems_solved >= 10:
            achievements.append(("🥇", "Senior Detective", "Solved 10 cases"))
        if st.session_state.problems_solved >= 25:
            achievements.append(("🏆", "Master Detective", "Solved 25 cases"))
        if st.session_state.current_level >= 5:
            achievements.append(("⭐", "High Level", "Reached Level 5"))
        if st.session_state.correct_streak >= 3:
            achievements.append(("🔥", "Hot Streak", "3+ correct in a row"))
        if st.session_state.points >= 100:
            achievements.append(("💎", "Point Master", "Earned 100+ points"))
        if st.session_state.current_level >= 10:
            achievements.append(("👑", "Academy Legend", "Reached Level 10"))
        
        # Display earned achievements
        st.markdown("### 🎖️ Earned Badges")
        if achievements:
            cols = st.columns(min(len(achievements), 4))
            for i, (emoji, name, desc) in enumerate(achievements):
                with cols[i % 4]:
                    st.markdown(f"""
                    <div class="achievement-badge">
                    {emoji}<br>{name}<br><small>{desc}</small>
                    </div>
                    """, unsafe_allow_html=True)
        else:
            st.info("🕵️ Start solving cases to earn your first achievement badge!")
        
        # Show next achievements to unlock
        st.markdown("### 🎯 Next Goals")
        next_goals = []
        if st.session_state.problems_solved < 5:
            next_goals.append(f"🥈 Solve {5 - st.session_state.problems_solved} more cases to become a Junior Detective")
        if st.session_state.problems_solved < 10:
            next_goals.append(f"🥇 Solve {10 - st.session_state.problems_solved} more cases to become a Senior Detective")
        if st.session_state.current_level < 5:
            next_goals.append(f"⭐ Reach Level 5 ({5 - st.session_state.current_level} levels to go)")
        
        for goal in next_goals[:3]:  # Show top 3 goals
            st.write(f"• {goal}")
    
    else:
        st.warning("🕵️ Join the Academy to start earning achievement badges!")

# --- Footer ---
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 1rem;">
<p>🕵️‍♀️🕵️‍♂️ <strong>MathCraft Detective Academy</strong> | Hands-On Mathematical Thinking</p>
<p>Join Detectives Amirah and Amari on mathematical adventures!</p>
<p>Developed by Xavier Honablue M.Ed. | Building mathematical minds through investigation!</p>
</div>
""", unsafe_allow_html=True)
