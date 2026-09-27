import streamlit as st

from database.db import initialize_database

from modules.auth import (
    register_user,
    login_user
)

from modules.resume_upload import (
    save_resume
)

from modules.pdf_parser import (
    extract_text_from_pdf
)

from modules.resume_parser import (
    parse_resume
)

from admin.admin_dashboard import (
    show_admin_dashboard
)

initialize_database()

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# Session State

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user_name" not in st.session_state:
    st.session_state.user_name = ""

if "user_id" not in st.session_state:
    st.session_state.user_id = None

if "role" not in st.session_state:
    st.session_state.role = "guest"

# Sidebar

st.sidebar.title("📄 AI Resume Analyzer")

# ADMIN VIEW

if st.session_state.role == "admin":

    page = st.sidebar.selectbox(
        "Admin Menu",
        [
            "Dashboard",
            "Logout"
        ]
    )

# USER VIEW

elif st.session_state.logged_in:

    page = st.sidebar.selectbox(
        "User Menu",
        [
            "Home",
            "Upload Resume",
            "Logout"
        ]
    )

# GUEST VIEW

else:

    page = st.sidebar.selectbox(
        "Menu",
        [
            "Home",
            "Register",
            "Login",
            "Admin Login"
        ]
    )

# HOME

if page == "Home":

    st.title("📄 AI Resume Analyzer")

    st.info(
        "NLP Based Resume Analysis System"
    )

# REGISTER

elif page == "Register":

    st.title("Register")

    name = st.text_input(
        "Full Name"
    )

    email = st.text_input(
        "Email"
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Register"):

        success = register_user(
            name,
            email,
            password
        )

        if success:

            st.success(
                "Registration Successful"
            )

        else:

            st.error(
                "Email Already Exists"
            )

# USER LOGIN

elif page == "Login":

    st.title("User Login")

    email = st.text_input(
        "Email"
    )

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

            if user[4] == "user":

                st.session_state.logged_in = True
                st.session_state.user_id = user[0]
                st.session_state.user_name = user[1]
                st.session_state.role = "user"

                st.rerun()

            else:

                st.error(
                    "Use Admin Login"
                )

# ADMIN LOGIN

elif page == "Admin Login":

    st.title(
        "🛡️ Admin Login"
    )

    email = st.text_input(
        "Admin Email"
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button(
        "Login As Admin"
    ):

        user = login_user(
            email,
            password
        )

        if user:

            if user[4] == "admin":

                st.session_state.logged_in = True
                st.session_state.user_id = user[0]
                st.session_state.user_name = user[1]
                st.session_state.role = "admin"

                st.rerun()

            else:

                st.error(
                    "Not An Admin Account"
                )

# UPLOAD RESUME

elif page == "Upload Resume":

    st.title("📄 Upload Resume")

    uploaded_file = st.file_uploader(
        "Upload Resume",
        type=["pdf"]
    )

    if uploaded_file:

        max_size = 10 * 1024 * 1024

        if uploaded_file.size > max_size:

            st.error(
                "Maximum file size is 10 MB"
            )

        else:

            if st.button(
                "Upload Resume"
            ):

                filepath = save_resume(
                    st.session_state.user_id,
                    uploaded_file
                )

                st.success(
                    "Resume Uploaded Successfully"
                )

                text = extract_text_from_pdf(
                    filepath
                )

                parsed = parse_resume(
                    text
                )

                st.subheader(
                    "Resume Details"
                )

                st.write(
                    f"Name: {parsed['name']}"
                )

                st.write(
                    f"Email: {parsed['email']}"
                )

                st.write(
                    f"Phone: {parsed['phone']}"
                )

                st.write(
                    parsed["skills"]
                )

# DASHBOARD

elif page == "Dashboard":

    show_admin_dashboard()

# LOGOUT

elif page == "Logout":

    st.session_state.logged_in = False
    st.session_state.user_id = None
    st.session_state.user_name = ""
    st.session_state.role = "guest"

    st.rerun()