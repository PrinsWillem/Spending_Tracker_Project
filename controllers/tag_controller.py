from controllers.merchant_controller import merchants
from flask import Flask, Blueprint, render_template,  request, redirect
from models.tag import Tag
import repositories.tag_repository as tag_repository

tags_blueprint = Blueprint("tag", __name__)

@tags_blueprint.route("/tags")
def tags():
    tags = tag_repository.select_all()
    return render_template("tags/index.html", tags = tags)

# SHOW
@tags_blueprint.route("/tags/<id>")
def show(id):
    tag = tag_repository.select(id)
    merchants = tag_repository.merchants(tag)
    return render_template("tags/show.html", tag = tag, merchants = merchants)

# NEW
@tags_blueprint.route("/tags/new")
def new_tag():
    return render_template("tags/new.html")

# CREATE
@tags_blueprint.route("/tags", methods=['POST'])
def create_tag():
    name = request.form["name"]
    new_tag = Tag(name)
    tag_repository.save(new_tag)
    return redirect('/tags')
