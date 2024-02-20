import streamlit as st
from app.auth import Auth
from app.list import DataList

# Set page configuration
st.set_page_config(page_title='Patient Data')

# Initialize authentication
auth = Auth()


if auth.check_credentials(st):
    DataList().show_data(st)