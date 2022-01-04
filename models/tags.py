from __init__ import db


# Tags object
class Tags(db.Model):
    __tablename__ = 'tag'

    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String)


# Tags object
class RecipeTags(db.Model):
    __tablename__ = 'recipe_tag'

    id = db.Column(db.Integer, primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)

