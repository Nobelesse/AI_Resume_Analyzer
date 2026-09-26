import streamlit as st

from database.db import initialize_database
from modules.auth import register_user, login_user
from modules.resume_upload import save_resume
from modules.history import get_user_resumes

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


st.sidebar.title("📄 AI Resume Analyzer")

page = st.sidebar.selectbox(
    "Menu",
    [
        "Home",
        "Register",
        "Login",
        "Upload Resume"
    ]
)

# HOME
if page == "Home":

    st.title("📄 AI Resume Analyzer")

    st.markdown("""
    ### NLP-Based Resume Analysis & Career Recommendation System

    Welcome to AI Resume Analyzer.

    Features:

    ✅ Resume Upload

    ✅ ATS Analysis

    ✅ Resume Matching

    ✅ Missing Skills Detection

    ✅ Job Recommendations

    ✅ Skill Gap Roadmap

    ✅ Admin Dashboard
    """)

# REGISTER
elif page == "Register":

    st.header("📝 Create Account")

    name = st.text_input("Full Name")

    email = st.text_input("Email")

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
                "Email already exists."
            )

# LOGIN
elif page == "Login":

    st.header("🔐 Login")

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
            st.session_state.user_id = user[0]
            st.session_state.user_name = user[1]

            st.success(
                f"Welcome {user[1]}"
            )

        else:
            st.error(
                "Invalid Email or Password"
            )

    if st.session_state.logged_in:

        st.success(
            f"Logged In As: {st.session_state.user_name}"
        )

# UPLOAD RESUME
elif page == "Upload Resume":

    st.header("📄 Upload Resume")

    if not st.session_state.logged_in:

        st.warning(
            "Please login first."
        )

    else:

        uploaded_file = st.file_uploader(
            "Upload Resume (PDF Only)",
            type=["pdf"]
        )

        if uploaded_file:

            max_size = 10 * 1024 * 1024

            if uploaded_file.size > max_size:

                st.error(
                    "File exceeds 10 MB limit."
                )

            else:

                st.success(
                    f"Selected File: {uploaded_file.name}"
                )

                if st.button(
                    "Upload Resume"
                ):

                    save_resume(
                        st.session_state.user_id,
                        uploaded_file
                    )

                    st.success(
                        "Resume uploaded successfully."
                    )

        st.divider()

        st.subheader("📜 Upload History")

        history = get_user_resumes(
            st.session_state.user_id
        )

        st.dataframe(
            history,
            use_container_width=True
        )