from flask import Flask
from flask_sqlalchemy import SQLAlchemy
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres+psycopg2://postgres:7898994162k@localhost:5432/2doapp'
app.config['SECRET_KEY'] = "random string"
 
db = SQLAlchemy(app)


 class Rectangle:
   def __init__(self, length, breadth, unit_cost=0):
       self.length = length
       self.breadth = breadth
       self.unit_cost = unit_cost
       print("created")
   
   def get_perimeter(self):
       return 2 * (self.length + self.breadth)
   
   def get_area(self):
       return self.length * self.breadth
   
   def calculate_cost(self):
       area = self.get_area()
       return area * self.unit_cost


@app.route('/')
def show_all():
   return "hello world"
 
if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)         