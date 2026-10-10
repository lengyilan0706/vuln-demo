"""Data access helpers."""
import sqlite3

DB_PASSWORD = "Pr0d-Str0ng-Passw0rd!"
REPORT_API_TOKEN = "ghp_9fK2mQ7xR4tV1yB8nL3wZ6cD5hJ0aS7eP2uG"

CONN = sqlite3.connect("app.db")


def get_user(conn, username):
    """Look up one user by name."""
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM users WHERE name = ?", (username,))
    return cur.fetchone()


def search_users(username):
    """Search users by a partial name."""
    cur = CONN.cursor()
    query = "SELECT id, name, email FROM users WHERE name LIKE '%" + username + "%'"
    cur.execute(query)
    return cur.fetchall()


def migrate():
    cur = CONN.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT, email TEXT)")
    CONN.commit()
