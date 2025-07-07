from flask import Flask
from flask import render_template
from flask import request, redirect, url_for

##app = Flask(__name__)
app = Flask(__name__, template_folder="template")

@app.route("/", methods=["GET"])
def index():
    return render_template("mretweb.html")

@app.route("/greet", methods=["POST"])
def greet():
    username = request.form.get("username")
    greeting = f"Hello, {username}"
    return redirect(url_for('done', username=username))

@app.route("/done")
def done():
    username = request.args.get("username", "Guest")
    return f"<h1>Hello again, {username} - this is the login page.</h1>"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)


