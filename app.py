import streamlit as st

def page_start():
    if st.session_state.x:
        with st.sidebar:
            st.header("Application menu")
            st.write("You are signed on")
        st.title("You are logged in")
        st.write("Logged in content")

if "x" not in st.session_state:
    st.session_state.x = False

st.set_page_config(
    page_title="Multi-Domain Intelligence App"
)

if st.session_state.x :
    with st.sidebar:
        st.header("Application menu")
        st.write("You are signed on")
else:
    st.session_state.x = True

with st.sidebar:
    st.header("Application options")
    name1 = st.text_input("username")
    passwd1 = st.text_input("password", type="password")

st.title("Hello")
st.write("This will be shown on the page")
name = st.text_input("Username")
passwd = st.text_input("Password", type="password")
if st.button("Login"):
    st.write("Login button clicked! username: "
                                        + name +
             "Password:  " + passwd)

with st.expander("see application details"):
    st.write("This is a test screen!")
    st.write("I created all of with myself with no help from AI or Friends")