import streamlit as st

# Set page config and title
st.set_page_config(page_title="💸 Payment Options", page_icon="💳", layout="wide")

# Custom CSS styling
st.markdown("""
    <style>
    .stButton>button {
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4, #45B7D1, #FF6B6B);
        background-size: 300% 300%;
        animation: gradientBG 5s ease infinite;
        color: white;
        font-weight: bold;
        font-size: 1.2em;
        border-radius: 30px;
        padding: 1.2rem 3.5rem;
        border: none;
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
    .stButton>button:hover {
        transform: translateY(-7px) scale(1.05);
        box-shadow: 0 15px 25px rgba(0,0,0,0.3);
    }
    </style>
""", unsafe_allow_html=True)

# Title of the app
st.markdown("<h1 style='text-align: center; color: aqua; font-family: Arial, sans-serif;'>💸 Payment Options</h1>", unsafe_allow_html=True)

# Payment options
payment_options = ["EasyPaisa", "JazzCash", "Bank Card","union pay","food panda"]

# Dropdown for selecting payment option
selected_option = st.selectbox("Select your payment method:", payment_options)

# Display selected payment option
st.markdown(f"<div style='text-align: center;'><h3 style='color: #33FF57; font-family: Arial, sans-serif;'>You have selected <b style='color: #3357FF;'>{selected_option}</b> as your payment method.</h3></div>", unsafe_allow_html=True)

# Input fields for payment details
amount = st.number_input("Enter the amount:", min_value=0.0, format="%.2f")


if selected_option == "EasyPaisa":
    easypaisa_number = st.text_input("Enter your EasyPaisa number:")
    if st.button("Pay with EasyPaisa"):
        st.success(f"Payment of {amount} PKR made successfully using EasyPaisa number {easypaisa_number}.")

elif selected_option == "JazzCash":
    jazzcash_number = st.text_input("Enter your JazzCash number:")
    if st.button("Pay with JazzCash"):
        st.success(f"Payment of {amount} PKR made successfully using JazzCash number {jazzcash_number}.")

elif selected_option == "Bank Card":
    card_number = st.text_input("Enter your card number:")
    card_expiry = st.text_input("Enter card expiry date (MM/YY):")
    card_cvc = st.text_input("Enter card CVC:")
    if st.button("Pay with Bank Card"):
        st.success(f"Payment of {amount} PKR made successfully using card number {card_number}.")


elif selected_option == "union pay":
    jazzcash_number = st.text_input("Enter your union pay number:")
    if st.button("Pay with union pay"):
        st.success(f"Payment of {amount} PKR made successfully using union pay number {jazzcash_number}.")

# elif selected_option == "food panda":
#     card_number = st.text_input("Enter your card number:")
#     card_expiry = st.text_input("Enter card expiry date (MM/YY):")
#     card_cvc = st.text_input("Enter card CVC:")
#     if st.button("Pay with Bank Card"):
#         st.success(f"Payment of {amount} PKR made successfully using card number {card_number}.

selected_option = "food panda"
if selected_option == "food panda":
    card_number = st.text_input("Enter your card number:")
    card_expiry = st.text_input("Enter card expiry date (MM/YY):")
    card_cvc = st.text_input("Enter card CVC:")
    # Add Password Field
    password = st.text_input("Enter your password:", type="password")

    if st.button("Pay with Bank Card"):
        if password:  # Check if password is entered
            st.success(f"Payment of {amount} PKR made successfully using Food Panda")
        else:
            st.error("Please enter your password to proceed!")