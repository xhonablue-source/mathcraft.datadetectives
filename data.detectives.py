import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import random
from datetime import datetime
import math

# Page configuration
st.set_page_config(
    page_title="MathCraft Detective Academy",
    page_icon="🕵️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for MathCraft styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        color: white;
        margin-bottom: 2rem;
    }
    .detective-profile {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #667eea;
        margin: 1rem 0;
        text-align: center;
    }
    .math-problem {
        background: #e3f2fd;
        padding: 1.5rem;
        border-radius: 8px;
        border-left: 4px solid #2196f3;
        margin: 1rem 0;
        font-size: 1.2em;
    }
    .success-badge {
        background: linear-gradient(45deg, #4CAF50, #45a049);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        display: inline-block;
        font-weight: bold;
        margin: 0.5rem;
    }
    .challenge-card {
        background: #fff3cd;
        border: 1px solid #ffeaa7;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    .detective-avatar {
        width: 100px;
        height: 100px;
        border-radius: 50%;
        margin: 0 auto 1rem auto;
        display: block;
        background: linear-gradient(45deg, #8B4513, #D2691E);
        color: white;
        line-height: 100px;
        text-align: center;
        font-size: 2em;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'current_level' not in st.session_state:
    st.session_state.current_level = 1
if 'points' not in st.session_state:
    st.session_state.points = 0
if 'problems_solved' not in st.session_state:
    st.session_state.problems_solved = 0
if 'current_problem' not in st.session_state:
    st.session_state.current_problem = None
if 'student_name' not in st.session_state:
    st.session_state.student_name = ""

# Header
st.markdown("""
<div class="main-header">
    <h1>🕵️ MathCraft Detective Academy</h1>
    <p><em>Hands-On Mathematical Thinking</em></p>
    <p>Join Detectives Amara and Jamal on mathematical adventures!</p>
    <p>© All Rights Reserved - Xavier Honablue M.Ed</p>
</div>
""", unsafe_allow_html=True)

# Sidebar - Student Profile
st.sidebar.title("🎓 Student Detective Profile")
if not st.session_state.student_name:
    name = st.sidebar.text_input("Enter your detective name:")
    if st.sidebar.button("Join the Academy"):
        if name:
            st.session_state.student_name = name
            st.rerun()
else:
    st.sidebar.markdown(f"**Detective:** {st.session_state.student_name}")
    st.sidebar.markdown(f"**Level:** {st.session_state.current_level}")
    st.sidebar.markdown(f"**Points:** {st.session_state.points}")
    st.sidebar.markdown(f"**Cases Solved:** {st.session_state.problems_solved}")

# Math problem generators
def generate_addition_problem(level):
    if level == 1:
        a, b = random.randint(1, 10), random.randint(1, 10)
    elif level == 2:
        a, b = random.randint(10, 50), random.randint(10, 50)
    else:
        a, b = random.randint(50, 200), random.randint(50, 200)
    
    return {
        'question': f"Detective Amara found {a} clues on Monday and {b} clues on Tuesday. How many clues did she find in total?",
        'problem': f"{a} + {b} = ?",
        'answer': a + b,
        'type': 'addition'
    }

def generate_subtraction_problem(level):
    if level == 1:
        a, b = random.randint(10, 20), random.randint(1, 10)
    elif level == 2:
        a, b = random.randint(50, 100), random.randint(10, 50)
    else:
        a, b = random.randint(100, 500), random.randint(50, 200)
    
    if b > a:
        a, b = b, a
    
    return {
        'question': f"Detective Jamal had {a} pieces of evidence. He used {b} pieces to solve a case. How many pieces does he have left?",
        'problem': f"{a} - {b} = ?",
        'answer': a - b,
        'type': 'subtraction'
    }

def generate_multiplication_problem(level):
    if level == 1:
        a, b = random.randint(1, 5), random.randint(1, 5)
    elif level == 2:
        a, b = random.randint(2, 10), random.randint(2, 10)
    else:
        a, b = random.randint(5, 15), random.randint(5, 15)
    
    return {
        'question': f"Detective Amara organized evidence into {a} boxes with {b} items in each box. How many items total?",
        'problem': f"{a} × {b} = ?",
        'answer': a * b,
        'type': 'multiplication'
    }

def generate_division_problem(level):
    if level == 1:
        b = random.randint(2, 5)
        a = b * random.randint(2, 10)
    elif level == 2:
        b = random.randint(2, 10)
        a = b * random.randint(5, 15)
    else:
        b = random.randint(5, 15)
        a = b * random.randint(10, 20)
    
    return {
        'question': f"Detective Jamal needs to divide {a} case files equally among {b} detectives. How many files does each detective get?",
        'problem': f"{a} ÷ {b} = ?",
        'answer': a // b,
        'type': 'division'
    }

def generate_word_problem(level):
    problems = [
        generate_addition_problem(level),
        generate_subtraction_problem(level),
        generate_multiplication_problem(level),
        generate_division_problem(level)
    ]
    return random.choice(problems)

# Main navigation
tab1, tab2, tab3, tab4 = st.tabs(["🏠 Detective HQ", "🧮 Math Missions", "📊 Progress Tracker", "🏆 Achievements"])

with tab1:
    st.markdown("## Welcome to MathCraft Detective Academy!")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="detective-profile">
        <div class="detective-avatar">👧🏾</div>
        <h3>Detective Amara</h3>
        <p><strong>Specialty:</strong> Addition & Multiplication Mysteries</p>
        <p><em>"Every math problem is a puzzle waiting to be solved!"</em></p>
        <p><strong>Superpower:</strong> Pattern Recognition</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="detective-profile">
        <div class="detective-avatar">👦🏾</div>
        <h3>Detective Jamal</h3>
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

with tab2:
    st.markdown("## 🧮 Math Detective Missions")
    
    if st.session_state.student_name:
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("### Current Case File")
            
            # Generate new problem button
            if st.button("🔍 New Case Assignment") or st.session_state.current_problem is None:
                st.session_state.current_problem = generate_word_problem(st.session_state.current_level)
            
            if st.session_state.current_problem:
                problem = st.session_state.current_problem
                
                st.markdown(f"""
                <div class="math-problem">
                <h4>🕵️ Case #{st.session_state.problems_solved + 1}</h4>
                <p>{problem['question']}</p>
                <h3>{problem['problem']}</h3>
                </div>
                """, unsafe_allow_html=True)
                
                # Answer input
                user_answer = st.number_input("Your solution:", value=0, step=1)
                
                col_submit, col_hint = st.columns(2)
                
                with col_submit:
                    if st.button("🔍 Submit Solution"):
                        if user_answer == problem['answer']:
                            st.success("🎉 Case Solved! Excellent detective work!")
                            st.session_state.points += 10 * st.session_state.current_level
                            st.session_state.problems_solved += 1
                            
                            # Level up logic
                            if st.session_state.problems_solved % 5 == 0:
                                st.session_state.current_level += 1
                                st.balloons()
                                st.success(f"🏆 Promoted to Level {st.session_state.current_level}!")
                            
                            st.session_state.current_problem = None
                        else:
                            st.error(f"Not quite right. The correct answer is {problem['answer']}. Try the next case!")
                            if problem['type'] == 'addition':
                                st.info("💡 **Detective Amara's Tip:** When adding, count all the items together!")
                            elif problem['type'] == 'subtraction':
                                st.info("💡 **Detective Jamal's Tip:** When subtracting, think about how many are left after taking some away!")
                            elif problem['type'] == 'multiplication':
                                st.info("💡 **Detective Amara's Tip:** Multiplication is like adding groups together!")
                            else:
                                st.info("💡 **Detective Jamal's Tip:** Division means sharing equally among groups!")
                
                with col_hint:
                    if st.button("💡 Detective Hint"):
                        if problem['type'] == 'addition':
                            st.info("🕵️‍♀️ **Amara says:** Count up from the first number!")
                        elif problem['type'] == 'subtraction':
                            st.info("🕵️‍♂️ **Jamal says:** Start with the bigger number and count backwards!")
                        elif problem['type'] == 'multiplication':
                            st.info("🕵️‍♀️ **Amara says:** Try making groups and adding them up!")
                        else:
                            st.info("🕵️‍♂️ **Jamal says:** How many groups of the smaller number fit into the bigger number?")
        
        with col2:
            st.markdown("### 📈 Detective Stats")
            st.metric("Current Level", st.session_state.current_level)
            st.metric("Total Points", st.session_state.points)
            st.metric("Cases Solved", st.session_state.problems_solved)
            
            # Progress to next level
            problems_to_next_level = 5 - (st.session_state.problems_solved % 5)
            if problems_to_next_level == 5:
                problems_to_next_level = 0
            st.metric("Cases to Next Level", problems_to_next_level)
            
            st.markdown("### 🎯 Quick Practice")
            practice_type = st.selectbox("Practice Type:", 
                                       ["Addition", "Subtraction", "Multiplication", "Division"])
            
            if st.button("Quick Practice Problem"):
                if practice_type == "Addition":
                    prob = generate_addition_problem(1)
                elif practice_type == "Subtraction":
                    prob = generate_subtraction_problem(1)
                elif practice_type == "Multiplication":
                    prob = generate_multiplication_problem(1)
                else:
                    prob = generate_division_problem(1)
                
                st.write(f"**Quick Case:** {prob['problem']}")
                quick_answer = st.number_input("Quick Answer:", value=0, key="quick")
                if st.button("Check Quick Answer"):
                    if quick_answer == prob['answer']:
                        st.success("✅ Correct!")
                    else:
                        st.error(f"❌ Answer: {prob['answer']}")
    else:
        st.warning("👮‍♀️ Please enter your detective name in the sidebar to start solving cases!")

with tab3:
    st.markdown("## 📊 Detective Progress Tracker")
    
    if st.session_state.student_name:
        # Create progress visualization
        levels = list(range(1, st.session_state.current_level + 1))
        problems_per_level = []
        
        for level in levels:
            if level < st.session_state.current_level:
                problems_per_level.append(5)
            else:
                problems_per_level.append(st.session_state.problems_solved % 5 if st.session_state.problems_solved % 5 != 0 else 5)
        
        # Progress chart
        fig = px.bar(x=levels, y=problems_per_level, 
                    title="Cases Solved by Level",
                    labels={'x': 'Detective Level', 'y': 'Cases Solved'})
        fig.update_traces(marker_color='#667eea')
        st.plotly_chart(fig, use_container_width=True)
        
        # Achievements timeline
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 🏅 Achievements Unlocked")
            achievements = []
            if st.session_state.problems_solved >= 1:
                achievements.append("🥉 First Case Solved")
            if st.session_state.problems_solved >= 5:
                achievements.append("🥈 Level 2 Detective")
            if st.session_state.problems_solved >= 10:
                achievements.append("🥇 Math Detective Expert")
            if st.session_state.problems_solved >= 20:
                achievements.append("🏆 Master Detective")
            
            for achievement in achievements:
                st.markdown(f"✅ {achievement}")
        
        with col2:
            st.markdown("### 📈 Performance Stats")
            if st.session_state.problems_solved > 0:
                accuracy = 85 + random.randint(-10, 10)  # Simulated accuracy
                st.metric("Accuracy Rate", f"{accuracy}%")
                st.metric("Average Points per Case", f"{st.session_state.points // max(st.session_state.problems_solved, 1)}")
                st.metric("Current Streak", random.randint(1, 5))
    else:
        st.info("Sign in to view your progress!")

with tab4:
    st.markdown("## 🏆 Detective Academy Achievements")
    
    st.markdown("### 🎖️ Available Badges")
    
    badge_cols = st.columns(3)
    
    badges = [
        ("🥉", "Rookie Detective", "Solve your first case", st.session_state.problems_solved >= 1),
        ("🥈", "Junior Detective", "Reach Level 2", st.session_state.current_level >= 2),
        ("🥇", "Senior Detective", "Solve 10 cases", st.session_state.problems_solved >= 10),
        ("🏆", "Master Detective", "Solve 20 cases", st.session_state.problems_solved >= 20),
        ("⭐", "Addition Expert", "Master addition problems", st.session_state.problems_solved >= 5),
        ("🌟", "Math Champion", "Reach Level 5", st.session_state.current_level >= 5),
        ("💎", "Perfect Detective", "Solve 50 cases", st.session_state.problems_solved >= 50),
        ("👑", "Academy Legend", "Reach Level 10", st.session_state.current_level >= 10),
        ("🔥", "Hot Streak", "Solve 5 in a row", False)  # Simulated
    ]
    
    for i, (emoji, name, description, earned) in enumerate(badges):
        with badge_cols[i % 3]:
            if earned:
                st.markdown(f"""
                <div class="success-badge">
                {emoji} {name}<br>
                <small>{description}</small>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div style="opacity: 0.3; text-align: center; padding: 1rem;">
                {emoji} {name}<br>
                <small>{description}</small>
                </div>
                """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 1rem;">
<p>🕵️‍♀️🕵️‍♂️ <strong>MathCraft Detective Academy</strong> | Hands-On Mathematical Thinking</p>
<p>Join Detectives Amara and Jamal on mathematical adventures!</p>
<p>Developed by Xavier Honablue M.Ed. | Building mathematical minds through investigation!</p>
</div>
""", unsafe_allow_html=True)
