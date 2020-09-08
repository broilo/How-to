from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect
from forms import SignUpForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'


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
    posts = [{'title': 'Technology in 2019', 'author': 'Mateus'},
             {'title': 'Expansion of oil in Russia', 'author': 'Matt'}]
    return render_template('blog.html', author="Matt", sunny=True, posts=posts)


@app.route('/blog/<string:blog_id>')
def blogpost(blog_id):
    return 'This is blog post number ' + blog_id


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.is_submitted():
        result = request.form()
        return render_template('user.html', result=result)
    return render_template('signup.html', form=form)


if __name__ == '__main__':
    app.run()
