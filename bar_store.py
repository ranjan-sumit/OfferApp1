# import streamlit as st
# import random
# import streamlit as st
# import streamlit.components.v1 as components
# import random
# import database

# import streamlit as st
# from streamlit_lottie import st_lottie

# st.image("final_img.png")

# col1, col2, col3 = st.columns(3)


# # Load and display the second Lottie animation in the second column
# with col2:
#     st_lottie("https://lottie.host/293db166-32fb-4ff9-b11d-489df8ca1c04/zZAqx4ZrQN.json",
#              quality="low",
#              height=200,
#              width =200)

# # with col3:
# #     st_lottie("https://lottie.host/35735e54-586d-4c23-93b8-a8f12da3fb49/Jkia5zaVCY.json",
# #              quality="low",
# #              height=200,
# #              width =200)


# # Enhanced animated heading with continuous animation
# heading_html = """
# <head>
# <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"/>
# </head>
# <div style="text-align: center;">
#     <h1 class="animate__animated animate__pulse animate__infinite" style="color: #0047AB; font-size: 40px;">My Offer Genie !</h1>
# </div>
# """


# # Enhanced animated heading with continuous animation
# heading_html = """
# <head>
# <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"/>
# </head>
# <div style="text-align: center;">
#     <h1 class="animate__animated animate__pulse animate__infinite" style="color: #ab0047; font-size: 40px;">Claim you Offer Today !</h1>
# </div>
# """

# components.html(heading_html, height=150)
# # Define your dropdown options
# options = ["Phone No","Share ID", "Email ID"]

# # Create a dropdown menu with the options
# selected_option = st.selectbox("Login using:", options)

# # Initialize a variable to hold the input value
# input_value_shareid = None
# input_value_phoneno = None
# input_value_emailid = None
# login_flag=False
# error_flag=True

# # Display an input field based on the selected option
# if selected_option == "Share ID":
#     input_value_shareid = st.text_input("Enter your 16 digit Share ID:")
#     if len(input_value_shareid) == 16 and input_value_shareid.isdigit():
#         pass
#     else:
#         st.error("Please enter a valid 16 digit Share ID.")
#         error_flag=False
# elif selected_option == "Email ID":
#     input_value_emailid = st.text_input("Enter your Email ID:")
# elif selected_option == "Phone No":
#     input_value_phoneno = st.text_input("Enter your 9 digit Phone No:")
#     if len(input_value_phoneno) == 9 and input_value_phoneno.isdigit():
#         pass
#     else:
#         st.error("Please enter a valid 9 digit phone number.")
#         error_flag=False

# # Create a button to submit the information
# if st.button('Login') and (input_value_shareid or input_value_emailid or input_value_phoneno) and error_flag:
    
#     with st.status("Your offer is being prepared. Kindly hold on !", expanded=True) as status:

#         if input_value_shareid:
#             offer=database.get_offer_shareid(input_value_shareid)
#         if input_value_emailid:
#             offer=database.get_offer_emailid(input_value_emailid)
#         if input_value_phoneno:
#             offer=database.get_offer_phoneno(input_value_phoneno)
    
        
#         if not offer.empty:
#             login_flag = True
    
#         if login_flag:
#             st.success(f'Login successful !!!')
            
#             # Randomly select and display an offer
#             selected_offer = offer['OFFER_4'].iloc[0]
#             offer_html = f"""
#             <style>
#             @keyframes fadeIn {{
#                 0% {{opacity: 0;}}
#                 100% {{opacity: 1;}}
#             }}
#             .offer-container {{
#                 background-color: #e6f4ea; /* Light green background */
#                 border-left: 5px solid #34c759; /* Darker green border on the left for emphasis */
#                 padding: 20px;
#                 margin: 20px 0;
#                 border-radius: 5px;
#                 animation: fadeIn 2s ease;
#             }}
#             </style>
#             <div class="offer-container">
#                 <h2 style="color: #34c759;">Redeem Your special offer:</h2>
#                 <p style="font-size:24px; color: #34c759;"><b>{selected_offer}</b></p>
#             </div>
#             """
#             st.markdown(offer_html, unsafe_allow_html=True)
#             st.image("dummy_barcode.png")
#             #st.markdown(offer_html, unsafe_allow_html=True)
#         else:
#             # Display guidance if login fails
#             st.error('Login failed. Please check your credentials and try again. Or create an account')
#             # Enhanced guidance message with HTML and CSS for a light green background
#     # Enhanced guidance message with HTML and CSS for a light pink background
#             guidance_html = """
#             <div style="background-color: #ffe4e1; padding: 20px; border-radius: 5px; border: 1px solid #ff6a67; margin-top: 20px;">
#                 <h2 style="color: #d32f2f;">Need help with your account?</h2>
#                 <p style="color: #d32f2f;">
#                     By downloading the <b>'SHARE Rewards'</b> app on Google Play or the Apple Store, you can start enjoying all your member benefits. Make sure to register, verify your email address, and login. If you already have an account with Share App, you can log into the SHARE app with your username and password.
#                 </p>
#                 <p style="color: #d32f2f;">
#                     For more information, visit our <a href="https://www.sharerewards.com/en/support#FAQ" target="_blank" style="color: #ff1744;">FAQs and Support</a> page.
#                 </p>
#             </div>
#             """

