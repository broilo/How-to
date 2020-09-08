from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def home():
    """
    Display Hello World in a local-host website
    """
    return 'Hello World'


@app.route('/about')
def about():
    return 'The About page'


@app.route('/blog')
def blog():
    return render_template('blog.html', author = "Matt")


@app.route('/blog/<string:blog_id>')
def blogpost(blog_id):
    return 'This is blog post number ' + blog_id


if __name__ == '__main__':
    app.run()
