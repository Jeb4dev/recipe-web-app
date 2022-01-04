from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from __init__ import db


# User object
class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), nullable=False)
    password_hash = db.Column(db.String(200))
    saved_recipes = db.relationship('SavedRecipes', backref='user')
    added_recipes = db.relationship('UserRecipes', backref='user')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


# Created Recipes object
class UserRecipes(db.Model):
    __tablename__ = 'user_recipe'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    recipe_id = db.Column(db.Integer, nullable=False)


# Saved Recipes object
class SavedRecipes(db.Model):
    __tablename__ = 'saved_recipe'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    recipe_id = db.Column(db.Integer, nullable=False)

