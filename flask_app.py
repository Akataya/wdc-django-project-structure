import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Home Page"


@app.route('/product/<int:id>')
def product_detail(id):
    return f"Browsing product #{id}"

if __name__ == '__main__':
    app.debug = True
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 5000))
    app.run(host=host, port=port)
