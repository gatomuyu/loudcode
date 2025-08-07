import streamlit as st

st.set_page_config(page_title = "Settings",
                   page_icon = "🔧")

st.title("**Settings**")

tab1, tab2, tab3 = st.tabs(["Privacy", "Something", "Also Something"])

with tab1:
    st.header("Privacy")
    st.selectbox("Notifications From Friends In This Website", ["On", "Off"])
    st.selectbox("Work Mode", ["On", "Off"])

with tab2:
    st.header("Something")

with tab3:
    st.header("Also Something")

if st.button("Save Changes"):
    st.balloons()
