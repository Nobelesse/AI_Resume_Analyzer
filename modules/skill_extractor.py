COMMON_SKILLS = [

    "python",
    "java",
    "c++",
    "c",
    "sql",
    "mysql",
    "mongodb",
    "html",
    "css",
    "javascript",
    "react",
    "nodejs",
    "streamlit",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "nlp",
    "pandas",
    "numpy",
    "scikit-learn",
    "tensorflow",
    "keras",
    "git",
    "github",
    "aws",
    "docker",
    "power bi",
    "excel"
]


def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in COMMON_SKILLS:

        if skill in text:
            found_skills.append(skill)

    return sorted(list(set(found_skills)))