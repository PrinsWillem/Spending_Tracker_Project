import pdb
from models.merchant import Merchant
from models.tag import Tag
from models.transaction import Transaction

import repositories.tag_repository as tag_repository
import repositories.merchant_repository as merchant_repository
import repositories.transaction_repository as transactions_repository

merchant_repository.delete_all()
tag_repository.delete_all()

merchant1 = Merchant('Tesco')
merchant_repository.save(merchant1)
merchant2 = Merchant('Cineworld')
merchant_repository.save(merchant2)

tag1 = Tag('Groceries')
tag_repository.save(tag1)
tag2 = Tag('Entertainment')
tag_repository.save(tag2)

transaction1 = Transaction(merchant1, tag1, 35.00)
transaction2 = Transaction(merchant2, tag2, 10.00)

pdb.set_trace()