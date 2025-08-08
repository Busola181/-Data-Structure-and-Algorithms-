# goal_tracker.py

import streamlit as st

# ----- Set page config and custom background style
st.set_page_config(page_title="Daily Goal Tracker", layout="centered")

# Inject custom CSS to set green background
st.markdown("""
    <style>
        .main {
            background-color: #e8f5e9;
        }
    </style>
""", unsafe_allow_html=True)

# ----- Title and layout
st.title("✅ Daily Goal Tracker")

# ----- In-memory goals list (array)
if "goals" not in st.session_state:
    st.session_state.goals = []

# ----- Input new goal
new_goal = st.text_input("Add a new goal:")
if st.button("Add Goal"):
    cleaned_goal = new_goal.strip()
    if cleaned_goal and all(cleaned_goal != g["task"] for g in st.session_state.goals):
        st.session_state.goals.append({"task": cleaned_goal, "done": False})
        st.rerun()

# ----- Show goals with checkboxes
st.subheader("Your Goals:")
updated_goals = []
for i, goal in enumerate(st.session_state.goals):
    done = st.checkbox(goal["task"], value=goal["done"], key=i)
    updated_goals.append({"task": goal["task"], "done": done})

# ----- Save checkbox changes if any
if any(g1 != g2 for g1, g2 in zip(st.session_state.goals, updated_goals)):
    st.session_state.goals = updated_goals

# ----- Reset goals
if st.button("🔁 Reset All Goals"):
    st.session_state.goals = []
    st.rerun()

# ----- Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit and Arrays")
