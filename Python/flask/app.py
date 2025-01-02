from flask import Flask, render_template, request, redirect, url_for
'''
It creates an instance of the Flask class,
which will be your WSGI (Web Server Gateway Interface) application.
'''
# WSGI Application
# {{}} is used to print the variable in the html file.
# {%..%} is used to write the python code in the html file. Like for loop, if else etc.
# {#..#} is used to write the comment in the html file.
# all these are the jinja2 template system.
app = Flask(__name__)

@app.route("/") # This is route for the app "flast()" we created.
def welcome(): # This is the funtion in this route to add funtioning.
    return "Hello everyone welcome to my website." + "<a href = '/about'> About this website</a>" # Here we return a "str".

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

# Variable rule
@app.route('/success/<int:score>')
def success(score):
    if score >= 50:
        res = "Passed"
    else:
        res = "Failed"
    return render_template('result1.html', results=res)

# If variable is key value pair.
@app.route('/successform', methods=['GET', 'POST'])
def succform():
    if request.method=='POST':
        info = {
            'name': request.form['name'],
            'score': int(request.form['score'])
        }
        return render_template('result.html', results=info)
    return render_template('successform.html')

# Bulding a dinamic URL and redirecting to the page.
@app.route('/submit>', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        math = float(request.form['math'])
        pro = float(request.form['programming'])
        datas = float(request.form['data_science'])
        ml = float(request.form['ml'])
        avg = (math + pro + datas + ml) / 4
    return redirect(url_for(success, score=avg))

if __name__=="__main__":
    app.run(debug=True)
