from flask import Flask, render_template, send_from_directory, url_for
import os
app = Flask(__name__)
print(__name__)


@app.route("/<username>/<int:post_id>")
def hello_world(username=None, post_id=None):
    return render_template('index.html', name=username, post_id=post_id)

@app.route("/about.html")
def about():
    return render_template('about.html')

@app.route("/blog")
def blog():
    return 'these are my blogs'

@app.route("/blog/2020/dogs")
def blog2():
    return 'this is not my dog'

# @app.route("/favicon.ico")
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, 'static'),
#                                'static/pic.ico')