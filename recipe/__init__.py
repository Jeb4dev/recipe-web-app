from flask import Blueprint

recipes = Blueprint('recipe', __name__)

from .recipe import recipe
