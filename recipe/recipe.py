from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from recipe import recipes
from models import User
from __init__ import db


# login page
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
