import streamlit as st

# --- Tool Functions ---
def analyze_goal(text):
    return "🎯 Goal: Lose 5kg in 2 months"

def generate_meal_plan(veg=False):
    if veg:
        return """
- 🥣 **Breakfast:** Oats with almond milk & banana  
- 🥗 **Lunch:** Chickpea salad with olive oil dressing  
- 🍛 **Dinner:** Lentil curry with brown rice  
"""
    return "🍗 Non-veg meal plan coming soon..."

def handle_injury(context):
    return """
- 🚫 Avoid squats and lunges  
- ✅ Do seated leg extensions  
- 🚴 Try low-impact cycling  
- 🏋️ Use resistance bands  
"""

def handle_diabetic_diet():
    return """
- 🚫 Avoid sugar & refined carbs  
- ✅ Eat whole grains, fiber-rich foods  
- 🍓 Prefer low-GI fruits like berries  
"""

def escalate_to_human():
    return "📞 A human trainer will contact you. [Book Now](https://example.com/booking) 💬"

# --- Streamlit UI Setup ---
st.set_page_config(
    page_title="💪 Faj's AI Wellness Planner",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.markdown(
    """
    <h1 style='text-align:center; color:#4CAF50;'>🧘‍♀️ Faj's AI Health & Wellness Dashboard</h1>
    <p style='text-align:center; font-size:16px; color:#666;'>Get personalized wellness plans tailored for YOU!</p>
    """,
    unsafe_allow_html=True,
)

st.markdown("---")

# --- Help / Examples ---
with st.expander("❓ What can I ask? (Click to expand)", expanded=True):
    st.markdown("""
    <ul style='font-size:16px;'>
    <li>🎯 <b>I want to lose 5kg in 2 months</b></li>
    <li>🥗 <b>I'm vegetarian, make me a diet plan</b></li>
    <li>🍭 <b>I'm diabetic, what should I eat?</b></li>
    <li>🦵 <b>I have knee pain, suggest exercises</b></li>
    <li>📞 <b>I want to talk to a real trainer</b></li>
    </ul>
    """, unsafe_allow_html=True)

st.markdown("**Quick prompts:**")
cols = st.columns([1,1,1])

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

if 'user_input' not in st.session_state:
    st.session_state['user_input'] = ""

def set_quick_prompt(prompt):
    st.session_state['user_input'] = prompt

with cols[0]:
    if st.button("🏋️ Lose 5kg"):
        set_quick_prompt("I want to lose 5kg in 2 months")

with cols[1]:
    if st.button("🥦 I'm vegetarian"):
        set_quick_prompt("I'm vegetarian")

with cols[2]:
    if st.button("🩺 I'm diabetic"):
        set_quick_prompt("I'm diabetic")

st.markdown("---")

# --- Chat Input ---
user_input = st.text_input("💬 Your message here...", value=st.session_state['user_input'], key="input_box")

if user_input and user_input != "":
    # Save user input
    st.session_state['chat_history'].append({"role": "user", "content": user_input})
    st.session_state['user_input'] = ""  # reset input box

    lowered = user_input.lower()

    # Response collection
    responses = []

    # 1. Goal Analyzer
    if "lose" in lowered and "kg" in lowered:
        responses.append(("🧠 Goal Analysis", analyze_goal(user_input)))

    # 2. Vegetarian Meal Plan
    if "vegetarian" in lowered:
        responses.append(("🥗 Vegetarian Meal Plan", generate_meal_plan(veg=True)))

    # 3. Injury Support
    if "knee pain" in lowered or "injury" in lowered:
        responses.append(("🦵 Injury Support Plan", handle_injury(user_input)))

    # 4. Diabetic Diet
    if "diabetic" in lowered:
        responses.append(("🍭 Diabetic-Friendly Diet", handle_diabetic_diet()))

    # 5. Escalation
    if "real trainer" in lowered or "talk to" in lowered:
        responses.append(("📞 Escalation", escalate_to_human()))

    # Save assistant responses
    for title, content in responses:
        st.session_state['chat_history'].append({"role": "assistant", "title": title, "content": content})

# --- Display Chat History ---
for msg in st.session_state['chat_history']:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"### {msg['title']}")
        st.markdown(msg['content'])
        st.markdown("---")
