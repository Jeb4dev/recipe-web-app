# Recipe Storage Web App
### Written in python using Flask
App contains recipe creation and automated recipe incrediants amount calculation depending of how many person recipe serves.


## Purpose
This project was made as part of the weekly programming challenge hosted by [DevJam].
The project was made for learning purposes.
### What I learned
The project was once againg very interesting and I learned lots of things like using css media print, lots of javascript, and for example using `white-space:no-wrap;`. Project included adding html elements via button clicks and using database relationships. 
## Screenshots and Demo
### [Live Demo](https://jeb-recipeapp.herokuapp.com/)
Recipe creation | List of recipes | Recipe card
![image](https://user-images.githubusercontent.com/76889226/148446624-e50610ff-7c71-413a-900d-47d6a54e6118.png)





## About the Challenge
#### 🛠 Difficulty Level (of user stories): Beginner 
📅 Start: December 30th<br>
📅 Deadline: January 6th 16:00 (4PM) GMT

#### 📝 Project Description
Like programs, recipes are a series of imperative steps which, if followed correctly, result in a tasty dish.
##### 📑User Stories
- ✔️ User can see a list of recipe titles
- ✔️ User can click a recipe title to display a recipe card containing the recipe title, meal type (breakfast, lunch, supper, or snack), number of people it serves, its difficulty level (beginner, intermediate, advanced), the list of ingredients (including their amounts), and the preparation steps.
##### 🌟 Bonus features

- ✔️ User can see a photo showing what the item looks like after it has been prepared.
- ❌ User can search for a recipe not in the list of recipe titles by entering the meal name into a search box and clicking a 'Search' button. Any open source recipe API may be used as the source for recipes.
- ❌ User can see a list of recipes matching the search terms
- ✔️ User can click the name of the recipe to display its recipe card.
- ❌ User can see a warning message if no matching recipe was found. 
- ✔️ User can click a 'Save' button on the cards for recipes located through the API to save a copy to this apps recipe file or __database__.

##### ✨ Custom features (not part of the challenge)
- ✔️ Automatical adding and reducing (not compleated yet) incrediants for certain amount of servings. 
- ✔️ User can create complicated recipes with unlimited ingrediants.
- ✔️ User can copy recipe link via button
- ✔️ User can print recipe
- ✔️ User can see times recipe takes to compleate, prepare and cook.
##### ✨📋 __TODO__ Custom features (not part of the challenge)
- [ ] User can add tags to recipes and sort all recipes by tags.
- [ ] User can edit recipes they have made and admin user can edit all recipes
- [ ] Admin user can delete recipes.
- [ ] Recipes cards show recipe creator.
- [ ] User can upload their own recipe images to the server and it will be saved in some 3rd party storage.
- [ ] Unit conversions (kg -> pounds for example)
- ✔️ Show saved recipes in different list.


## Tech

The app is written in python using Flaks-library. 
Frontend is written in html5, css and vanilla js.
Backend uses Flask sqlalchemy and flask-login.
App is deployed in [Heroku].

#### Frameworks and libraries:

- [Flask] - Micro web framework written in python.
- [Flask-Socketio](https://flask-socketio.readthedocs.io/en/latest/) - Flask-SocketIO gives Flask applications access to low latency bi-directional communications between the clients and the server.
- [Flask-login] - Flask-Login provides user session management for Flask.
#### Deployment
- [Heroku] - Heroku is a cloud platform as a service supporting several programming languages.



## Installation and running

This app requires [python 3.7+](https://www.python.org/downloads/) to run.

Clone git repo
```sh
git clone https://github.com/JesperKauppinen/quizapp.git
```

After cloning or downloading this git repo, install required python libraries

```sh
pip install -r requirements.txt
```

run app.py
```sh
python app.py
```
### Deployment
App is hosted in Heroku.  The deployment requires `Procfile`.

## Database
for Database is used postresql and flask-sqlalchemy.
Database structure
![image](https://user-images.githubusercontent.com/76889226/148434091-1ed42aa8-95e4-46de-b509-74d62432c050.png)


## Contribute?
Want to contribute? Awesome!  
This project was part of weekly challenges hosted by [DevJam] and won't be updated.
Maybe you would like to work with us, hit me up and let's talk. :)

## Credits
- [Valio](https://www.valio.fi/reseptit/haku/#) - HTML and CSS is mainly taken from valio website, please don't sue me.
- [Card design](https://www.quackit.com/css/grid/examples/css_grid_card_examples.cfm) - Cars design templte.
- [Fontawesome](https://fontawesome.com/) - Icons

Did I miss some credits, let me know and I will update them
## License
MIT

## Disclamer
Images and text (recipes) may be copyrighted.


   [Flask]: <https://flask.palletsprojects.com/en/2.0.x/>
   [Flask-login]: <https://flask-login.readthedocs.io/en/latest/>
   [DevJam]: <https://discord.gg/nZBxGEudY6>
   [emojipedia]: <https://emojipedia.org/artist-palette/>
   [icons8]: <https://icons8.com/>
   [sharingbuttons]: <https://sharingbuttons.io/>
   [Handdrawn]: <https://fxaeberhard.github.io/handdrawn.css/>
   [imgbb]: <https://imgbb.com/upload>
   [Heroku]: <https://www.heroku.com>
