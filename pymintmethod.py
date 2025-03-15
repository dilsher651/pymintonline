import streamlit as st
from PIL import Image
import io

# Set page config and title
st.set_page_config(page_title="💸 Payment Options", page_icon="💳", layout="wide")

# Custom CSS styling
st.markdown("""
    <style>
    @keyframes float {
        0% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-15px) rotate(5deg); }
        100% { transform: translateY(0px) rotate(0deg); }
    }
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    @keyframes shine {
        0% { background-position: -100% 50%; }
        100% { background-position: 200% 50%; }
    }
    .floating-emoji {
        display: inline-block;
        font-size: 4em;
        animation: float 4s ease-in-out infinite;
        filter: drop-shadow(0 0 10px rgba(0,0,0,0.3));
    }
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
    .payment-card {
        background: rgba(255, 255, 255, 0.9);
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 8px 32px rgba(31, 38, 135, 0.2);
        backdrop-filter: blur(4px);
        border: 1px solid rgba(255, 255, 255, 0.18);
        margin-bottom: 20px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .payment-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(31, 38, 135, 0.3);
    }
    .payment-header {
        background: linear-gradient(90deg, #FC466B 0%, #3F5EFB 100%);
        color: white;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 15px;
        text-align: center;
        font-weight: bold;
    }
    .stTextInput>div>div>input {
        border-radius: 10px;
        border: 2px solid #e0e0e0;
        padding: 10px 15px;
        transition: all 0.3s ease;
    }
    .stTextInput>div>div>input:focus {
        border-color: #3F5EFB;
        box-shadow: 0 0 0 2px rgba(63, 94, 251, 0.2);
    }
    .success-msg {
        background: linear-gradient(90deg, #00C9FF 0%, #92FE9D 100%);
        color: white;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        animation: gradientBG 5s ease infinite;
        font-weight: bold;
    }
    .error-msg {
        background: linear-gradient(90deg, #FF416C 0%, #FF4B2B 100%);
        color: white;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        animation: gradientBG 5s ease infinite;
        font-weight: bold;
    }
    .summary-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 20px;
        border-radius: 15px;
        margin-top: 30px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    }
    .store-link {
        display: inline-block;
        margin-top: 15px;
        padding: 10px 20px;
        background: linear-gradient(90deg, #4776E6 0%, #8E54E9 100%);
        color: white;
        text-decoration: none;
        border-radius: 8px;
        font-weight: bold;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    .store-link:hover {
        transform: translateY(-3px);
        box-shadow: 0 7px 20px rgba(0,0,0,0.3);
    }
    .login-btn {
        background: linear-gradient(90deg, #36D1DC 0%, #5B86E5 100%);
        color: white;
        padding: 8px 15px;
        border-radius: 8px;
        font-weight: bold;
        border: none;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }
    .login-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 15px rgba(0,0,0,0.2);
    }
    .logout-btn {
        background: linear-gradient(90deg, #FF416C 0%, #FF4B2B 100%);
        color: white;
        padding: 8px 15px;
        border-radius: 8px;
        font-weight: bold;
        border: none;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }
    .logout-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 15px rgba(0,0,0,0.2);
    }
    .signup-btn {
        background: linear-gradient(90deg, #11998e 0%, #38ef7d 100%);
        color: white;
        padding: 8px 15px;
        border-radius: 8px;
        font-weight: bold;
        border: none;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }
    .signup-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 15px rgba(0,0,0,0.2);
    }
    .user-info {
        background: rgba(255, 255, 255, 0.8);
        padding: 10px 15px;
        border-radius: 8px;
        display: inline-block;
        margin-right: 10px;
    }
    .auth-card {
        background: white;
        border-radius: 15px;
        padding: 25px;
        box-shadow: 0 8px 32px rgba(31, 38, 135, 0.2);
        max-width: 400px;
        margin: 0 auto;
    }
    .auth-header {
        text-align: center;
        margin-bottom: 20px;
        color: #333;
    }
    .auth-switch {
        text-align: center;
        margin-top: 15px;
        color: #666;
    }
    .auth-switch a {
        color: #3F5EFB;
        text-decoration: none;
        font-weight: bold;
    }
    .auth-switch a:hover {
        text-decoration: underline;
    }
    </style>
""", unsafe_allow_html=True)

