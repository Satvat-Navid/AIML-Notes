from flask import Flask, render_template, request
'''
It creates an instance of the Flask class,
which will be your WSGI (Web Server Gateway Interface) application.
'''
# WSGI Application
app = Flask(__name__)

@app.route("/") # This is route for the app "flast()" we created.
def welcome(): # This is the funtion in this route to add funtioning.
    return 'Hello everyone welcome to my website.'

@app.route("/about")
def about():
    # we can return html syntax in the funtion when the route "/about" is accessed
    return """<html>
                <body>
                <H1>This is my First webpage Hello World</H1>
                <br>
                <a href = "/index"> Index Page </a>
                </body>
                </html>"""

@app.route("/index")
def index():
    # This is the use of jinja2 template system , we can return html file in that.
    return render_template('index.html')

# This is the GET and POST methods used when we interact with webpage.
# GET is set by default.
@app.route("/form", methods=['GET', 'POST'])
def form():
    if request.method == 'POST':  # If we post anything on the page the POST method is executed.
        name = request.form['name']
        age = request.form['age']
        return f"Hello {name} your age is {age}."
    return render_template('form.html')

if __name__=="__main__":
    app.run(debug=True)
