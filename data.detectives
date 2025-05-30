import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="MathCraft Data Detectives",
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
    .investigation-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #667eea;
        margin: 1rem 0;
    }
    .step-header {
        background: #e3f2fd;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #2196f3;
        margin: 1rem 0;
    }
    .detective-badge {
        background: linear-gradient(45deg, #ff6b6b, #feca57);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        display: inline-block;
        font-weight: bold;
        margin: 0.5rem;
    }
    .math-fact {
        background: #fff3cd;
        border: 1px solid #ffeaa7;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1>🕵️ MathCraft Data Detectives</h1>
    <p><em>Hands-On Mathematical Thinking</em></p>
    <p>Meet Detective Maya and Detective Marcus - your mathematical investigation guides!</p>
    <p>© All Rights Reserved - Xavier Honablue M.Ed</p>
</div>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("🔍 Detective Dashboard")
st.sidebar.markdown("👥 **Your Guides:** Detective Maya & Marcus")
investigation_mode = st.sidebar.selectbox(
    "Choose Your Investigation:",
    ["🏠 Detective HQ", "📏 Maya's Measurement Mystery", "🌈 Marcus's Color Pattern Case", 
     "🎲 Maya's Number Preference Puzzle", "📐 Marcus's Shape Hunter Challenge", "📊 Data Gallery"]
)

# Initialize session state for data storage
if 'measurement_data' not in st.session_state:
    st.session_state.measurement_data = pd.DataFrame(columns=['Name', 'Height_inches', 'Arm_Span_inches'])
if 'color_data' not in st.session_state:
    st.session_state.color_data = pd.DataFrame(columns=['Color', 'Count'])
if 'number_data' not in st.session_state:
    st.session_state.number_data = pd.DataFrame(columns=['Number', 'Count'])
if 'shape_data' not in st.session_state:
    st.session_state.shape_data = pd.DataFrame(columns=['Shape', 'Count'])

# Main content based on selection
if investigation_mode == "🏠 Detective HQ":
    st.markdown("## Welcome to MathCraft Detective Headquarters!")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class="investigation-card">
        <h3>🧠 The MathCraft Detective Framework</h3>
        <p>Every great mathematical detective follows these four steps:</p>
        </div>
        """, unsafe_allow_html=True)
        
        steps = [
            ("🔍 INVESTIGATE", "What mystery will I solve?", "Choose your mathematical investigation"),
            ("📊 COLLECT", "How will I gather mathematical evidence?", "Use systematic data collection methods"),
            ("📈 VISUALIZE", "How can I show my mathematical thinking?", "Choose the best way to represent your data"),
            ("🎯 CONCLUDE", "What mathematical story does my data tell?", "Draw evidence-based conclusions")
        ]
        
        for i, (icon, question, description) in enumerate(steps, 1):
            st.markdown(f"""
            <div class="step-header">
            <h4>Step {i}: {icon} {question}</h4>
            <p>{description}</p>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 👥 Meet Your Detective Guides")
        st.markdown("""
        **🕵️‍♀️ Detective Maya** - Pattern Recognition Expert  
        *"I love finding mathematical patterns hidden in everyday data!"*
        
        **🕵️‍♂️ Detective Marcus** - Measurement Specialist  
        *"Every measurement tells a story if you know how to listen!"*
        """)
        
        st.markdown("### 🏆 Available Investigations")
        investigations = [
            "📏 Maya's Measurement Mystery",
            "🌈 Marcus's Color Pattern Case", 
            "🎲 Maya's Number Preference Puzzle",
            "📐 Marcus's Shape Hunter Challenge"
        ]
        for inv in investigations:
            st.markdown(f'<div class="detective-badge">{inv}</div>', unsafe_allow_html=True)
        
        st.markdown("### 📊 Mathematical Tools")
        st.write("✏️ Maya's Measurement Pencil")
        st.write("📐 Marcus's Precision Tools")
        st.write("📋 Detective Data Sheets")
        st.write("🧮 Team Mathematical Reasoning")

elif investigation_mode == "📏 Measurement Mystery":
    st.markdown("## 📏 Detective Maya's Measurement Mystery")
    st.markdown("**Maya's Investigation Question:** Do arm spans equal heights for most people?")
    
    st.info("🕵️‍♀️ **Detective Maya says:** 'Let's use our mathematical measuring skills to solve this mystery together!'")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 📊 Data Collection")
        with st.form("measurement_form"):
            name = st.text_input("Student Name")
            height = st.number_input("Height (inches)", min_value=30.0, max_value=80.0, step=0.5)
            arm_span = st.number_input("Arm Span (inches)", min_value=30.0, max_value=80.0, step=0.5)
            
            if st.form_submit_button("Add Detective Data"):
                if name and height and arm_span:
                    new_data = pd.DataFrame({
                        'Name': [name],
                        'Height_inches': [height],
                        'Arm_Span_inches': [arm_span]
                    })
                    st.session_state.measurement_data = pd.concat([st.session_state.measurement_data, new_data], ignore_index=True)
                    st.success(f"Added data for {name}!")
    
    with col2:
        st.markdown("### 🎯 Mathematical Analysis")
        if not st.session_state.measurement_data.empty:
            # Calculate differences
            df = st.session_state.measurement_data.copy()
            df['Difference'] = df['Arm_Span_inches'] - df['Height_inches']
            
            # Display data table
            st.dataframe(df)
            
            # Mathematical insights
            avg_diff = df['Difference'].mean()
            st.markdown(f"""
            <div class="math-fact">
            <strong>Mathematical Discovery:</strong><br>
            Average difference: {avg_diff:.2f} inches<br>
            Pattern: {"Arm spans tend to be longer" if avg_diff > 0 else "Heights tend to be longer" if avg_diff < 0 else "They're about equal"}
            </div>
            """, unsafe_allow_html=True)
    
    # Visualization
    if not st.session_state.measurement_data.empty:
        st.markdown("### 📈 Mathematical Visualization")
        df = st.session_state.measurement_data.copy()
        df['Difference'] = df['Arm_Span_inches'] - df['Height_inches']
        
        # Scatter plot
        fig = px.scatter(df, x='Height_inches', y='Arm_Span_inches', 
                        hover_data=['Name'], title="Height vs Arm Span Investigation")
        fig.add_line(x=[df['Height_inches'].min(), df['Height_inches'].max()], 
                    y=[df['Height_inches'].min(), df['Height_inches'].max()], 
                    line_dash="dash", line_color="red")
        fig.update_layout(
            xaxis_title="Height (inches)",
            yaxis_title="Arm Span (inches)"
        )
        st.plotly_chart(fig, use_container_width=True)

elif investigation_mode == "🌈 Color Pattern Detective":
    st.markdown("## 🌈 Detective Marcus's Color Pattern Case")
    st.markdown("**Marcus's Investigation Question:** What colors appear most frequently in our classroom?")
    
    st.info("🕵️‍♂️ **Detective Marcus says:** 'Every color has a story to tell. Let's count systematically and see what patterns emerge!'")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 🎨 Color Data Collection")
        colors = ["Red", "Blue", "Green", "Yellow", "Purple", "Orange", "Pink", "Black", "White", "Brown"]
        
        selected_color = st.selectbox("Choose a color to count:", colors)
        count = st.number_input("How many did you find?", min_value=0, max_value=50, step=1)
        
        if st.button("Record Color Data"):
            if selected_color and count > 0:
                # Check if color already exists
                if selected_color in st.session_state.color_data['Color'].values:
                    st.session_state.color_data.loc[st.session_state.color_data['Color'] == selected_color, 'Count'] += count
                else:
                    new_data = pd.DataFrame({'Color': [selected_color], 'Count': [count]})
                    st.session_state.color_data = pd.concat([st.session_state.color_data, new_data], ignore_index=True)
                st.success(f"Recorded {count} {selected_color} items!")
    
    with col2:
        st.markdown("### 📊 Mathematical Analysis")
        if not st.session_state.color_data.empty:
            df = st.session_state.color_data.copy()
            df = df.sort_values('Count', ascending=False)
            
            st.dataframe(df)
            
            # Mathematical insights
            total_items = df['Count'].sum()
            most_common = df.iloc[0]['Color']
            most_count = df.iloc[0]['Count']
            
            st.markdown(f"""
            <div class="math-fact">
            <strong>Mathematical Discovery:</strong><br>
            Total items counted: {total_items}<br>
            Most common color: {most_common} ({most_count} items)<br>
            Percentage: {(most_count/total_items)*100:.1f}%
            </div>
            """, unsafe_allow_html=True)
    
    # Visualization
    if not st.session_state.color_data.empty:
        st.markdown("### 📈 Color Distribution Chart")
        df = st.session_state.color_data.copy()
        
        fig = px.bar(df, x='Color', y='Count', 
                    title="Color Frequency Investigation",
                    color='Color',
                    color_discrete_map={
                        'Red': '#ff4444', 'Blue': '#4444ff', 'Green': '#44ff44',
                        'Yellow': '#ffff44', 'Purple': '#ff44ff', 'Orange': '#ff8844',
                        'Pink': '#ffaaaa', 'Black': '#444444', 'White': '#dddddd',
                        'Brown': '#8b4513'
                    })
        st.plotly_chart(fig, use_container_width=True)

elif investigation_mode == "🎲 Number Preference Mystery":
    st.markdown("## 🎲 Detective Maya's Number Preference Puzzle")
    st.markdown("**Maya's Investigation Question:** Do students have favorite numbers between 1-20? Are there patterns?")
    
    st.info("🕵️‍♀️ **Detective Maya says:** 'Numbers have personalities! Let's discover which ones are most popular and why.'")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 🔢 Number Collection")
        favorite_number = st.selectbox("Favorite Number (1-20):", list(range(1, 21)))
        
        if st.button("Record Number Choice"):
            if str(favorite_number) in st.session_state.number_data['Number'].values:
                st.session_state.number_data.loc[st.session_state.number_data['Number'] == str(favorite_number), 'Count'] += 1
            else:
                new_data = pd.DataFrame({'Number': [str(favorite_number)], 'Count': [1]})
                st.session_state.number_data = pd.concat([st.session_state.number_data, new_data], ignore_index=True)
            st.success(f"Recorded choice: {favorite_number}")
    
    with col2:
        st.markdown("### 🧮 Mathematical Analysis")
        if not st.session_state.number_data.empty:
            df = st.session_state.number_data.copy()
            df['Number'] = df['Number'].astype(int)
            df = df.sort_values('Number')
            
            st.dataframe(df)
            
            # Mathematical insights
            total_responses = df['Count'].sum()
            most_popular = df.loc[df['Count'].idxmax(), 'Number']
            most_count = df['Count'].max()
            
            st.markdown(f"""
            <div class="math-fact">
            <strong>Mathematical Discovery:</strong><br>
            Total responses: {total_responses}<br>
            Most popular number: {most_popular} ({most_count} votes)<br>
            Range of choices: {df['Number'].min()} to {df['Number'].max()}
            </div>
            """, unsafe_allow_html=True)
    
    # Visualization
    if not st.session_state.number_data.empty:
        st.markdown("### 📈 Number Preference Distribution")
        df = st.session_state.number_data.copy()
        df['Number'] = df['Number'].astype(int)
        df = df.sort_values('Number')
        
        fig = px.bar(df, x='Number', y='Count', 
                    title="Favorite Number Investigation",
                    color='Count',
                    color_continuous_scale='viridis')
        fig.update_layout(xaxis_title="Favorite Number", yaxis_title="Number of Votes")
        st.plotly_chart(fig, use_container_width=True)

elif investigation_mode == "📐 Shape Hunter Challenge":
    st.markdown("## 📐 Detective Marcus's Shape Hunter Challenge")
    st.markdown("**Marcus's Investigation Question:** Which 2D shapes appear most in our classroom environment?")
    
    st.info("🕵️‍♂️ **Detective Marcus says:** 'Shapes are everywhere! Let's hunt them down and see which geometric friends visit our classroom most often.'")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 🔺 Shape Collection")
        shapes = ["Circle", "Square", "Rectangle", "Triangle", "Pentagon", "Hexagon", "Oval", "Diamond"]
        
        selected_shape = st.selectbox("Shape found:", shapes)
        count = st.number_input("How many found?", min_value=0, max_value=50, step=1)
        
        if st.button("Record Shape Data"):
            if selected_shape and count > 0:
                if selected_shape in st.session_state.shape_data['Shape'].values:
                    st.session_state.shape_data.loc[st.session_state.shape_data['Shape'] == selected_shape, 'Count'] += count
                else:
                    new_data = pd.DataFrame({'Shape': [selected_shape], 'Count': [count]})
                    st.session_state.shape_data = pd.concat([st.session_state.shape_data, new_data], ignore_index=True)
                st.success(f"Recorded {count} {selected_shape}(s)!")
    
    with col2:
        st.markdown("### 📊 Geometric Analysis")
        if not st.session_state.shape_data.empty:
            df = st.session_state.shape_data.copy()
            df = df.sort_values('Count', ascending=False)
            
            st.dataframe(df)
            
            # Mathematical insights
            total_shapes = df['Count'].sum()
            most_common_shape = df.iloc[0]['Shape']
            most_count = df.iloc[0]['Count']
            
            st.markdown(f"""
            <div class="math-fact">
            <strong>Geometric Discovery:</strong><br>
            Total shapes found: {total_shapes}<br>
            Most common shape: {most_common_shape} ({most_count} found)<br>
            Shape variety: {len(df)} different types
            </div>
            """, unsafe_allow_html=True)
    
    # Visualization
    if not st.session_state.shape_data.empty:
        st.markdown("### 📈 Shape Distribution Chart")
        df = st.session_state.shape_data.copy()
        
        fig = px.pie(df, values='Count', names='Shape', 
                    title="Shape Distribution in Our Classroom")
        st.plotly_chart(fig, use_container_width=True)

elif investigation_mode == "📊 Data Gallery":
    st.markdown("## 📊 MathCraft Data Gallery")
    st.markdown("### View all your mathematical discoveries!")
    
    # Summary dashboard
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("👥 Measurement Detectives", 
                 len(st.session_state.measurement_data))
    
    with col2:
        color_total = st.session_state.color_data['Count'].sum() if not st.session_state.color_data.empty else 0
        st.metric("🌈 Colors Investigated", color_total)
    
    with col3:
        number_total = st.session_state.number_data['Count'].sum() if not st.session_state.number_data.empty else 0
        st.metric("🎲 Number Preferences", number_total)
    
    with col4:
        shape_total = st.session_state.shape_data['Count'].sum() if not st.session_state.shape_data.empty else 0
        st.metric("📐 Shapes Discovered", shape_total)
    
    # Export options
    st.markdown("### 📋 Export Your Mathematical Evidence")
    
    if st.button("📁 Download All Investigation Data"):
        # Create a summary report
        report_data = {
            "Investigation": [],
            "Total_Data_Points": [],
            "Key_Finding": []
        }
        
        if not st.session_state.measurement_data.empty:
            df = st.session_state.measurement_data.copy()
            df['Difference'] = df['Arm_Span_inches'] - df['Height_inches']
            avg_diff = df['Difference'].mean()
            report_data["Investigation"].append("Measurement Mystery")
            report_data["Total_Data_Points"].append(len(df))
            report_data["Key_Finding"].append(f"Average arm span difference: {avg_diff:.2f} inches")
        
        if not st.session_state.color_data.empty:
            most_common_color = st.session_state.color_data.loc[st.session_state.color_data['Count'].idxmax(), 'Color']
            report_data["Investigation"].append("Color Pattern Detective")
            report_data["Total_Data_Points"].append(st.session_state.color_data['Count'].sum())
            report_data["Key_Finding"].append(f"Most common color: {most_common_color}")
        
        if not st.session_state.number_data.empty:
            most_popular_num = st.session_state.number_data.loc[st.session_state.number_data['Count'].idxmax(), 'Number']
            report_data["Investigation"].append("Number Preference Mystery")
            report_data["Total_Data_Points"].append(st.session_state.number_data['Count'].sum())
            report_data["Key_Finding"].append(f"Most popular number: {most_popular_num}")
        
        if not st.session_state.shape_data.empty:
            most_common_shape = st.session_state.shape_data.loc[st.session_state.shape_data['Count'].idxmax(), 'Shape']
            report_data["Investigation"].append("Shape Hunter Challenge")
            report_data["Total_Data_Points"].append(st.session_state.shape_data['Count'].sum())
            report_data["Key_Finding"].append(f"Most common shape: {most_common_shape}")
        
        if report_data["Investigation"]:
            summary_df = pd.DataFrame(report_data)
            st.dataframe(summary_df)
            
            # Convert to CSV
            csv = summary_df.to_csv(index=False)
            st.download_button(
                label="📥 Download Summary Report",
                data=csv,
                file_name=f"mathcraft_detective_report_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv"
            )
        else:
            st.info("No investigations completed yet! Start collecting data to generate a report.")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 1rem;">
<p>🕵️‍♀️🕵️‍♂️ <strong>MathCraft Data Detectives</strong> | Hands-On Mathematical Thinking</p>
<p>Join Detective Maya and Detective Marcus on mathematical adventures!</p>
<p>Developed by Xavier Honablue M.Ed. | Building mathematical minds through investigation!</p>
</div>
""", unsafe_allow_html=True)

# Sidebar tips
st.sidebar.markdown("---")
st.sidebar.markdown("### 💡 Detective Team Tips")
st.sidebar.markdown("""
- **Maya's Motto**: "Patterns are everywhere if you look closely!"
- **Marcus's Method**: "Measure twice, analyze once!"
- **Team Rule**: Ask questions like a detective
- **Success Secret**: Show your mathematical thinking
""")

st.sidebar.markdown("### 🎯 Learning Goals")
st.sidebar.markdown("""
- Data collection & organization
- Mathematical visualization
- Pattern recognition
- Evidence-based conclusions
""")
