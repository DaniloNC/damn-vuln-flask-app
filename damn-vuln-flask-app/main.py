from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/user/<username>")
def hello_user(username):
    # should flag the lack of escape, XSS vuln
    return f"Hello, {username}"

def main():
    # should flag the debug instance
    app.run(debug=True)

if __name__ == '__main__':
    main()