import streamlit as st

st.title('Welcome to :blue[_AutoMarvel_]')
         
st.header("login or signup", divider="rainbow")

if st.button('login'):
    st.page_link('AUTO_MARVEL/loginpage.py')
if st.button('sign up'):
    st.page_link('AUTO_MARVEL/signuppage.py')




