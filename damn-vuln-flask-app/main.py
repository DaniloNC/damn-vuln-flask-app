from flask import Flask, escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/user/<username>")
def hello_user(username):
    return f"Hello, {escape(username)}"

def main():
    app.run()

if __name__ == '__main__':
    main()