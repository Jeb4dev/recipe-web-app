# Recipe web app
Recipe web app coded in python using flask framework.

## Purpose
This project was made as part of the weekly programming challenge hosted by [DevJam].
The project was made for learning purposes.
### What I learned
tba. 
All recipes
![image](https://user-images.githubusercontent.com/76889226/148412394-313de2d9-f7a6-4444-82cb-e3ebf0f9bad0.png)
One Recipe
![image](https://user-images.githubusercontent.com/76889226/148412628-1a15daa0-f062-4504-9298-6d7bba5a1dc6.png)
Creating Recipe
![image](https://user-images.githubusercontent.com/76889226/148412736-3f150f37-ca4d-472b-b6a6-acc791ac17dd.png)


## [Live Demo](https://jeb-recipeapp.herokuapp.com/)



## About the Challenge
#### 🛠 Difficulty Level (of user stories): Beginner 
📅 Start: December 30th<br>
📅 Deadline: January 6th 16:00 (4PM) GMT

#### 📝 Project Description
Like programs, recipes are a series of imperative steps which, if followed correctly, result in a tasty dish.
##### 📑User Stories
- [ ] User can see a list of recipe titles ... ✔️
- [ ] User can click a recipe title to display a recipe card containing the recipe title, meal type (breakfast, lunch, supper, or snack), number of people it serves, its difficulty level (beginner, intermediate, advanced), the list of ingredients (including their amounts), and the preparation steps.
##### 🌟 Bonus features

- [ ] User can see a photo showing what the item looks like after it has been prepared.
- [ ] User can search for a recipe not in the list of recipe titles by entering the meal name into a search box and clicking a 'Search' button. Any open source recipe API may be used as the source for recipes (see The MealDB below).
- [ ] User can see a list of recipes matching the search terms
- [ ] User can click the name of the recipe to display its recipe card.
- [ ] User can see a warning message if no matching recipe was found. 
- [ ] User can click a 'Save' button on the cards for recipes located through the API to save a copy to this apps recipe file or database.

##### ✨ Custom features (not part of the challenge)
- [ ] tba.

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
App is hosted in heroku. Use `HEROKU` branch for heroku deployment as it also contains `Procfile`.


## Contribute?
Want to contribute? Awesome!  
This project was part of weekly challenges hosted by [DevJam] and won't be updated.
Maybe you would like to work with us, hit me up and let's talk. :)

## Credits
- [Scoreboard design](https://codepen.io/hakura/pen/ebglw) - Leaderboard design
- [Card design](https://codepen.io/hakura/pen/ebglw) - Cars design
- [Boostrap](https://codepen.io/hakura/pen/ebglw) - Some frontend elements like grids.
- [Fontawesome](https://fontawesome.com/) - Icons

## License
MIT


   [Flask]: <https://flask.palletsprojects.com/en/2.0.x/>
   [Flask-login]: <https://flask-login.readthedocs.io/en/latest/>
   [DevJam]: <https://discord.gg/nZBxGEudY6>
   [emojipedia]: <https://emojipedia.org/artist-palette/>
   [icons8]: <https://icons8.com/>
   [sharingbuttons]: <https://sharingbuttons.io/>
   [Handdrawn]: <https://fxaeberhard.github.io/handdrawn.css/>
   [imgbb]: <https://imgbb.com/upload>
   [Heroku]: <https://www.heroku.com>
