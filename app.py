import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Simple Calculator",
    page_icon="🧮",
    layout="centered"
)

st.title("🧮 Simple Calculator")
st.write("Perform basic mathematical operations.")

# Input numbers
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# Select operation
operation = st.selectbox(
    "Choose an operation",
    ["Addition", "Subtraction", "Multiplication", "Division"]
)

# Calculate button
if st.button("Calculate"):
    
    if operation == "Addition":
        result = num1 + num2

    elif operation == "Subtraction":
        result = num1 - num2

    elif operation == "Multiplication":
        result = num1 * num2

    elif operation == "Division":
        if num2 == 0:
            st.error("❌ Cannot divide by zero.")
        else:
            result = num1 / num2

    # Display result
    if not (operation == "Division" and num2 == 0):
        st.success(f"Result: **{result}**")
