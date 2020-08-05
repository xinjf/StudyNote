"""变量规则"""

from flask import Flask
app = Flask(__name__)


@app.route('/hello/<name>')
def hello_name(name):
    return 'hello {}'.format(name)


@app.route('/blog/<int:postID>')
def show_blog(postID):
    return 'blog {}'.format(postID)


@app.route('/rev/<float:revNo>')
def revision(revNo):
    return 'revision {}'.format(revNo)


if __name__ == '__main__':
    app.run(debug = True)


