from flask import Flask, redirect, url_for, request
app = Flask(__name__)


@app.route('/success/<name>')
def success(name):
    return 'welcome {}'.format(name)


@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        print("post")
        return redirect(url_for('success', name = user))
    else:
        user = request.args.get('nm')
        print("get")
        return redirect(url_for('success', name = user))


if __name__ == '__main__':
    app.run(debug = True)


