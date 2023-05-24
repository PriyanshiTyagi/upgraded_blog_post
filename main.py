import os
import smtplib

import requests
from dotenv import load_dotenv
from flask import Flask, render_template, request

load_dotenv()

app = Flask(__name__)

response = requests.get("https://api.npoint.io/81bab482e62ce81face5")
response.raise_for_status()
all_post = response.json()


@app.route("/")
def home():
    return render_template("index.html", ALL_POST=all_post)


@app.route("/index")
def index():
    return render_template("index.html", ALL_POST=all_post)


@app.route("/about")
def about():
    return render_template("about.html")


# @app.route("/contact.html")
# def contact():
#     return render_template("contact.html")


@app.route("/post/<int:post_id>")
def post(post_id):
    return render_template("post.html", ID=post_id, ALL_POST=all_post)


my_email = os.getenv("MY_MAIL")
password = os.getenv("PASSWORD")


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "GET":
        return render_template("contact.html")

    else:
        message = f"Name: {request.form['name']}\n" \
                  f"Email: {request.form['email']}\n" \
                  f"Phone No: {request.form['phone']}\n" \
                  f"Message: {request.form['message']}\n"
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=os.getenv("TO_MAIL"),
                msg=f"Subject:Blog Post Form\n\n {message}".encode('utf-8'),

            )
        return render_template("contact.html", msg="Successfully sent the mail")


if __name__ == "__main__":
    app.run(debug=True)
