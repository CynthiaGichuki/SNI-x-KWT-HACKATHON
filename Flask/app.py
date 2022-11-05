import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'image/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route("/")
@app.route("/index")
def index():
	return render_template("index.html")

@app.route("/addlion")
def add_lion():
	return render_template("add_lion.html")

@app.route("/findlion")
def find_lion():
	return render_template("find_lion.html")

@app.route('/results', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename)))
      return 'Image saved at ' + UPLOAD_FOLDER + 'folder'

if __name__ == '__main__':
	app.run(debug=True)