import sqlite3
import pandas as pd


def get_user_resumes(user_id):

    conn = sqlite3.connect(
        "database/resume_analyzer.db"
    )

    query = """
    SELECT
    resume_name,
    upload_date
    FROM resumes
    WHERE user_id=?
    """

    df = pd.read_sql_query(
        query,
        conn,
        params=(user_id,)
    )

    conn.close()

    return df