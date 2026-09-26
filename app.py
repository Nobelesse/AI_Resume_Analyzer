import streamlit as st

from database.db import initialize_database
from modules.auth import register_user, login_user

# Initialize DB
initialize_database()

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# Session
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user_name" not in st.session_state:
    st.session_state.user_name = ""


st.sidebar.title("📄 AI Resume Analyzer")

page = st.sidebar.selectbox(
    "Menu",
    [
        "Home",
        "Register",
        "Login"
    ]
)

# Home
if page == "Home":

    st.title("📄 AI Resume Analyzer")

    st.info(
        "NLP Based Resume Analysis & Job Recommendation System"
    )

# Register
elif page == "Register":

    st.header("Create Account")

    name = st.text_input("Full Name")
    email = st.text_input("Email")
    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Register"):

        if register_user(
                name,
                email,
                password):

            st.success(
                "Registration Successful"
            )

        else:
            st.error(
                "Email already exists"
            )

# Login
elif page == "Login":

    st.header("Login")

    email = st.text_input("Email")
    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        user = login_user(
            email,
            password
        )

        if user:

            st.session_state.logged_in = True
            st.session_state.user_name = user[1]

            st.success(
                f"Welcome {user[1]}"
            )

        else:

            st.error(
                "Invalid Credentials"
            )

    if st.session_state.logged_in:

        st.success(
            f"Logged in as {st.session_state.user_name}"
        )