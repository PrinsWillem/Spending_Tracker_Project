from db.run_sql import run_sql
from models.transaction import Transaction
import repositories.merchant_repository as merchant_repositories
import repositories.tag_repository as tag_repositories

def save(transaction):
    sql = "INSERT INTO transactions (merchant_id, tag_id, amount) VALUES (%s, %s, %s) RETURNING id"
    values = [transaction.merchant.id, transaction.tag.id, transaction.amount]
    results = run_sql(sql, values)
    transaction.id = results[0]['id']
    return transaction

def select_all():
    transactions = []

    sql = "SELECT * FROM transactions"
    results = run_sql(sql)

    for row in results:
        merchant = merchant_repositories.select(row['merchant_id'])
        tag = tag_repositories.select(row['tag_id'])
        transaction = Transaction(merchant, tag, row['amount'], row['id'])
        transactions.insert(0, transaction)
    return transactions

def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM transactions WHERE id = %s"
    values = [id]
    run_sql(sql, values)