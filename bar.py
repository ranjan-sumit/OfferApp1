import streamlit as st
import random
import streamlit as st
import streamlit.components.v1 as components
import random

# Your existing code to define dummy_data, offers, etc.


# Dummy data for login (in real application, replace with database or secure storage check)
dummy_data = {
    "Share ID": ["iD9UGS29", "BMHFDdBs"],
    "Email ID": ["BBMKZ@example.com", "vWumN@example.com"],
    "Phone No": ["+19573297639", "+17825290856"]
}

# Define offers
offers = ["Offer 1: 10% Off", "Offer 2: Buy 1 Get 1", "Offer 3: Free Shipping"]

# Display the logo at the top of the app
st.image("logo_bar.png")  # Adjust the path

# Enhanced animated heading with continuous animation
heading_html = """
<head>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"/>
</head>
<div style="text-align: center;">
    <h1 class="animate__animated animate__pulse animate__infinite" style="color: #0047AB; font-size: 40px;">My Offer Genie !</h1>
</div>
"""

components.html(heading_html, height=150)
# Define your dropdown options
options = ["Share ID", "Email ID", "Phone No"]

# Create a dropdown menu with the options
selected_option = st.selectbox("Login using:", options)

# Initialize a variable to hold the input value
input_value = None

# Display an input field based on the selected option
if selected_option == "Share ID":
    input_value = st.text_input("Enter your Share ID:")
elif selected_option == "Email ID":
    input_value = st.text_input("Enter your Email ID:")
elif selected_option == "Phone No":
    input_value = st.text_input("Enter your Phone No:")

# Create a button to submit the information
if st.button('Login') and input_value:
    # Check if the input value is in the dummy data for the selected option
    if input_value in dummy_data[selected_option]:
        st.success(f'Login successful for {selected_option} with value: {input_value}')
        
        # Randomly select and display an offer
        selected_offer = random.choice(offers)
        offer_html = f"""
        <style>
        @keyframes fadeIn {{
            0% {{opacity: 0;}}
            100% {{opacity: 1;}}
        }}
        .offer-container {{
            background-color: #e6f4ea; /* Light green background */
            border-left: 5px solid #34c759; /* Darker green border on the left for emphasis */
            padding: 20px;
            margin: 20px 0;
            border-radius: 5px;
            animation: fadeIn 2s ease;
        }}
        </style>
        <div class="offer-container">
            <h2 style="color: #34c759;">Your special offer:</h2>
            <p style="font-size:24px; color: #34c759;"><b>{selected_offer}</b></p>
        </div>
        """
        st.markdown(offer_html, unsafe_allow_html=True)
        #st.markdown(offer_html, unsafe_allow_html=True)
    else:
        # Display guidance if login fails
        st.error('Login failed. Please check your credentials and try again. Or create an account')
        # Enhanced guidance message with HTML and CSS for a light green background
# Enhanced guidance message with HTML and CSS for a light pink background
        guidance_html = """
        <div style="background-color: #ffe4e1; padding: 20px; border-radius: 5px; border: 1px solid #ff6a67; margin-top: 20px;">
            <h2 style="color: #d32f2f;">Need help with your account?</h2>
            <p style="color: #d32f2f;">
                By downloading the <b>'SHARE Rewards'</b> app on Google Play or the Apple Store, you can start enjoying all your member benefits. Make sure to register, verify your email address, and login. If you already have an account with VOX Cinemas, you can log into the SHARE app with your VOX username and password.
            </p>
            <p style="color: #d32f2f;">
                For more information, visit our <a href="https://www.sharerewards.com/en/support#FAQ" target="_blank" style="color: #ff1744;">FAQs and Support</a> page.
            </p>
        </div>
        """
        selected_offer_new_cust="Get Flat 25% Off upto 50 AED on your first purchase. "
        offer_html_new = f"""
        <style>
        @keyframes fadeIn {{
            0% {{opacity: 0;}}
            100% {{opacity: 1;}}
        }}
        .offer-container {{
            background-color: #e6f4ea; /* Light green background */
            border-left: 5px solid #34c759; /* Darker green border on the left for emphasis */
            padding: 20px;
            margin: 20px 0;
            border-radius: 5px;
            animation: fadeIn 2s ease;
        }}
        </style>
        <div class="offer-container">
            <h2 style="color: #34c759;">Register Now and Redeem Special Offer for New Customer:</h2>
            <p style="font-size:24px; color: #34c759;"><b>{selected_offer_new_cust}</b></p>
        </div>
        """



        st.markdown(guidance_html, unsafe_allow_html=True)
        st.markdown(offer_html_new, unsafe_allow_html=True)
