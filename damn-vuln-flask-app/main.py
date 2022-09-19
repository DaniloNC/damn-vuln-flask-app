from flask import Flask, escape
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/user/<username>")
def hello_user(username):
    return f"Hello, {escape(username)}"

@app.route("/info/<cmd>")
def cmd_run(cmd):
    parsed_cmd = validate_cmd(cmd)
    if parsed_cmd != "":
        os.system(parsed_cmd)
    return "Executed"

def validate_cmd(cmd):
    if cmd == "ipinfo":
        return cmd
    
    return ""

def main():
    app.run()

if __name__ == '__main__':
    main()