from flask import Flask, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import environ, path

db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__, instance_relative_config=False)

    # Application Configuration
    app.config.from_object('config.Config')

    # Initialize Plugins
    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        from models import User
        from auth import account
        from recipe import recipes

        # Register Blueprints
        app.register_blueprint(account, url_prefix='/account/')
        app.register_blueprint(recipes, url_prefix='/recipe/')

        # Create Database Models
        db.create_all()

        @login_manager.user_loader
        def load_user(identifier):
            return User.query.get(int(identifier))

        # Error Management
        @app.errorhandler(404)
        def page_not_found(error):
            return redirect(url_for('recipe.all_recipes'))

        quest = User.query.filter_by(id=0).first()
        if not quest:
            new_user = User(id=0, username="Guest")
            new_user.set_password("password")
            db.session.add(new_user)
            db.session.commit()
            print("Quest user created")
        admin = User.query.filter_by(id=69420).first()
        if not admin:
            ADMIN_PSWD = environ.get('ADMIN_PSWD') or 'password'
            new_user = User(id=69420, username="Admin")
            new_user.set_password(ADMIN_PSWD)
            db.session.add(new_user)
            db.session.commit()
            print("Quest user created")

        return app
