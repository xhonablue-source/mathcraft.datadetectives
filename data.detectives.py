import streamlit as st
import random
import plotly.express as px
import pandas as pd
from datetime import datetime

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
    .detective-avatar {
        width: 120px;
        height: 120px;
        border-radius: 50%;
        margin: 0 auto 1rem auto;
        display: block;
        background: linear-gradient(135deg, #8B4513, #D2691E);
        color: white;
        line-height: 120px;
        text-align: center;
        font-size: 3em;
        border: 4px solid #667eea;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    .amirah-avatar {
        background: linear-gradient(135deg, #8B4513, #D2691E);
    }
    .amari-avatar {
        background: linear-gradient(135deg, #654321, #8B4513);
    }
    .detective-profile {
        background: #f8f9fa;
        padding: 2rem;
        border-radius: 15px;
        border-left: 5px solid #667eea;
        margin: 1rem 0;
        text-align: center;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .mission-card {
        background: linear-gradient(135deg, #e3f2fd, #bbdefb);
        padding: 2rem;
        border-radius: 15px;
        border-left: 5px solid #2196f3;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .achievement-badge {
        background: linear-gradient(45deg, #4CAF50, #45a049);
        color: white;
        padding: 0.8rem 1.2rem;
        border-radius: 25px;
        display: inline-block;
        font-weight: bold;
        margin: 0.5rem;
        font-size: 0.9em;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }
    .hint-box {
        background: linear-gradient(135deg, #fff3cd, #ffeaa7);
        border: 2px solid #f39c12;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .stats-card {
        background: #f1f3f4;
        padding: 1rem;
        border-radius: 8px;
        text-align: center;
        margin: 0.5rem 0;
    }
    .success-message {
        background: linear-gradient(135deg, #d4edda, #c3e6cb);
        border: 2px solid #28a745;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .error-message {
        background: linear-gradient(135deg, #f8d7da, #f5c6cb);
        border: 2px solid #dc3545;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown("""
<div class="main-header">
    <div style="font-size: 4em; margin-bottom: 1rem;">🕵️‍♀️🕵️‍♂️</div>
    <h1>🕵️ MathCraft Detective Academy</h1>
    <p style="font-size: 1.2em;"><em>Hands-On Mathematical Thinking</em></p>
    <p>Join Detectives Amirah and Amari on mathematical adventures!</p>
    <p>© All Rights Reserved - Xavier Honablue M.Ed</p>
</div>
""", unsafe_allow_html=True)

# --- Enhanced Sidebar ---
st.sidebar.title("🎓 Detective Profile")
if not st.session_state.student_name:
    st.sidebar.markdown("### 👋 Welcome, Future Detective!")
    name = st.sidebar.text_input("Enter your detective name:")
    if st.sidebar.button("🚀 Join the Academy", type="primary"):
        if name:
            st.session_state.student_name = name
            st.rerun()
else:
    st.sidebar.markdown(f"### 🕵️ Detective {st.session_state.student_name}")
    
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

# --- Problem Generator ---
def generate_problem(level):
    """Generate a math problem based on difficulty level"""
    difficulty_multiplier = min(level, 10)
    
    base_min = 1 + (difficulty_multiplier - 1) * 3
    base_max = 8 + (difficulty_multiplier - 1) * 8
    
    operations = ["+", "-", "×", "÷"]
    operation = random.choice(operations)
    
    if operation == "+":
        a = random.randint(base_min, base_max)
        b = random.randint(base_min, base_max)
        question = f"Detective Amirah collected {a} pieces of evidence on Monday and {b} pieces on Tuesday. How many pieces did she collect in total?"
        answer = a + b
        hint = "💡 **Amirah's Tip:** Add the numbers together to find the total! Think of it as combining all the evidence."
        
    elif operation == "-":
        a = random.randint(base_max, base_max * 2)
        b = random.randint(base_min, a - 1)
        question = f"Detective Amari had {a} case files. She solved {b} cases and filed them away. How many case files are still on her desk?"
        answer = a - b
        hint = "💡 **Amari's Tip:** Start with the first number and count backwards by the second number!"
        
    elif operation == "×":
        a = random.randint(2, base_min + 4)
        b = random.randint(2, base_min + 3)
        question = f"Detective Amirah organized evidence into {a} boxes with {b} items in each box. How many items are there in total?"
        answer = a * b
        hint = "💡 **Amirah's Tip:** Think of it as adding the same number multiple times! You can also skip count."
        
    else:  # division
        b = random.randint(2, base_min + 3)
        a = b * random.randint(2, base_min + 4)
        question = f"Detective Amari needs to distribute {a} clues equally among {b} investigation teams. How many clues will each team get?"
        answer = a // b
        hint = "💡 **Amari's Tip:** How many groups of the smaller number fit into the larger number? Think about sharing equally!"
    
    return {
        'question': question,
        'expression': f"{a} {operation} {b}",
        'answer': answer,
        'hint': hint,
        'operation': operation,
        'level': level
    }

# --- Main Layout ---
tab1, tab2, tab3, tab4 = st.tabs(["🏠 Detective HQ", "🧮 Math Missions", "📊 Progress Dashboard", "🏆 Achievements"])

with tab1:
    st.markdown("## Meet Your MathCraft Detective Mentors")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="detective-profile">
            <div class="detective-avatar amirah-avatar">👧🏾</div>
            <h2>🕵️‍♀️ Detective Amirah</h2>
            <p><strong>Age:</strong> 10 years old</p>
            <p><strong>Specialty:</strong> Addition & Multiplication Mysteries</p>
            <p><strong>Favorite Quote:</strong> <em>"Every math problem is a puzzle waiting to be solved!"</em></p>
            <p><strong>Detective Badge:</strong> Pattern Recognition Expert</p>
            <p><strong>Superpower:</strong> Finding mathematical patterns in everyday situations</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="detective-profile">
            <div class="detective-avatar amari-avatar">👦🏾</div>
            <h2>🕵️‍♂️ Detective Amari</h2>
            <p><strong>Age:</strong> 11 years old</p>
            <p><strong>Specialty:</strong> Subtraction & Division Cases</p>
            <p><strong>Favorite Quote:</strong> <em>"Math is everywhere—let's investigate together!"</em></p>
            <p><strong>Detective Badge:</strong> Logic & Reasoning Master</p>
            <p><strong>Superpower:</strong> Breaking down complex problems into simple steps</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### 🕵️ The MathCraft Detective Method")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **🔍 Investigation Steps:**
        1. 📖 **Read the case carefully** - What's the mystery?
        2. 🧠 **Identify the clues** - What numbers do we have?
        3. 🔢 **Choose your tool** - Which operation will solve it?
        4. ✅ **Verify your solution** - Does the answer make sense?
        """)
    with col2:
        st.markdown("""
        **🎯 Detective Skills:**
        - 🕵️ **Attention to Detail** - Every word matters
        - 🤔 **Logical Thinking** - Step by step reasoning
        - 📝 **Show Your Work** - Explain your process
        - 🔄 **Learn & Improve** - Every case makes you stronger
        """)

    st.markdown("### 🌟 Why Be a Math Detective?")
    st.markdown("""
    Math detectives like Amirah and Amari use mathematical thinking to solve real-world mysteries! 
    When you practice math through detective work, you're building problem-solving superpowers that 
    help you in school, at home, and everywhere you go. Every problem you solve makes you a better detective!
    """)

with tab2:
    st.markdown("## 🧮 Math Detective Missions")

    if st.session_state.student_name:
        # Mission controls
        col1, col2, col3 = st.columns([3, 1, 1])
        with col1:
            if st.button("🆕 New Mission Assignment", type="primary"):
                st.session_state.current_problem = generate_problem(st.session_state.current_level)
                st.session_state.show_hint = False
        
        with col2:
            if st.button("💡 Get Hint"):
                st.session_state.show_hint = True
        
        with col3:
            if st.button("🔄 Refresh"):
                st.rerun()
        
        # Generate initial problem if none exists
        if st.session_state.current_problem is None:
            st.session_state.current_problem = generate_problem(st.session_state.current_level)

        problem = st.session_state.current_problem
        
        # Display mission
        st.markdown(f"""
        <div class="mission-card">
        <h3>🕵️ Case File #{st.session_state.problems_solved + 1}</h3>
        <h4>Detective Level: {problem['level']} | Difficulty: {'⭐' * min(problem['level'], 5)}</h4>
        <br>
        <h4>📋 Mission Brief:</h4>
        <p style="font-size: 1.1em; line-height: 1.6;">{problem['question']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Show the mathematical expression
        st.markdown("### 🔢 Mathematical Expression:")
        
        # Create larger, more prominent display for the math problem
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown(f"""
            <div style="background: white; padding: 2rem; border-radius: 10px; text-align: center; border: 3px solid #2196f3; margin: 1rem 0;">
            <h1 style="color: #2196f3; font-size: 3em; margin: 0;">{problem['expression']} = ?</h1>
            </div>
            """, unsafe_allow_html=True)
        
        # Show hint if requested
        if st.session_state.show_hint:
            st.markdown(f"""
            <div class="hint-box">
            <h4>🔍 Detective Hint:</h4>
            <p>{problem['hint']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Answer input
        st.markdown("### 🎯 Your Detective Solution:")
        col1, col2 = st.columns([2, 1])
        with col1:
            guess = st.number_input("Enter your answer:", 
                                  step=1, 
                                  format="%i", 
                                  key="answer_input",
                                  help="Type the number that solves the mystery!")
        
        with col2:
            st.markdown("<br>", unsafe_allow_html=True)
            submit_answer = st.button("🔍 Submit Solution", type="primary", use_container_width=True)
        
        # Check answer
        if submit_answer:
            if guess == problem['answer']:
                # Success!
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
                
                st.markdown(f"""
                <div class="success-message">
                <h3>🎉 Case Solved! Outstanding Detective Work!</h3>
                <p>✅ <strong>Correct Answer:</strong> {problem['answer']}</p>
                <p>🏆 <strong>Points Earned:</strong> {total_points} points</p>
                {f'<p>🔥 <strong>Streak Bonus:</strong> +{streak_bonus} points for {st.session_state.correct_streak} correct answers in a row!</p>' if streak_bonus > 0 else ''}
                </div>
                """, unsafe_allow_html=True)
                
                # Level up check
                if st.session_state.problems_solved % 5 == 0:
                    st.session_state.current_level += 1
                    st.balloons()
                    st.success(f"🚀 **PROMOTION!** Welcome to Detective Level {st.session_state.current_level}! Harder cases await!")
                
                # Generate new problem
                st.session_state.current_problem = generate_problem(st.session_state.current_level)
                st.session_state.show_hint = False
                
            else:
                st.session_state.correct_streak = 0
                st.session_state.problem_history.append({
                    'problem': problem['expression'],
                    'correct': False,
                    'level': problem['level'],
                    'points': 0,
                    'timestamp': datetime.now()
                })
                
                st.markdown(f"""
                <div class="error-message">
                <h4>❌ Not quite right, Detective!</h4>
                <p>🎯 <strong>The correct answer is:</strong> {problem['answer']}</p>
                <p>🕵️ <strong>Keep investigating!</strong> Every great detective learns from each case.</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Show the hint automatically after wrong answer
                st.session_state.show_hint = True
    
    else:
        st.markdown("""
        <div style="text-align: center; padding: 3rem; background: #f8f9fa; border-radius: 15px; margin: 2rem 0;">
        <h2>🕵️ Welcome to the Academy!</h2>
        <p style="font-size: 1.2em;">Join Detective Amirah and Detective Amari by entering your name in the sidebar to start solving mathematical mysteries!</p>
        <p>🎯 <strong>What you'll do:</strong> Solve exciting math problems presented as detective cases</p>
        <p>📈 <strong>How you'll grow:</strong> Earn points, level up, and unlock achievements</p>
        <p>🏆 <strong>Why it's fun:</strong> Every problem is an adventure with your detective mentors!</p>
        </div>
        """, unsafe_allow_html=True)

with tab3:
    st.markdown("## 📊 Detective Progress Dashboard")
    
    if st.session_state.student_name and st.session_state.problem_history:
        # Performance metrics
        col1, col2, col3, col4 = st.columns(4)
        
        total_problems = len(st.session_state.problem_history)
        correct_problems = sum(1 for p in st.session_state.problem_history if p['correct'])
        accuracy = (correct_problems / total_problems * 100) if total_problems > 0 else 0
        
        with col1:
            st.metric("Total Cases", total_problems, help="Number of problems attempted")
        with col2:
            st.metric("Solved Cases", correct_problems, help="Number of correct answers")
        with col3:
            st.metric("Accuracy Rate", f"{accuracy:.1f}%", help="Percentage of problems solved correctly")
        with col4:
            st.metric("Current Streak", st.session_state.correct_streak, help="Consecutive correct answers")
        
        # Progress visualization
        if len(st.session_state.problem_history) >= 3:
            st.markdown("### 📈 Your Detective Journey")
            
            # Recent performance chart
            recent_history = st.session_state.problem_history[-10:]
            df = pd.DataFrame(recent_history)
            df['Case_Number'] = range(1, len(df) + 1)
            df['Success'] = df['correct'].astype(int)
            
            fig = px.line(df, x='Case_Number', y='Success', 
                         title="Recent Case Success Rate (Last 10 Cases)",
                         labels={'Case_Number': 'Case Number', 'Success': 'Solved (1) or Not (0)'})
            fig.update_traces(mode='markers+lines', marker_size=8)
            fig.update_layout(yaxis_range=[-0.1, 1.1])
            st.plotly_chart(fig, use_container_width=True)
            
            # Points earned over time
            df['Cumulative_Points'] = df['points'].cumsum()
            fig2 = px.bar(df, x='Case_Number', y='points',
                         title="Points Earned per Case",
                         labels={'Case_Number': 'Case Number', 'points': 'Points Earned'},
                         color='points',
                         color_continuous_scale='viridis')
            st.plotly_chart(fig2, use_container_width=True)
            
            # Performance by level
            level_stats = df.groupby('level').agg({
                'correct': ['count', 'sum', 'mean']
            }).round(2)
            level_stats.columns = ['Total_Cases', 'Solved_Cases', 'Success_Rate']
            level_stats = level_stats.reset_index()
            
            if len(level_stats) > 1:
                fig3 = px.bar(level_stats, x='level', y='Success_Rate',
                             title="Success Rate by Detective Level",
                             labels={'level': 'Detective Level', 'Success_Rate': 'Success Rate'},
                             color='Success_Rate',
                             color_continuous_scale='RdYlGn')
                st.plotly_chart(fig3, use_container_width=True)
    
    elif st.session_state.student_name:
        st.info("🕵️ Start solving cases to see your progress statistics! Your first few cases will unlock detailed analytics.")
    else:
        st.warning("👮‍♀️ Sign in to view your detective progress dashboard!")

with tab4:
    st.markdown("## 🏆 Detective Academy Hall of Fame")
    
    if st.session_state.student_name:
        # Achievement logic
        achievements = []
        
        if st.session_state.problems_solved >= 1:
            achievements.append(("🥉", "First Case Solved", "Completed your first mathematical mystery"))
        if st.session_state.problems_solved >= 5:
            achievements.append(("🥈", "Junior Detective", "Reached Level 2 - You're getting good at this!"))
        if st.session_state.problems_solved >= 10:
            achievements.append(("🥇", "Senior Detective", "Solved 10 cases - You're a real pro!"))
        if st.session_state.problems_solved >= 25:
            achievements.append(("🏆", "Master Detective", "Solved 25 cases - Elite status!"))
        if st.session_state.current_level >= 5:
            achievements.append(("⭐", "High Level Agent", "Reached Level 5 - Advanced detective!"))
        if st.session_state.correct_streak >= 3:
            achievements.append(("🔥", "Hot Streak", "3+ correct answers in a row!"))
        if st.session_state.correct_streak >= 5:
            achievements.append(("🌟", "Super Streak", "5+ correct answers in a row!"))
        if st.session_state.points >= 100:
            achievements.append(("💎", "Point Collector", "Earned 100+ points"))
        if st.session_state.points >= 500:
            achievements.append(("💰", "Point Master", "Earned 500+ points"))
        if st.session_state.current_level >= 10:
            achievements.append(("👑", "Academy Legend", "Reached Level 10 - Legendary!"))
        
        # Display earned achievements
        st.markdown("### 🎖️ Your Detective Badges")
        if achievements:
            # Group achievements in rows of 3
            for i in range(0, len(achievements), 3):
                cols = st.columns(3)
                for j, (emoji, name, desc) in enumerate(achievements[i:i+3]):
                    with cols[j]:
                        st.markdown(f"""
                        <div class="achievement-badge">
                        <div style="font-size: 2em;">{emoji}</div>
                        <strong>{name}</strong><br>
                        <small>{desc}</small>
                        </div>
                        """, unsafe_allow_html=True)
        else:
            st.info("🕵️ Start solving cases to earn your first achievement badge!")
        
        # Show next achievements to unlock
        st.markdown("### 🎯 Next Detective Goals")
        next_goals = []
        if st.session_state.problems_solved < 5:
            next_goals.append(f"🥈 Solve {5 - st.session_state.problems_solved} more cases to become a Junior Detective")
        if st.session_state.problems_solved < 10:
            next_goals.append(f"🥇 Solve {10 - st.session_state.problems_solved} more cases to become a Senior Detective")
        if st.session_state.problems_solved < 25:
            next_goals.append(f"🏆 Solve {25 - st.session_state.problems_solved} more cases to become a Master Detective")
        if st.session_state.current_level < 5:
            next_goals.append(f"⭐ Reach Level 5 ({5 - st.session_state.current_level} levels to go)")
        if st.session_state.points < 100:
            next_goals.append(f"💎 Earn {100 - st.session_state.points} more points to become a Point Collector")
        
        for goal in next_goals[:4]:  # Show top 4 goals
            st.write(f"• {goal}")
            
        # Leaderboard simulation
        st.markdown("### 🏅 Academy Leaderboard (This Month)")
        leaderboard_data = [
            ["🥇 Detective Maya", "Level 8", "850 points"],
            ["🥈 Detective Jordan", "Level 7", "720 points"],
            ["🥉 Detective Alex", "Level 6", "680 points"],
            [f"🎯 Detective {st.session_state.student_name}", f"Level {st.session_state.current_level}", f"{st.session_state.points} points"],
            ["Detective Sam", "Level 5", "520 points"]
        ]
        
        leaderboard_df = pd.DataFrame(leaderboard_data, columns=["Detective", "Level", "Points"])
        st.dataframe(leaderboard_df, use_container_width=True, hide_index=True)
    
    else:
        st.warning("🕵️ Join the Academy to start earning achievement badges and climb the leaderboard!")

# --- Footer ---
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 2rem; background: #f8f9fa; border-radius: 10px;">
<p style="font-size: 1.2em;">🕵️‍♀️🕵️‍♂️ <strong>MathCraft Detective Academy</strong></p>
<p><em>Hands-On Mathematical Thinking</em></p>
<p>Join Detectives Amirah and Amari on mathematical adventures!</p>
<p>Developed by <strong>Xavier Honablue M.Ed.</strong> | Building mathematical minds through investigation!</p>
<p style="margin-top: 1rem; font-size: 0.9em;">🌟 Making math fun, engaging, and accessible for all young detectives! 🌟</p>
</div>
""", unsafe_allow_html=True)
