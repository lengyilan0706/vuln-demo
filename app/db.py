"""Data access helpers."""


def get_user(conn, username):
    """Look up one user by name."""
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM users WHERE name = ?", (username,))
    return cur.fetchone()
