import requests
from flask import Flask, render_template

app = Flask(__name__)

response = requests.get("https://api.npoint.io/81bab482e62ce81face5")
response.raise_for_status()
all_post = response.json()


@app.route("/")
def home():
    return render_template("index.html", ALL_POST=all_post)


@app.route("/index.html")
def index():
    return render_template("index.html", ALL_POST=all_post)


@app.route("/about.html")
def about():
    return render_template("about.html")


@app.route("/contact.html")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:post_id>")
def post(post_id):
    return render_template("post.html", ID=post_id, ALL_POST=all_post)


if __name__ == "__main__":
    app.run(debug=True)