#             selected_offer_new_cust="Get Flat 25% Off upto 50 AED on your first purchase. "
#             offer_html_new = f"""
#         <style>
#         @keyframes fadeIn {{
#             0% {{opacity: 0;}}
#             100% {{opacity: 1;}}10
#         }}
#         .offer-container {{
#             background-color: #e6f4ea; /* Light green background */
#             border-left: 5px solid #34c759; /* Darker green border on the left for emphasis */
#             padding: 20px;
#             margin: 20px 0;
#             border-radius: 5px;
#             animation: fadeIn 2s ease;
#         }}
#         </style>
#         <div class="offer-container">
#             <h2 style="color: #34c759;">Register Now and Redeem Special Offer for New Customer:</h2>
#             <p style="font-size:24px; color: #34c759;"><b>{selected_offer_new_cust}</b></p>
#         </div>
#         """



#             st.markdown(guidance_html, unsafe_allow_html=True)
#             st.markdown(offer_html_new, unsafe_allow_html=True)
#             st.image("dummy_barcode.png")


import streamlit as st
import random
import streamlit.components.v1 as components
from streamlit_lottie import st_lottie
#import database

st.image("final_img.png")

# col1, col2, col3 = st.columns(3)

# # Load and display the second Lottie animation in the second column
# with col2:
#     st_lottie("https://lottie.host/293db166-32fb-4ff9-b11d-489df8ca1c04/zZAqx4ZrQN.json",
#              quality="low",
#              height=200,
#              width=200)

# Enhanced animated heading with continuous animation
heading_html = """
<head>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"/>
</head>
<div style="text-align: center;">
    <h1 class="animate__animated animate__pulse animate__infinite" style="color: #ab0047; font-size: 40px;">Claim Your Offer Today!</h1>
</div>
"""
components.html(heading_html, height=150)

# Define your dropdown options
options = ["Phone No", "Share ID", "Email ID"]

# Create a dropdown menu with the options
selected_option = st.selectbox("Login using:", options)

# Initialize a variable to hold the input value
input_value_shareid = None
input_value_phoneno = None
input_value_emailid = None
login_flag = False
error_flag = True

# Display an input field based on the selected option
if selected_option == "Share ID":
    input_value_shareid = st.text_input("Enter your 16 digit Share ID:")
    if len(input_value_shareid) == 16 and input_value_shareid.isdigit():
        pass
    else:
        st.error("Please enter a valid 16 digit Share ID.")
        error_flag = False
elif selected_option == "Email ID":
    input_value_emailid = st.text_input("Enter your Email ID:")
elif selected_option == "Phone No":
    input_value_phoneno = st.text_input("Enter your 9 digit Phone No:")
    if len(input_value_phoneno) == 9 and input_value_phoneno.isdigit():
        pass
    else:
        st.error("Please enter a valid 9 digit phone number.")
        error_flag = False

# Create a button to submit the information
if st.button('Login') and (input_value_shareid or input_value_emailid or input_value_phoneno) and error_flag:
    with st.spinner("Your offer is being prepared. Kindly hold on!"):
        offer = None
        if input_value_shareid:
            offer = "5% cashback on shop of 200 AED Instore Shopping + Free Falafel and Tea"
        elif input_value_emailid:
            offer = "5% cashback on shop of 200 AED Instore Shopping + Free Falafel and Tea"
        elif input_value_phoneno:
            if input_value_phoneno == "819719934":
                login_flag = True
                selected_offer = "5% cashback on shop of 200 AED Instore Shopping + Free Falafel and Tea"
            else:
                login_flag = False

        if offer and not offer.empty:
            login_flag = True

        if login_flag:
            st.success('Login successful!!!')
            if input_value_phoneno == "819719934":
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
                    <h2 style="color: #34c759;">Redeem Your special offer:</h2>
                    <p style="font-size:24px; color: #34c759;"><b>{selected_offer}</b></p>
                </div>
                """
            else:
                selected_offer = offer['OFFER_4'].iloc[0]
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
                    <h2 style="color: #34c759;">Redeem Your special offer:</h2>
                    <p style="font-size:24px; color: #34c759;"><b>{selected_offer}</b></p>
                </div>
                """
            st.markdown(offer_html, unsafe_allow_html=True)
            st.image("dummy_barcode.png")
        else:
            st.error('Login failed. Please check your credentials and try again. Or create an account')
            guidance_html = """
            <div style="background-color: #ffe4e1; padding: 20px; border-radius: 5px; border: 1px solid #ff6a67; margin-top: 20px;">
                <h2 style="color: #d32f2f;">Need help with your account?</h2>
                <p style="color: #d32f2f;">
                    By downloading the <b>'SHARE Rewards'</b> app on Google Play or the Apple Store, you can start enjoying all your member benefits. Make sure to register, verify your email address, and login. If you already have an account with Share App, you can log into the SHARE app with your username and password.
                </p>
                <p style="color: #d32f2f;">
                    For more information, visit our <a href="https://www.sharerewards.com/en/support#FAQ" target="_blank" style="color: #ff1744;">FAQs and Support</a> page.
                </p>
            </div>
            """

            selected_offer_new_cust = "Get Flat 5% cashback on spend up to 150 AED on your first purchase +  Free Falafel and Tea "
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
            st.image("dummy_barcode.png")
