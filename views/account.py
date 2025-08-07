import streamlit as st
from views.register import username, gmail

st.set_page_config(page_title = "My Account",
                   page_icon = "👁️‍🗨️")

logged_in = False

st.header("**My Account**")
if not logged_in:
    st.write("**Not Logged In, Sorry**")
else:
    st.write(f"**Welcome {username}, We Have Sent A Email To {gmail}**")
