import os
import sqlite3
from datetime import datetime

UPLOAD_FOLDER = "uploads"


def save_resume(user_id, uploaded_file):

    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = (
        f"{user_id}_{timestamp}_{uploaded_file.name}"
    )

    filepath = os.path.join(
        UPLOAD_FOLDER,
        filename
    )

    with open(filepath, "wb") as file:
        file.write(uploaded_file.getbuffer())

    conn = sqlite3.connect(
        "database/resume_analyzer.db"
    )

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO resumes
    (user_id,resume_name,file_path)
    VALUES (?,?,?)
    """, (
        user_id,
        filename,
        filepath
    ))

    conn.commit()
    conn.close()

    return filepath