import sqlite3
import bcrypt

DB_PATH = "database/resume_analyzer.db"


def hash_password(password):
    return bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    ).decode()


def verify_password(password, hashed):
    return bcrypt.checkpw(
        password.encode(),
        hashed.encode()
    )


def register_user(name, email, password):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    hashed_password = hash_password(password)

    try:
        cursor.execute("""
        INSERT INTO users
        (name,email,password)
        VALUES (?,?,?)
        """, (name, email, hashed_password))

        conn.commit()
        return True

    except sqlite3.IntegrityError:
        return False

    finally:
        conn.close()


def login_user(email, password):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE email=?",
        (email,)
    )

    user = cursor.fetchone()

    conn.close()

    if user:
        if verify_password(
            password,
            user[3]
        ):
            return user

    return None