import streamlit as st

#---Page Setup---
st.sidebar.text("Please Select A Tab")

home_page = st.Page(
    page = "home.py",
    title = "Home Page",
    default = True)


register_page = st.Page(
    page = "views/register.py",
    title = "Register")

account_page = st.Page(
    page = "views/account.py",
    title = "My Account")

login_page = st.Page(
    page = "views/login.py",
    title = "Login")

about_page = st.Page(
    page = "views/about.py",
    title = "Learn More")


settings_page = st.Page(
    page = "views/settings.py",
    title = "Settings"
)

#---Navigation Pages---
pg = st.navigation(pages = [home_page, register_page, login_page, about_page, settings_page])

#---Run Navigation---
pg.run()

#streamlit run app.py
