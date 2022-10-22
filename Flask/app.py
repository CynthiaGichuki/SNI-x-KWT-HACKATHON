from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
	return render_template("index.html")

@app.route("/addlion")
def add_lion():
	return render_template("add_lion.html")

if __name__ == '__main__':
	app.run(debug=True)