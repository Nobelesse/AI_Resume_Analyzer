import streamlit as st

from modules.history import (
    get_all_uploads,
    get_total_users,
    get_total_resumes
)


def show_admin_dashboard():

    st.title("🛡️ Admin Dashboard")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Total Users",
            get_total_users()
        )

    with col2:
        st.metric(
            "Total Resumes",
            get_total_resumes()
        )

    st.divider()

    st.subheader(
        "📋 Resume Upload History"
    )

    uploads = get_all_uploads()

    st.dataframe(
        uploads,
        use_container_width=True
    )