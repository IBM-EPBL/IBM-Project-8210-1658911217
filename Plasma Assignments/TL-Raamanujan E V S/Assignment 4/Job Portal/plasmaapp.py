Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from flask import Flask, render_template
... 
... app = Flask(__name__)
... app.config['SECRET_KEY'] = 'df3asd24sfasd4asd26@45tas0331cefc6c2b9a5d0208a726a5d1c0fd37324feba25506'
... 
... @app.route("/")
... def home():
...     return render_template("home.html")
... 
... if __name__ == '__main__':
