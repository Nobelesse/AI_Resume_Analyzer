import streamlit as st

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# Sidebar
st.sidebar.title("AI Resume Analyzer")
st.sidebar.markdown("---")

menu = st.sidebar.radio(
    "Navigation",
    [
        "Home"
    ]
)

# Home Page
st.title("📄 AI Resume Analyzer")

st.markdown("""
### Welcome to AI Resume Analyzer

An NLP-Based Resume Analysis and Job Recommendation System.

### Features

✅ Resume Upload (PDF)

✅ ATS Score Analysis

✅ Resume vs Job Matching

✅ Missing Skills Detection

✅ Job Recommendations

✅ Career Roadmap Generation

✅ Admin Dashboard

✅ Downloadable PDF Reports
""")

st.info("Phase 1 Setup Completed Successfully.")