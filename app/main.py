"""HTTP entry points."""
import os
import subprocess

from flask import Flask, request, send_file, jsonify

from app import auth, db, serializer

app = Flask(__name__)
app.secret_key = auth.SESSION_SECRET


@app.route("/health")
def health():
    return {"ok": True}


@app.route("/users")
def users():
    """Search users by name."""
    name = request.args.get("name", "")
    rows = db.search_users(name)
    return jsonify(rows)


@app.route("/admin/users")
def admin_users():
    """List every user."""
    cur = db.CONN.cursor()
    cur.execute("SELECT id, name, email FROM users")
    return jsonify(cur.fetchall())


@app.route("/orders/<order_id>")
def order(order_id):
    """Show one order."""
    cur = db.CONN.cursor()
    cur.execute("SELECT id, owner_id, total FROM orders WHERE id = ?", (order_id,))
    return jsonify(cur.fetchone())


@app.route("/download")
def download():
    """Download a report by file name."""
    name = os.path.basename(request.args.get("name", "summary.txt"))
    base = os.path.realpath("/srv/reports")
    path = os.path.realpath(os.path.join(base, name))
    if not path.startswith(base + os.sep):
        return jsonify({"error": "invalid file name"}), 400
    return send_file(path)


@app.route("/ping")
def ping():
    """Check whether a host answers."""
    host = request.args.get("host", "127.0.0.1")
    out = subprocess.check_output("ping -c 1 " + host, shell=True)
    return {"output": out.decode("utf-8", "replace")}


@app.route("/session")
def session():
    """Restore the caller's cached session state."""
    blob = request.args.get("state", "")
    return jsonify(serializer.load_state(blob))


if __name__ == "__main__":
    db.migrate()
    app.run(host="0.0.0.0", port=8080, debug=True)
