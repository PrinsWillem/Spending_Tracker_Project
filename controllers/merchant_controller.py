from flask import Flask, Blueprint, render_template, request, redirect
from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository
import repositories.transaction_repository as transaction_repository
import pdb

merchants_blueprint = Blueprint("merchants", __name__)

@merchants_blueprint.route("/merchants")
def merchants():
    merchants = merchant_repository.select_all()
    return render_template("merchants/index.html", merchants = merchants)

# SHOW
@merchants_blueprint.route("/merchants/<id>")
def show(id):
    merchant = merchant_repository.select(id)
    tags = merchant_repository.tags(merchant)
    tag_names = []
    for tag in tags:
        tag_names.append(tag.name)
    unique_tags = []
    for tag in tag_names:
         if tag not in unique_tags:
             unique_tags.append(tag)
    all_transactions = transaction_repository.select_all()
    total_merchants_spent = 0
    for transaction in all_transactions:
        if transaction.merchant.name == merchant.name:
            total_merchants_spent += transaction.amount
    # pdb.set_trace()
    return render_template("merchants/show.html", merchant = merchant, unique_tags = unique_tags, total_merchants_spent = total_merchants_spent)

# NEW
@merchants_blueprint.route("/merchants/new")
def new_merchant():
    return render_template("merchants/new.html")

# CREATE
@merchants_blueprint.route("/merchants", methods=['POST'])
def create_merchant():
    name = request.form["name"]
    new_merchant = Merchant(name)
    merchant_repository.save(new_merchant)
    return redirect('/merchants')
