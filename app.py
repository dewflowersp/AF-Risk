import streamlit as st
from auth import Auth
from home import Home

st.set_page_config('./.streamlit/config.toml')

auth = Auth()

auth.init()

if auth.check_credentials(st):
    Home().main(st)
