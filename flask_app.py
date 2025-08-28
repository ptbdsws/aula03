from flask import Flask, request, url_for, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route("/")
def main():
    return render_template('index.html', current_time=datetime.timezone.utc.now())

@app.route("/user/<user_name>")
def user(user_name):
    return render_template('user.html', user_name=user_name)

@app.errorhandler(404)
def not_found(e):
    return render_template('not_found.html'), 404

if __name__ == "__main__":
    app.run(debug=True)