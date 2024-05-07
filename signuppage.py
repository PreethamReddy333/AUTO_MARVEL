import streamlit as st


LoginData = {"Preetham9070":"123456789Reddy", "1":"1"} 
Dictnames = {"Preetham9070":"Preetham", "1":"1"}

st.title("Sign up")
a = st.text_input("name", key = 3)
b = st.text_input("Enter Username👇", key=332)
c = st.text_input("Enter password👇", key=423)

if st.button("sign up"):
    Dictnames[b] = a
    LoginData[b] = c
    st.page_link('AUTO_MARVEL/loginpage.py')

