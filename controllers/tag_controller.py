from controllers.merchant_controller import merchants
from flask import Flask, Blueprint, render_template,  request, redirect
from models.tag import Tag
import repositories.tag_repository as tag_repository
import repositories.transaction_repository as transaction_repository
import pdb

tags_blueprint = Blueprint("tag", __name__)

@tags_blueprint.route("/tags")
def tags():
    tags = tag_repository.select_all()
    return render_template("tags/index.html", tags = tags)

# SHOW
@tags_blueprint.route("/tags/<id>")
def show(id):
    tag = tag_repository.select(id)
    merchant_amounts = {}
    all_transactions = transaction_repository.select_all()
    total_categories_spent = 0
    for transaction in all_transactions:
        if transaction.tag.name == tag.name:
            total_categories_spent += transaction.amount
            if transaction.merchant.name not in merchant_amounts:
                merchant_amounts[transaction.merchant.name] = 0
            merchant_amount = merchant_amounts[transaction.merchant.name]
            merchant_amounts[transaction.merchant.name] = merchant_amount + transaction.amount
    # pdb.set_trace()
    return render_template("tags/show.html", tag = tag, merchant_amounts = merchant_amounts, total_categories_spent = total_categories_spent)

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

# EDIT
@tags_blueprint.route("/tags/<id>/edit", methods=['GET'])
def edit_tag(id):
    tag = tag_repository.select(id)
    return render_template('tags/edit.html', tag = tag)

# UPDATE
@tags_blueprint.route("/tags/<id>", methods=['POST'])
def update_tag(id):
    name = request.form["name"]
    tag = Tag(name, int(id))
    tag_repository.update(tag)
    return redirect('/tags')
