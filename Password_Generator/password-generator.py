import streamlit as st
import re

# Page Config
st.set_page_config(page_title="Password Strength Checker", page_icon="🔐", layout="centered")

# Custom Styling 
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
        
        .stApp {
            background: linear-gradient(135deg, #1E1E2F, #2A2A5A);
            color: white;
            font-family: 'Poppins', sans-serif;
            padding: 40px;
            border-radius: 15px;
        }
        .big-title {
            text-align: center;
            font-size: 40px;
            font-weight: bold;
            color: #FFD700;
        }
        .sub-title {
            text-align: center;
            font-size: 18px;
            color: #E0E0E0;
        }
        .password-box {
            border: 2px solid #FFD700;
            padding: 10px;
            border-radius: 10px;
            background-color: rgba(255, 255, 255, 0.1);
        }
        .info-box {
            color: white !important;
        }
    </style>
    """, unsafe_allow_html=True
)

# Title & Description
st.markdown("<h1 class='big-title'>🔐 Password Strength Checker</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Check your password strength and get tips to improve it! 🔒</p>", unsafe_allow_html=True)

# Password Input
password = st.text_input("Enter your password", type="password", key="password_input")

# Initialize score & feedback list
score = 0
feedback = []

if password:
    # Check Length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least **8 characters** long!")

    # Check Upper & Lower Case
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain **both uppercase and lowercase letters**.")

    # Check for Numbers
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❌ Password should contain **at least one digit (0-9)**.")

    # Check for Special Characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain **at least one special character (!@#$%^&*)**.")

    # Display Strength Level
    st.markdown("### 🔍 Password Strength")
    strength_labels = {0: "Very Weak", 1: "Weak", 2: "Medium", 3: "Strong", 4: "Very Strong"}
    strength_colors = {0: "#FF4B4B", 1: "#FF914D", 2: "#FFC107", 3: "#4CAF50", 4: "#008000"}
    
    st.progress(score / 4)  # Progress bar
    st.markdown(f"<h3 style='color:{strength_colors[score]}; text-align:center;'>{strength_labels[score]}</h3>", unsafe_allow_html=True)
    
    # Show suggestions in an expandable dropdown
    if feedback:
        with st.expander("💡 Click here to see improvement suggestions"):
            for tip in feedback:
                st.write(tip)
else:
    st.markdown("<p class='info-box'>🔹 Please enter a password to check its strength.</p>", unsafe_allow_html=True)