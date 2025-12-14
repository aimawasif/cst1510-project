import streamlit as st

# --------------------------------------------
# SESSION STATE
# --------------------------------------------
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# --------------------------------------------
# LOGIN FUNCTION
# --------------------------------------------
def login(username, password):
    # Replace with real authentication if needed
    if username == "admin" and password == "1234":
        st.session_state.authenticated = True
        st.success("Login successful! You can now access the dashboard.")
    else:
        st.error("Invalid username or password")

# --------------------------------------------
# LOGIN PAGE LAYOUT
# --------------------------------------------
st.set_page_config(page_title="Login - Multi-Domain Intelligence App", page_icon="🔐", layout="centered")

st.markdown(
    """
    <div style="text-align:center; margin-bottom:30px;">
        <h1>Welcome to the Multi-Domain Intelligence App</h1>
        <p>Secure Dashboard for Credential Hygiene Analysis</p>
    </div>
    """,
    unsafe_allow_html=True
)

username = st.text_input("Username", placeholder="Enter your username")
password = st.text_input("Password", type="password", placeholder="Enter your password")

if st.button("Login"):
    login(username, password)

