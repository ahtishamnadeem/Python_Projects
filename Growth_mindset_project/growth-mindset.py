import streamlit as st
import time

st.set_page_config("Growth Mindset", page_icon="🧠", layout="wide")

# Custom CSS for styling
def add_custom_css():
    st.markdown(
        """
        <style>
            body {
                background: linear-gradient(135deg, #667eea, #764ba2);
                background-attachment: fixed;
            }
            .stApp {
                background: rgba(255, 255, 255, 0.8);
                padding: 2rem;
                border-radius: 15px;
                box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.2);
            }
            .sidebar .sidebar-content {
                background: rgba(255, 255, 255, 0.9);
                padding: 20px;
                border-radius: 10px;
            }
            .stButton button {
                background-color: #4CAF50;
                color: white;
                border-radius: 10px;
                padding: 10px 20px;
                font-size: 16px;
                transition: 0.3s;
            }
            .stButton button:hover {
                background-color: #45a049;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

def main():
    add_custom_css()
    
    st.sidebar.title('🧐 Growth Mindset')
    st.sidebar.subheader("👀 How to Apply the Growth Mindset")
    steps = [
        "Identify your current situation.",
        "Reflect on how you can improve.",
        "Break down your challenge into smaller, manageable tasks.",
        "Prioritize your tasks based on their urgency and importance.",
        "Set small, achievable goals for yourself.",
        "Use feedback to continuously improve your performance.",
        "Surround yourself with positive, supportive people.",
        "Be open to feedback and learn from it.",
        "Be patient with yourself and your progress.",
        "Be grateful for the opportunities you have."
    ]
    for step in steps:
        st.sidebar.markdown(f"✅ {step}")

    st.title("🌱 Growth Mindset Project by CodeWithAhtii 😎")
    st.write(
        "A growth mindset is the belief that your abilities and intelligence "
        "can be developed through dedication and hard work. Embrace challenges, "
        "learn from mistakes, and grow continuously!"
    )

    st.header("🎯 Set Your Learning Goals")
    input_challenge = st.text_input("Write your learning challenge...")
    if input_challenge:
        st.success(f"Today you are going to learn **{input_challenge}**. Keep working hard!")
    else:
        st.info("Please set a goal to track your progress!")

    st.header("💡 Reflection on Challenges")
    input_reflection = st.text_area("Reflect on your learning...")
    if input_reflection:
        st.success(f"Reflection: {input_reflection}. Keep working hard!")

    st.subheader("📈 Track Your Progress")
    progress = st.slider("How much progress have you made?", 0, 100, 0)
    progress_bar = st.progress(0)
    for i in range(progress):
        time.sleep(0.02)
        progress_bar.progress(i + 1)
    st.write(f"Your progress: **{progress}%**")
    
    st.subheader("🌟 Motivational Quotes")
    quotes = [
        "Little things make big days. – Napoleon Hill", 
        "The only way to do great work is to love what you do. - Steve Jobs",
        "It always seems impossible until it's done. - Nelson Mandela",
        "Success is not the key to happiness. Happiness is the key to success. - Albert Schweitzer",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "Push yourself, because no one else is going to do it for you",
        "Success doesn't just find you. You have to go out and get it. – T. Harv Eker",
        "Dream bigger. Do bigger. – Robin Sharma"
    ] 
    st.write(f"✨ {quotes[progress % len(quotes)]}")
    st.balloons()

if __name__ == "__main__":
    main()
