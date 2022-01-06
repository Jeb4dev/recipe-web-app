import json

from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from recipe import recipes
from models import Recipes, Dishes, Ingredients
from models import User, UserRecipes, SavedRecipes
from __init__ import db


# recipe page
@recipes.route('/', methods=['GET'])
def all_recipes():
    recipes = Recipes.query.all()
    recipes_data = []
    for i in range(len(recipes)):
        recipe_data = {"name": recipes[i].dish_name,
                       "img": recipes[i].img_url,
                       "time": recipes[i].total_time,
                       "saves": recipes[i].saves,
                       "id": recipes[i].id,
                       }
        recipes_data.append(recipe_data)
    return render_template("all.html", data=recipes_data)


# create recipe page
@recipes.route('/create/', methods=['GET', 'POST'])
def create():

    if request.method == "POST":
        user_id = 0
        if current_user.is_authenticated:
            user_id = current_user.id

        print(request.form)

        new_recipe = Recipes(user_id=user_id)
        db.session.add(new_recipe)
        db.session.commit()

        new_recipe.dish_name = request.form.get('recipe_name')
        new_recipe.description = request.form.get('recipe_desc')
        new_recipe.difficulty = request.form.get('recipe_diff')
        new_recipe.serving = request.form.get('recipe_serving')
        new_recipe.img_url = request.form.get('img_name')
        new_recipe.saves = 0
        new_recipe.tags = ""
        new_recipe.allergens = ""

        # Uploaded img
        img_upload = request.form.get('img_upload')
        if img_upload:
            pass

        new_recipe.prep_time = request.form.get('recipe_preptime')
        new_recipe.cook_time = request.form.get('recipe_cooktime')
        new_recipe.total_time = request.form.get('recipe_totaltime')

        # Instructions
        instruction = request.form.get('recipe_instruction')
        i = 0
        instructions = []
        while True:
            if request.form.get(f'recipe_instruction_{i}'):
                instruction = request.form.get(f'recipe_instruction_{i}')
                instructions.append(instruction)
                i += 1
            else:
                break
        # print(instructions)
        new_recipe.instructions = json.dumps(instructions)

        # Meals
        j = 0
        meal_names = []
        while True:
            if request.form.get(f'meal_name_{j}'):
                meal_name = request.form.get(f'meal_name_{j}')
                meal_names.append(meal_name)

                new_dishes = Dishes(recipe_id=new_recipe.id, name=meal_name)
                db.session.add(new_dishes)
                db.session.commit()

                # Incredients

                i = 0
                ing_name = request.form.get(f'{j}_ing_name')
                ing_amount = request.form.get(f'{j}_ing_amount')
                ing_unit = request.form.get(f'{j}_ing_unit')

                new_ingredients = Ingredients(dish_id=new_dishes.id)

                new_ingredients.ingredient = ing_name
                new_ingredients.amount = ing_amount
                new_ingredients.unit = ing_unit

                print("-----------------------")
                print(f" meal name: {meal_name}")
                print(f"{meal_name} ingredients")
                print(f" ing_name: {ing_name} - {j}_ing_name")
                print(f" ing_amount: {ing_amount}")
                print(f" ing_unit: {ing_unit}")
                print("-----------------------")

                db.session.add(new_ingredients)
                while True:
                    if request.form.get(f'{j}_ing_name_{i}'):
                        ing_name = request.form.get(f'{j}_ing_name_{i}')
                        ing_amount = request.form.get(f'{j}_ing_amount_{i}')
                        ing_unit = request.form.get(f'{j}_ing_unit_{i}')

                        new_ingredients = Ingredients(dish_id=new_dishes.id)

                        new_ingredients.ingredient = ing_name
                        new_ingredients.amount = ing_amount
                        new_ingredients.unit = ing_unit

                        db.session.add(new_ingredients)

                        print("-----------------------")
                        print(f" meal name: {meal_name}")
                        print(f"{meal_name} ingredients")
                        print(f" ing_name: {ing_name} - {j}_ing_name_{i}")
                        print(f" ing_amount: {ing_amount}")
                        print(f" ing_unit: {ing_unit}")
                        print("-----------------------")

                        i += 1
                    else:
                        print(f'FAILED to find: {j}_ing_name_{i}')
                        break
                    db.session.add(new_dishes)

                    db.session.commit()
                j += 1
            else:
                break

        # Add recipe to user that created it
        new_user_recipe = UserRecipes(user_id=user_id, recipe_id=new_recipe.id)
        db.session.add(new_user_recipe)
        db.session.commit()

        return redirect(url_for('recipe.look', identifier=new_recipe.id))
    return render_template("create.html")


# recipe page
@recipes.route('/<identifier>/', methods=['GET', 'POST'])
def look(identifier):
    try:
        with db.session.no_autoflush:
            recipe_id = identifier
            recipe = Recipes.query.filter_by(id=recipe_id).first()
            if not recipe:
                return redirect(url_for('recipe.all_recipes'))
            print(recipe)
            recipe.tags = []
            recipe.allergens = []
            if recipe.difficulty == 0:
                recipe.difficulty = "Easy"
            elif recipe.difficulty == 1:
                recipe.difficulty = "Intermediate"
            elif recipe.difficulty == 2:
                recipe.difficulty = "Advanced"

            recipe.instructions = json.loads(recipe.instructions)
            recipe.menu = Dishes.query.filter_by(recipe_id=recipe_id).all()
            if current_user.is_authenticated:
                user_id = current_user.id
                liked = SavedRecipes.query.filter_by(user_id=user_id, recipe_id=recipe_id).first()
                if liked:
                    recipe.saved = True
                else:
                    recipe.saved = False
            else:
                recipe.saved = False
            return render_template("recipe.html", ingredients=recipe)
    except TypeError:
        return redirect(url_for('recipe.look', identifier=1))


# add recipe to saved recipes
@login_required
@recipes.route('/<identifier>/save/', methods=['GET'])
def save(identifier):
    with db.session.no_autoflush:
        recipe_id = identifier
        recipe = Recipes.query.filter_by(id=recipe_id).first()
        if not recipe:
            return "error 404: no dish with that id was found"

        liked = SavedRecipes.query.filter_by(user_id=current_user.id, recipe_id=recipe_id).first()
        if liked:
            liked.delete()
            print(f"ERROR: save was already found with: user_id {current_user.id} and recipe_id {recipe_id}.")
            return redirect(url_for("recipe.look", identifier=recipe_id))
        else:
            new_liked = SavedRecipes(user_id=current_user.id, recipe_id=recipe_id)
            recipe.saves += 1
            db.session.add(new_liked)
            db.session.commit()
            return redirect(url_for("recipe.look", identifier=recipe_id))


# remove recipe to saved recipes
@login_required
@recipes.route('/<identifier>/unsave/', methods=['GET'])
def unsave(identifier):
    with db.session.no_autoflush:
        recipe_id = identifier
        recipe = Recipes.query.filter_by(id=recipe_id).first()
        if not recipe:
            return "ERROR 404: no dish with that id was found"

        liked = SavedRecipes.query.filter_by(user_id=current_user.id, recipe_id=recipe_id).first()
        if liked:
            recipe.saves -= 1
            db.session.delete(liked)
            db.session.commit()
            return redirect(url_for("recipe.look", identifier=recipe_id))
        else:
            return f"ERROR 404: save was not found with: user_id {current_user.id} and recipe_id {recipe_id}."
