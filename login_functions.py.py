import streamlit as st

# ----------------------------
# Login credentials
# ----------------------------
USER_CREDENTIALS = {
    "admin": "admin123",
    "user1": "password1"
}

def show_login():
    """Display login screen and update session state upon success."""
    st.title("🔐 Login")
    st.write("Enter your username and password to access the dashboard.")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        # Strip spaces and lowercase username for robustness
        username_clean = username.strip().lower()
        if username_clean in USER_CREDENTIALS and USER_CREDENTIALS[username_clean] == password:
            st.session_state.authenticated = True
            st.session_state.username = username_clean
            st.success(f"Welcome, {username_clean}!")
        else:
            st.error("Invalid username or password")

