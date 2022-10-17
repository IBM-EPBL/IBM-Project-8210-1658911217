Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from flask import Flask,render_template
... 
... 
... app = Flask(__name__)
... 
... 
... @app.route('/')
... def home():
...     return render_template("sign_in.html")
... @app.route('/signup')
... def sign_up():
...     return render_template("sign_up.html")
... @app.route('/home')
... def ho():
...     return render_template("home.html")
... @app.route('/about')
... def about():
...     return render_template("about.html")
... 
... 
... if __name__ == '__main__':
