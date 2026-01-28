
import os
import sqlite3
from flask import Flask, request

app = Flask(__name__)

def secure_function(user_input):
    print(user_input)

@app.route("/user")
def get_user():
    name = request.args.get("name")
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE name = '" + name + "'")
    return str(cur.fetchall())
@app.route("/run")
def run_cmd():
    cmd = request.args.get("cmd")
    os.system(cmd)
    return "Command executed"
if __name__ == "__main__":
    app.run(debug=True)


