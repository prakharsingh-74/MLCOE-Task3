from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/loginPage")
def renderLogin():
    return render_template("form.html")

@app.route("/formlogin", methods=['POST'])
def login():
    userName = request.form["userName"]
    password = request.form["password"]
    if userName == 'prakhar' and password == '123':
        return "<p>Successful Login</p>"
    else:
        return "Invalid User Name or Password"

if __name__ == "__main__":
    app.run(debug=True)
