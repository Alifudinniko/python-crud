from enum import unique
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.wrappers import request

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} - {self.description}"


@app.route("/")
def index():
    return "Hello World!"

# @app.route("/food")
# def get_food():
#     return {"food":"food data"}


@app.route('/foods')
def get_foods():
    foods = Food.query.all()
    output = []
    for food in foods:
        food_data = {
            'name': food.name,
            'description': food.description
        }
        output.append(food_data)

    return {"foods": output}


@app.route('/foods/<id>')
def get_food(id):
    food = Food.query.get_or_404(id)
    return {"name": food.name, "description": food.description}


@app.route('/foods', methods=['POST'])
def add_food():
    food = Food(
        name=request.json['name'],
        description=request.json['description']
    )
    db.session.add(food)
    db.session.commit()
    return {'id': food.id}


@app.route('/foods/<id>', methods=['DELETE'])
def delete_food(id):
    food = Food.query.get(id)
    if food is None:
        return {"error": "not found"}

    db.session.delete(food)
    db.session.commit()
    return {"message": "yeet!"}
