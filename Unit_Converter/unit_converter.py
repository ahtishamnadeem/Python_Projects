import streamlit as st 

# App Title and Description
st.title("🌎 Unit Converter App")
st.markdown("### Converts Length, Weight, & Time Instantly")
st.write("Welcome! Select a category, enter a value, and get the converted result in real-time.")

# Select Category
category = st.selectbox("Choose a category", ["Length", "Weight", "Time"])

# Define Unit Conversion Function
def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371

    elif category == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462

    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Hours to Minutes":
            return value * 60
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Days to Hours":
            return value * 24

# Select Conversion Type
if category == "Length":
    unit = st.selectbox("📏 Select Conversion", ["Kilometers to Miles", "Miles to Kilometers"])
elif category == "Weight":
    unit = st.selectbox("⚖️ Select Conversion", ["Pounds to Kilograms", "Kilograms to Pounds"])
elif category == "Time":
    unit = st.selectbox("⏱️ Select Conversion", ["Seconds to Minutes", "Minutes to Seconds", 
                                                  "Minutes to Hours", "Hours to Minutes", 
                                                  "Hours to Days", "Days to Hours"])

# Get User Input
value = st.number_input("Enter the value to convert", min_value=0.0, format="%.4f")

# Perform Conversion
if st.button("Convert"):
    result = convert_units(category, value, unit)
    if result is not None:
        st.success(f"✅ The result is: **{result:.4f}**")
    else:
        st.error("⚠️ Invalid conversion. Please check your input.")

# Footer with Creator Name
st.markdown("---")  # Adds a horizontal separator
st.markdown("### 👨‍💻 Design by **CodeWithAhtii**")