# Background with gradient
st.markdown("""
    <div style='
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        z-index: -1;
    '></div>
""", unsafe_allow_html=True)

# Initialize session state for user authentication
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = ""
if 'users' not in st.session_state:
    st.session_state.users = {}  # Dictionary to store user credentials
if 'auth_page' not in st.session_state:
    st.session_state.auth_page = "login"  # Can be "login" or "signup"

# Login/Logout section in the top right corner
login_col1, login_col2 = st.columns([6, 1])

with login_col2:
    if not st.session_state.logged_in:
        col_login, col_signup = st.columns(2)
        with col_login:
            if st.button("Login", key="login_button", help="Click to login"):
                st.session_state.auth_page = "login"
                st.session_state.show_auth = True
        with col_signup:
            if st.button("Sign Up", key="signup_button", help="Click to sign up"):
                st.session_state.auth_page = "signup"
                st.session_state.show_auth = True
    else:
        st.markdown(f"""
            <div style='text-align: right; margin-top: 10px;'>
                <span class='user-info'>👤 {st.session_state.username}</span>
                <button class='logout-btn' onclick="window.location.href='?logout=true'">Logout</button>
            </div>
        """, unsafe_allow_html=True)
        
        # Handle logout via query parameter
        if st.query_params.get('logout'):
            st.session_state.logged_in = False
            st.session_state.username = ""
            st.rerun()

# Authentication modal (Login or Signup)
if not st.session_state.logged_in and ('show_auth' in st.session_state and st.session_state.show_auth):
    with st.container():
        st.markdown("<div class='auth-card'>", unsafe_allow_html=True)
        
        if st.session_state.auth_page == "login":
            st.markdown("<h2 class='auth-header'>Login</h2>", unsafe_allow_html=True)
            
            with st.form("login_form"):
                username = st.text_input("Username")
                password = st.text_input("Password", type="password")
                
                submit = st.form_submit_button("Login")
                
                if submit:
                    if username in st.session_state.users and st.session_state.users[username] == password:
                        st.session_state.logged_in = True
                        st.session_state.username = username
                        st.session_state.show_auth = False
                        st.success(f"Welcome back, {username}!")
                        st.rerun()
                    else:
                        st.error("Invalid username or password")
            
            st.markdown("<div class='auth-switch'>Don't have an account? <a href='#' onclick='document.getElementById(\"signup_button\").click(); return false;'>Sign Up</a></div>", unsafe_allow_html=True)
        
        elif st.session_state.auth_page == "signup":
            st.markdown("<h2 class='auth-header'>Sign Up</h2>", unsafe_allow_html=True)
            
            with st.form("signup_form"):
                new_username = st.text_input("Choose a Username")
                new_password = st.text_input("Create a Password", type="password")
                confirm_password = st.text_input("Confirm Password", type="password")
                
                submit = st.form_submit_button("Sign Up")
                
                if submit:
                    if not new_username or not new_password:
                        st.error("Username and password are required")
                    elif new_username in st.session_state.users:
                        st.error("Username already exists. Please choose another one.")
                    elif new_password != confirm_password:
                        st.error("Passwords do not match")
                    else:
                        # Register the new user
                        st.session_state.users[new_username] = new_password
                        # Don't log in automatically after signup
                        st.session_state.auth_page = "login"
                        st.session_state.show_auth = True
                        st.success("Account created successfully! Please login with your credentials.")
                        st.rerun()
            
            st.markdown("<div class='auth-switch'>Already have an account? <a href='#' onclick='document.getElementById(\"login_button\").click(); return false;'>Login</a></div>", unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)

# Title of the app with animation
st.markdown("""
    <div style='text-align: center; padding: 30px 0;'>
        <span class='floating-emoji'>💸</span>
        <h1 style='color: #333; font-family: "Segoe UI", Arial, sans-serif; font-size: 3em; margin: 10px 0; text-shadow: 2px 2px 4px rgba(0,0,0,0.1);'>
            Payment Options
        </h1>
        <p style='color: #666; font-size: 1.2em;'>Choose your preferred payment method below</p>
    </div>
""", unsafe_allow_html=True)

