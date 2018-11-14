name = input()
//format string
print(f"Hello, {name}!")

//////////////////
ages = {"Alice": 22, "Bob": 27}
ages["Charlie"] = 30
ages["Alice] += 1

Print(ages)
///////////////////

def square(x):
  return x*x
  
def main():
  for i in range(10):
    print("{} squared is {}".format(i, square(i))}
    
if __name__ == "__main__":
  main()
  
////////////////////
class Point:
  def __init__(self, x, y):
    self.x=x
    self.y=y

p = Point(3,5)
print(p.x)
print(p.y)

////////////////////
<body>
  {% if new_year %}
    <h1>Yes! Happy New Year!</h1>
  {% else %}
    <h1>NO</h1>
  {% endif %}
</body>
////////////////////
import datetime
from flask import Flask, reder_template

app = Flask(__name__)

@app.route("/")
def index():
  return "Hello, world!"
  
@app.route("/david")
def index():
  return "Hello, David!"
  
@app.route("/<string:name>")
def hello(name):
  name = name.capitalize()
  return f"Hello, {name}!"
  
@app.route("/")
def index():
  headline = "Hello, world!"
  return render_template("index.html", headline=headline)
  
@app.route("/")
def index():
  now = datetime.datetime.now()
  new_year = now.month ==1 and now.day == 1
  return render_template("index.html", new_year=new_year)
  
@app.route("/more")
def more():
  return render_template("more.html")

<a href="{{ url_for('more') }}">See more...</a>

/////////////////////////////////////
<body>
<h1>{% block heading %}{% endblock %}
</h1>
{% block body %}
{% endblock %}
/////////////////////////////////////
index.html

{% extend "layout.html" %}

{% block heading %}
  First Page
{% endblock %}


{% block body %}
  axxxxxxxassaasdsdsa
{% endblock %}

//////////////////////////////////////

{% block body %}
  <form action="{{ url_for('hello') }}" method="post">
  <input type="text" name="name" placeholder="Enter Your name">
  <button>Submit</button>
  </form>
{% endblock %}

from flask import Flask, render_template, request

app = Flask(__name__)

@app.rout("/hello", methods=["POST"])
hello():
name = reqest.form.get("name")
return render_template("hello.html", name=name)

///////////////////////////////////////
