from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def Helloworld():
    return render_template('login.html')
    #return 'Hello, World!'

@app.route('/products')
def products():
    return 'this is products page'

if __name__=="__main__":
    app.run(debug=True)