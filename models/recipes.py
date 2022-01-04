from sqlalchemy import func

from __init__ import db


# Recipes object
class Recipes(db.Model):
    __tablename__ = 'recipe'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    dish_name = db.Column(db.String(200))
    date = db.Column(db.DateTime(timezone=True), default=func.now())

    img_url = db.Column(db.String)

    dices = db.relationship('Dishes', backref='recipe')
    description = db.Column(db.String)
    instructions = db.Column(db.String)
    serving = db.Column(db.Integer)
    difficulty = db.Column(db.Integer)
    total_time = db.Column(db.String)
    prep_time = db.Column(db.String)
    cook_time = db.Column(db.String)
    allergens = db.Column(db.Integer)
    tags = db.Column(db.Integer)

    saves = db.Column(db.Integer)


# Created Recipes object
class Dishes(db.Model):
    __tablename__ = 'dish'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String)

    ingredients = db.relationship('Ingredients', backref='dish')
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)


# Created Recipes object
class Ingredients(db.Model):
    __tablename__ = 'ingredients'

    id = db.Column(db.Integer, primary_key=True)

    ingredient = db.Column(db.String)
    amount = db.Column(db.String)
    unit = db.Column(db.String)
    dish_id = db.Column(db.Integer, db.ForeignKey('dish.id'), nullable=False)
