from flask import Flask, render_template, request

'''
It creates an instance of the Flask class,
which will be your WSGI (Web Server Gateway Interface) application.
'''
# WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome():
    return """<html><body>
                <H1>This is my First webpage Hello World</H1>
                <br>
                <a href = "/index"> Index Page </a>
                </body></html>"""

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/form", methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        return f"Hello {name} your age is {age}."
    return render_template('form.html')

if __name__=="__main__":
    app.run(debug=True)
