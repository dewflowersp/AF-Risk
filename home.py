import streamlit as st
from app.auth import Auth
from app.home import Home

st.set_page_config(page_title='Home')

auth = Auth()

if auth.check_credentials(st):
    Home().main(st)
