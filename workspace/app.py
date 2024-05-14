
from flask import Flask, render_template

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def index():
    title = 'Flask MVC'
    return render_template('index.html',title = title)

if __name__ == '__main__':
    app.run(port=8000, debug=True)