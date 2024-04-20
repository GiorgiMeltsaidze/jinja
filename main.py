from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/user')
def user():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/oddeven/<name>')
def oddeven(name):
    return render_template("oddeven.html", my_name=name)

if __name__ == '__main__':
    app.run(debug=True)
