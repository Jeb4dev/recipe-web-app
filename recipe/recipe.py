import json

from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from recipe import recipes
from models import Recipes, Dishes, Ingredients
from models import User
from __init__ import db


# recipe page
@recipes.route('/example/', methods=['GET', 'POST'])
def recipe():
    ingredients = {"title": "Poronkäristys ja ruskistettu pottuvoi",
                   "menu": [
                       {"name": "Poronkäristys",
                        "ingredients": [
                            {"ingredient": "poronkäristyslihaa",
                             "amount": "20",
                             "unit": "kg"},
                            {"ingredient": "sipuli",
                             "amount": "1",
                             "unit": ""}
                        ]
                        },
                       {"name": "Ruskistettu pottuvoi",
                        "ingredients": [
                            {"ingredient": "puikulaperunaa",
                             "amount": "1",
                             "unit": "kg"},
                            {"ingredient": "voita",
                             "amount": "150",
                             "unit": "g"}
                        ]
                        },
                       {"name": "Lisäksi",
                        "ingredients": [
                            {"ingredient": "suolakurkkua",
                             "amount": "",
                             "unit": ""},
                            {"ingredient": "puolukkaa",
                             "amount": "",
                             "unit": ""}
                        ]
                        }
                   ],
                   "serving": "4",
                   "instructions": [
                       "Ota poronkäristysliha sulamaan. Kuori ja hienonna sipuli. ",
                       "Kuumenna voi pannulla tai padassa. Lisää sipulit ja kuullota hetki. Lisää joukkoon kohmeinen poronkäristysliha parissa erässä ja anna paistua välillä käännellen. ",
                       "Lisää mausteet, olut ja vesi. Anna kiehahtaa ja hauduta kannen alla miedolla lämmöllä tunti tai kunnes liha on mureaa. Lisää tarvittaessa nestettä. "
                   ],
                   "description": "Poronkäristys valmistuu hitaasti haudutellen. Pottuvoi on loistolisäke käristykselle. Ihanaa makua potuille antaa ruskistettu voi. ",
                   "time": {
                       "prep": "20 min",
                       "cook": "50 min",
                       "total": "1 h 10 min",
                    },
                   "difficulty": "intermediate",
                   "tags": ["Dinner", "Meat"],
                   "allergens": ["egg"],
                   "img": "https://cdn.valio.fi/mediafiles/aec4ad8c-e390-41ba-89e8-dddb42fcbebb/1000x752-recipe-hero/4x3/poronkaristys-ja-ruskistettu-pottuvoi.jpg"
                   }

    return render_template("recipe.html", ingredients=ingredients)


# recipe page
@recipes.route('/create/', methods=['GET', 'POST'])
def create():
    ingredients = {"title": "Poronkäristys ja ruskistettu pottuvoi",
                   "menu": [
                       {"name": "Poronkäristys",
                        "ingredients": [
                            {"ingredient": "poronkäristyslihaa",
                             "amount": "20",
                             "unit": "kg"},
                            {"ingredient": "sipuli",
                             "amount": "1",
                             "unit": ""}
                        ]
                        },
                       {"name": "Ruskistettu pottuvoi",
                        "ingredients": [
                            {"ingredient": "puikulaperunaa",
                             "amount": "1",
                             "unit": "kg"},
                            {"ingredient": "voita",
                             "amount": "150",
                             "unit": "g"}
                        ]
                        },
                       {"name": "Lisäksi",
                        "ingredients": [
                            {"ingredient": "suolakurkkua",
                             "amount": "",
                             "unit": ""},
                            {"ingredient": "puolukkaa",
                             "amount": "",
                             "unit": ""}
                        ]
                        }
                   ],
                   "serving": "4",
                   "instructions": [
                       "Ota poronkäristysliha sulamaan. Kuori ja hienonna sipuli. ",
                       "Kuumenna voi pannulla tai padassa. Lisää sipulit ja kuullota hetki. Lisää joukkoon kohmeinen poronkäristysliha parissa erässä ja anna paistua välillä käännellen. ",
                       "Lisää mausteet, olut ja vesi. Anna kiehahtaa ja hauduta kannen alla miedolla lämmöllä tunti tai kunnes liha on mureaa. Lisää tarvittaessa nestettä. "
                   ],
                   "description": "Poronkäristys valmistuu hitaasti haudutellen. Pottuvoi on loistolisäke käristykselle. Ihanaa makua potuille antaa ruskistettu voi. ",
                   "time": {
                       "prep": "20 min",
                       "cook": "50 min",
                       "total": "1 h 10 min",
                    },
                   "difficulty": "intermediate",
                   "tags": ["Dinner", "Meat"],
                   "allergens": ["egg"],
                   "img": "https://cdn.valio.fi/mediafiles/aec4ad8c-e390-41ba-89e8-dddb42fcbebb/1000x752-recipe-hero/4x3/poronkaristys-ja-ruskistettu-pottuvoi.jpg"
                   }
    new_recipe = Recipes(user_id=0)
    db.session.add(new_recipe)
    db.session.commit()
    new_recipe.dish_name = "Poronkäristys ja ruskistettu pottuvoi"
    new_recipe.img_url = "https://cdn.valio.fi/mediafiles/aec4ad8c-e390-41ba-89e8-dddb42fcbebb/1000x752-recipe-hero/4x3/poronkaristys-ja-ruskistettu-pottuvoi.jpg"
    new_recipe.description = "Poronkäristys valmistuu hitaasti haudutellen. Pottuvoi on loistolisäke käristykselle. Ihanaa makua potuille antaa ruskistettu voi. "
    instructions = ["Ota poronkäristysliha sulamaan. Kuori ja hienonna sipuli. ",
                               "Kuumenna voi pannulla tai padassa. Lisää sipulit ja kuullota hetki. Lisää joukkoon kohmeinen poronkäristysliha parissa erässä ja anna paistua välillä käännellen. ",
                               "Lisää mausteet, olut ja vesi. Anna kiehahtaa ja hauduta kannen alla miedolla lämmöllä tunti tai kunnes liha on mureaa. Lisää tarvittaessa nestettä. "
                               ]
    new_recipe.instructions = json.dumps(instructions)
    new_recipe.serving = 4
    new_recipe.difficulty = 2
    new_recipe.total_time = "1 h 10 min"
    new_recipe.prep_time = "50 min"
    new_recipe.cook_time = "20 min"
    new_recipe.allergens = 0
    new_recipe.tags = 0
    new_recipe.saves = 0

    new_dishes = Dishes(recipe_id=new_recipe.id, name="Poronkäristys")
    db.session.add(new_dishes)
    db.session.commit()

    new_ingredients = Ingredients(dish_id=new_dishes.id)
    new_ingredients.ingredient = "puikula perunaa"
    new_ingredients.amount = "0.5"
    new_ingredients.unit = "kg"

    db.session.add(new_ingredients)
    db.session.add(new_dishes)

    db.session.commit()

    return render_template("recipe.html", ingredients=ingredients)


