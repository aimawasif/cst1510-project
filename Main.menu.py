import streamlit as st
from login_functions import show_login
from dashboard_functions import show_dashboard  # Make sure this exists

st.set_page_config(page_title="Multi-Domain Intelligence App", page_icon="🔐", layout="wide")

# Initialize session
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# App flow
if not st.session_state.authenticated:
    show_login()
else:
    show_dashboard()


