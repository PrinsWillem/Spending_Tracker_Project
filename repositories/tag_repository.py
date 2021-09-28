from db.run_sql import run_sql
from models.tag import Tag
from models.merchant import Merchant

def save(tag):
    sql = "INSERT INTO tags (name) VALUES (%s) RETURNING *"
    values = [tag.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    tag.id = id
    return tag

def select_all():
    tags = []

    sql = "SELECT * FROM tags"
    results = run_sql(sql)
    for row in results:
        tag = Tag(row['name'], row['id'])
        tags.append(tag)
    return tags

def select(id):
    tag = None
    sql = "SELECT * FROM tags WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        tag = Tag(result['name'], result['id'])
    return tag

def delete_all():
    sql = "DELETE FROM tags"
    run_sql(sql)

def merchants(tag):
    merchants = []
    sql = "SELECT merchants.* FROM merchants INNER JOIN transactions ON transactions.merchant_id = merchants.id WHERE tag_id = %s"
    values = [tag.id]
    results = run_sql(sql, values)

    for row in results:
        merchant = Merchant(row['name'], row['id'])
        merchants.append(merchant)
    return merchants

# def delete(id):
#     sql = "DELETE FROM tags WHERE id = %s"
#     values = [id]
#     run_sql(sql, values)

def update(tag):
    sql = "UPDATE tags SET (name) = (%s) WHERE id = %s"
    values = [tag.name, tag.id]
    run_sql(sql, values)


