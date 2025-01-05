from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<h1> Welcome to Flask <h2>"

@app.route("/welcome/<name>")
def welcome(name):
    return f"<h1>Hello {name} Welcome to our Flask page<h2>"

@app.route("/addition/<int:num>")
def addition(num):
    return f"<h1> The input number is {num} and its sum with 10 is {num + 10} Welcome to About page of Flask<h2>"

@app.route("/additiontwo/<int:num1>/<int:num2>")
def addition2(num1,num2):
    return f"<h1> The input number is {num1 , num2} and its sum  is {num1 + num2} Welcome to About page of Flask<h2>"

@app.route("/about")
def about():
    return "<h1> Welcome to About page of Flask<h2>"


if __name__ == "__main__":
    app.run(debug=True)