# Online store links
store_links = {
    "EasyPaisa": "https://easypaisa.com.pk/",
    "JazzCash": "https://www.jazzcash.com.pk/",
    "Bank Card": "https://www.hbl.com/",
    "Foodpanda": "https://www.foodpanda.pk/"
}

# Payment options with icons
payment_options = {
    "EasyPaisa": "💚",
    "JazzCash": "❤️",
    "Bank Card": "💳",
    "Foodpanda": "🐼"
}

# Create columns for better layout
col1, col2, col3 = st.columns([1, 2, 1])

# Initialize session state for storing payment data
if 'payment_data' not in st.session_state:
    st.session_state.payment_data = {
        'method': '',
        'amount': 0.0,
        'details': {}
    }

with col2:
    # Check if user is logged in
    if not st.session_state.logged_in:
        st.warning("Please login or sign up to access payment options")
        
        # Add demo credentials for easy testing
        st.info("For testing, you can sign up with any username and password, or use these demo credentials:")
        st.code("Username: demo\nPassword: demo123")
        
        # Add demo user if not already added
        if 'demo' not in st.session_state.users:
            st.session_state.users['demo'] = 'demo123'
    else:
        # Logout button at the top of the payment section
        if st.button("Logout", key="logout_button_main"):
            st.session_state.logged_in = False
            st.session_state.username = ""
            st.rerun()
            
        # Dropdown for selecting payment option with custom styling
        st.markdown("<div style='margin-bottom: 30px;'></div>", unsafe_allow_html=True)
        selected_option = st.selectbox(
            "Select your payment method:",
            options=list(payment_options.keys()),
            format_func=lambda x: f"{payment_options[x]} {x}"
        )
        
        # Update payment method in session state
        st.session_state.payment_data['method'] = selected_option

        # Display selected payment option
        st.markdown(f"""
            <div style='text-align: center; margin: 20px 0;'>
                <h3 style='color: #333; font-family: "Segoe UI", Arial, sans-serif;'>
                    You have selected 
                    <span style='font-size: 1.5em; margin: 0 10px;'>{payment_options[selected_option]}</span>
                    <b style='background: linear-gradient(90deg, #3F5EFB 0%, #FC466B 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>
                        {selected_option}
                    </b> 
                    as your payment method.
                </h3>
                <a href="{store_links[selected_option]}" target="_blank" class="store-link">Visit {selected_option} Website</a>
            </div>
        """, unsafe_allow_html=True)

        # Input fields for payment details
        st.markdown("<div class='payment-card'>", unsafe_allow_html=True)
        st.markdown(f"<div class='payment-header'>{payment_options[selected_option]} {selected_option} Payment Details</div>", unsafe_allow_html=True)
        
        amount = st.number_input("Enter the amount:", min_value=0.0, format="%.2f")
        st.session_state.payment_data['amount'] = amount

        payment_success = False

        if selected_option == "EasyPaisa":
            easypaisa_number = st.text_input("Enter your EasyPaisa number:")
            easypaisa_password = st.text_input("Enter your EasyPaisa password:", type="password")
            # Demo password for testing
            correct_password = "easypaisa123"
            
            # Store details in session state
            st.session_state.payment_data['details'] = {
                'number': easypaisa_number,
                'password': '********'  # Don't store actual password
            }
            
            if st.button(f"Pay {amount} PKR with EasyPaisa"):
                if easypaisa_password == correct_password:
                    st.markdown(f"<div class='success-msg'>Payment of {amount} PKR made successfully using EasyPaisa number {easypaisa_number}.</div>", unsafe_allow_html=True)
                    payment_success = True
                else:
                    st.markdown("<div class='error-msg'>Incorrect password. Please try again.</div>", unsafe_allow_html=True)

        elif selected_option == "JazzCash":
            jazzcash_number = st.text_input("Enter your JazzCash number:")
            jazzcash_password = st.text_input("Enter your JazzCash password:", type="password")
            # Demo password for testing
            correct_password = "jazzcash123"
            
            # Store details in session state
            st.session_state.payment_data['details'] = {
                'number': jazzcash_number,
                'password': '********'  # Don't store actual password
            }
            
            if st.button(f"Pay {amount} PKR with JazzCash"):
                if jazzcash_password == correct_password:
                    st.markdown(f"<div class='success-msg'>Payment of {amount} PKR made successfully using JazzCash number {jazzcash_number}.</div>", unsafe_allow_html=True)
                    payment_success = True
                else:
                    st.markdown("<div class='error-msg'>Incorrect password. Please try again.</div>", unsafe_allow_html=True)

        elif selected_option == "Bank Card":
            col_a, col_b = st.columns(2)
            with col_a:
                card_number = st.text_input("Enter your card number:")
                card_expiry = st.text_input("Enter card expiry date (MM/YY):")
            with col_b:
                card_cvc = st.text_input("Enter card CVC:")
                card_password = st.text_input("Enter your card password:", type="password")
            
            # Store details in session state
            st.session_state.payment_data['details'] = {
                'card_number': card_number,
                'expiry': card_expiry,
                'cvc': '***',  # Don't store actual CVC
                'password': '********'  # Don't store actual password
            }
            
            # Demo password for testing
            correct_password = "card123"
            if st.button(f"Pay {amount} PKR with Bank Card"):
                if card_password == correct_password:
                    st.markdown(f"<div class='success-msg'>Payment of {amount} PKR made successfully using card number {card_number}.</div>", unsafe_allow_html=True)
                    payment_success = True
                else:
                    st.markdown("<div class='error-msg'>Incorrect password. Please try again.</div>", unsafe_allow_html=True)

        elif selected_option == "Foodpanda":
            foodpanda_id = st.text_input("Enter your Foodpanda ID:")
            foodpanda_password = st.text_input("Enter your Foodpanda password:", type="password")
            
            # Store details in session state
            st.session_state.payment_data['details'] = {
                'id': foodpanda_id,
                'password': '********'  # Don't store actual password
            }
            
            # Demo password for testing
            correct_password = "foodpanda123"
            if st.button(f"Pay {amount} PKR with Foodpanda"):
                if foodpanda_password == correct_password:
                    st.markdown(f"<div class='success-msg'>Payment of {amount} PKR made successfully using Foodpanda ID {foodpanda_id}.</div>", unsafe_allow_html=True)
                    payment_success = True
                else:
                    st.markdown("<div class='error-msg'>Incorrect password. Please try again.</div>", unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Display payment summary at the end
        if 'payment_data' in st.session_state and st.session_state.payment_data['amount'] > 0:
            st.markdown("<div class='summary-card'>", unsafe_allow_html=True)
            st.markdown("<h3 style='text-align: center; margin-bottom: 15px;'>Payment Summary</h3>", unsafe_allow_html=True)
            
            data = st.session_state.payment_data
            st.markdown(f"""
                <p><strong>Payment Method:</strong> {payment_options.get(data['method'], '')} {data['method']}</p>
                <p><strong>Amount:</strong> {data['amount']} PKR</p>
            """, unsafe_allow_html=True)
            
            # Display details based on payment method
            if data['method'] == 'EasyPaisa' and 'number' in data['details']:
                st.markdown(f"<p><strong>EasyPaisa Number:</strong> {data['details']['number']}</p>", unsafe_allow_html=True)
            elif data['method'] == 'JazzCash' and 'number' in data['details']:
                st.markdown(f"<p><strong>JazzCash Number:</strong> {data['details']['number']}</p>", unsafe_allow_html=True)
            elif data['method'] == 'Bank Card' and 'card_number' in data['details']:
                # Mask card number for security
                masked_number = "xxxx-xxxx-xxxx-" + data['details']['card_number'][-4:] if len(data['details']['card_number']) >= 4 else data['details']['card_number']
                st.markdown(f"""
                    <p><strong>Card Number:</strong> {masked_number}</p>
                    <p><strong>Expiry Date:</strong> {data['details'].get('expiry', '')}</p>
                """, unsafe_allow_html=True)
            elif data['method'] == 'Foodpanda' and 'id' in data['details']:
                st.markdown(f"<p><strong>Foodpanda ID:</strong> {data['details']['id']}</p>", unsafe_allow_html=True)
            
            if payment_success:
                st.markdown("<p style='color: #92FE9D; font-weight: bold;'>✅ Payment Successful</p>", unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)
