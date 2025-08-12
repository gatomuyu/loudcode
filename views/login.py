import streamlit as st
from PIL import Image

st.set_page_config(
    page_title = "Login",
    page_icon = "🧑")

st.title("**Login**")

username = st.text_input("**Enter Your Username**")
password = st.text_input("**Enter Your Password**")

#Functions
def login():
    taken_users = []
    taken_passwords = []

    taken_users.clear()
    taken_passwords.clear()

    with open("views/usernames", "r") as f:
        for line in f:
            taken_users.append(line.rstrip("\n"))

    with open("views/passwords", "r") as f:
        for line in f:
            taken_passwords.append(line.rstrip("\n"))

    try:
        decoded_user = taken_users.index(username)

    except ValueError:
        decoded_user = None

    try:
        decoded_password = taken_passwords.index(password)

    except ValueError:
        decoded_password = None

    if decoded_user or decoded_password is not None:
        if decoded_user == decoded_password:

            st.write("**Successfully Logged In!**")

            user_image = Image.open("images/User_image.jpg")
            new_img = user_image.resize((100, 100))

            st.sidebar.image(new_img)
            st.sidebar.text(username if not None else "'Not Registered'")


        else:
            st.write("**Username or Password Incorrect!**")

    else:
        st.write("**Username or Password Incorrect**")

if st.button("Login"):
    login()
