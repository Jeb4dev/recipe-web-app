from flask import Blueprint

recipes = Blueprint('recipe', __name__)

from .recipe import all_recipes, create, look, save, unsave