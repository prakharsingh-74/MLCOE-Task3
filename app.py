from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def renderLogin():
    return render_template("form.html")

@app.route("/formlogin", methods=['POST'])
def login():
    userName = request.form["userName"]
    password = request.form["password"]
    if userName == 'prakhar' and password == '123':
        return "<p>Authentication successfull redirecting towards Face recognition</p>"
    else:
        return "Invalid User Name or Password"

@app.route("/final")
def renderfinal():
    return render_template("final.html")

if __name__ == "__main__":
    app.run(debug=True)
