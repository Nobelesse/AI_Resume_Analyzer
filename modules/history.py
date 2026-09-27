import sqlite3
import pandas as pd


def get_all_uploads():

    conn = sqlite3.connect(
        "database/resume_analyzer.db"
    )

    query = """
    SELECT
        users.name,
        users.email,
        resumes.resume_name,
        resumes.upload_date

    FROM resumes

    INNER JOIN users
    ON users.id = resumes.user_id

    ORDER BY resumes.id DESC
    """

    df = pd.read_sql_query(
        query,
        conn
    )

    conn.close()

    return df


def get_total_users():

    conn = sqlite3.connect(
        "database/resume_analyzer.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM users"
    )

    count = cursor.fetchone()[0]

    conn.close()

    return count


def get_total_resumes():

    conn = sqlite3.connect(
        "database/resume_analyzer.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM resumes"
    )

    count = cursor.fetchone()[0]

    conn.close()

    return count