# recipe page
@recipes.route('/example2/', methods=['GET', 'POST'])
def look():
    ingredients = {"dish_name": "Poronkäristys ja ruskistettu pottuvoi",
                   "menu": [
                       {"name": "Poronkäristys",
                        "ingredients": [
                            {"ingredient": "poronkäristyslihaa",
                             "amount": "20",
                             "unit": "kg"},
                            {"ingredient": "sipuli",
                             "amount": "1",
                             "unit": ""}
                        ]
                        },
                       {"name": "Ruskistettu pottuvoi",
                        "ingredients": [
                            {"ingredient": "puikulaperunaa",
                             "amount": "1",
                             "unit": "kg"},
                            {"ingredient": "voita",
                             "amount": "150",
                             "unit": "g"}
                        ]
                        },
                       {"name": "Lisäksi",
                        "ingredients": [
                            {"ingredient": "suolakurkkua",
                             "amount": "",
                             "unit": ""},
                            {"ingredient": "puolukkaa",
                             "amount": "",
                             "unit": ""}
                        ]
                        }
                   ],
                   "serving": "4",
                   "instructions": [
                       "Ota poronkäristysliha sulamaan. Kuori ja hienonna sipuli. ",
                       "Kuumenna voi pannulla tai padassa. Lisää sipulit ja kuullota hetki. Lisää joukkoon kohmeinen poronkäristysliha parissa erässä ja anna paistua välillä käännellen. ",
                       "Lisää mausteet, olut ja vesi. Anna kiehahtaa ja hauduta kannen alla miedolla lämmöllä tunti tai kunnes liha on mureaa. Lisää tarvittaessa nestettä. "
                   ],
                   "description": "Poronkäristys valmistuu hitaasti haudutellen. Pottuvoi on loistolisäke käristykselle. Ihanaa makua potuille antaa ruskistettu voi. ",
                   # "time": {
                   #     "prep": "20 min",
                   #     "cook": "50 min",
                   #     "total": "1 h 10 min",
                   #  },
                   "total_time": "1h 10 min",
                   "prep_time": "20 min",
                   "cook_time": "50 min",
                   "difficulty": "intermediate",
                   "tags": ["Dinner", "Meat"],
                   "allergens": ["egg"],
                   "img_url": "https://cdn.valio.fi/mediafiles/aec4ad8c-e390-41ba-89e8-dddb42fcbebb/1000x752-recipe-hero/4x3/poronkaristys-ja-ruskistettu-pottuvoi.jpg"
                   }
    with db.session.no_autoflush:
        recipe = Recipes.query.filter_by(id=2).first()
        print(recipe)
        recipe.tags = []
        recipe.allergens = []
        recipe.instructions = json.loads(recipe.instructions)
        recipe.menu = Dishes.query.filter_by(recipe_id=2).all()
        return render_template("recipe.html", ingredients=recipe)

