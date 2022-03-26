from flask import Flask, render_template, request
import requests
from post import Post
from email_sender import EmailSender

app = Flask(__name__)

posts = requests.get('https://api.npoint.io/c790b4d5cab58020d391').json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

@app.route('/')
def get_homepage():
    return render_template("index.html", all_posts=post_objects)


@app.route('/post/<int:post_index>')
def get_post(post_index):
    requested_post = None
    for article in post_objects:
        if article.id == post_index:
            requested_post = article

    return render_template("post.html", post=requested_post)


@app.route('/about')
def get_about():
    return render_template("about.html")


@app.route('/contact', methods=["GET", "POST"])
def get_contact():

    # catch GET request
    if request.method == "GET":
        header = "Contact Me"
        return render_template("contact.html", header=header)

    # catch information from POST
    elif request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        # email message from POST
        es = EmailSender
        email_message = f"{message}\n\nFrom {name}\n{email}\n{phone}"
        es(email_message)
        header = "Message Successfully Sent"
        return render_template("contact.html", header=header)
    else:
        print("Error, try again")


if __name__ == "__main__":
    app.run(debug=True)
