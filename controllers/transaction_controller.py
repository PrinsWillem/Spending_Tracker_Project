from flask import Flask, Blueprint, render_template, request, redirect
from models.transaction import Transaction
import repositories.transaction_repository as transaction_repository
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository

transactions_blueprint = Blueprint("transactions", __name__)

@transactions_blueprint.route("/transactions")
def transactions():
    transactions = transaction_repository.select_all()
    return render_template("transactions/index.html", transactions = transactions)

# NEW
# GET '/transactions/new'
@transactions_blueprint.route("/transactions/new", methods=['GET'])
def new_transaction():
    merchants = merchant_repository.select_all()
    tags = tag_repository.select_all()
    return render_template("transactions/new.html", merchants = merchants, tags = tags)

# NEW
# POST '/transactions'
@transactions_blueprint.route("/transactions", methods=['POST'])
def create_transaction():
    merchant_id = request.form['merchant_id']
    tag_id = request.form['tag_id']
    amount = request.form['number_amount']
    merchant = merchant_repository.select(merchant_id)
    tag = tag_repository.select(tag_id)
    transaction = Transaction(merchant, tag, amount)
    transaction_repository.save(transaction)
    return redirect('/transactions')

# DELETE '/transactions/<id>'
@transactions_blueprint.route("/transactions/<id>/delete", methods=['POST'])
def delete_transaction(id):
    transaction_repository.delete(id)
    return redirect('/transactions')
