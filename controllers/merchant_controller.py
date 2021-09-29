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
    tag_amounts = {}
    all_transactions = transaction_repository.select_all()
    total_merchants_spent = 0
    for transaction in all_transactions:
        if transaction.merchant.name == merchant.name:
            total_merchants_spent += transaction.amount
            if transaction.tag.name not in tag_amounts:
                tag_amounts[transaction.tag.name] = 0
            tag_amount = tag_amounts[transaction.tag.name]
            tag_amounts[transaction.tag.name] = tag_amount + transaction.amount 
    # pdb.set_trace()
    return render_template("merchants/show.html", merchant = merchant, tag_amounts = tag_amounts, total_merchants_spent = total_merchants_spent)

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

# EDIT
@merchants_blueprint.route("/merchants/<id>/edit", methods=['GET'])
def edit_merchant(id):
    merchant = merchant_repository.select(id)
    return render_template('merchants/edit.html', merchant = merchant)

# UPDATE
@merchants_blueprint.route("/merchants/update/<id>", methods=['POST'])
def update_merchant(id):
    name = request.form["name"]
    merchant = Merchant(name, int(id))
    # pdb.set_trace()
    merchant_repository.update(merchant)
    return redirect('/merchants')
