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
        return "redirecting towards face recognition"        
    else:
        return "Invalid User Name or Password"

@app.route("/face.py", methods)

@app.route("/final")
def renderfinal():
    return render_template("final.html")

if __name__ == "__main__":
    app.run(debug=True)
