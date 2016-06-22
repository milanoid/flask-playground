from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello')
def hello_world():
    return 'Hello, World!'


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'The about page'


@app.route('/login', methods=['GET', 'POST'])
# if GET present HEAD and OPTIONS added automatically
def login():
    if request.method == 'POST':
        return 'Do the login'
    else:
        return 'Show login form'


@app.route('/urlbuilding')
def urlbuilding():
    with app.test_request_context():
        return url_for('show_user_profile', username='John Doe')


@app.route('/getstaticurl')
def get_static_url():
    return url_for('static', filename='style.css')
