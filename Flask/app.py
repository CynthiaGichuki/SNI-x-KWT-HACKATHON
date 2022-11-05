import os
from flask import Flask, render_template, request,  redirect, url_for
# from werkzeug import secure_filename



app = Flask(__name__)

# @app.route("/")
# @app.route("/index")
# def index():
# 	return render_template("index.html")


path = r"Flask\dataset"
assert os.path.isfile(path)
with open(path, "r") as f:
    pass


@app.route("/", methods=['GET','POST'])
def add_lion():
	if request.method == "POST":
		# lion_name = request.form['lion_name']
		# lion_pride = request.form['lion_pride']
		# dob = request.form['dob']
		imagefile = request.files['imagefile']		
		image_path = "/" + imagefile.filename
		imagefile.save(image_path)

		return "upload successful "+ imagefile 
		 
		# return "Your name is "+lion_name +"/n pride " + lion_pride + dob

	return render_template("add_lion.html")
	

		

	# # lion_name = request.files['name']
	# # lion_pride = request.files['lion_pride']
	# imagefile = request.files['imagefile']
	# image_path = "./images/" + imagefile.filename
	# imagefile.save(image_path)
	# return render_template("add_lion.html")

# @app.route("/findlion", methods=['GET'])
# def find_lion():
# 	return render_template("find_lion.html")

if __name__ == '__main__':
	app.run(debug=True)


