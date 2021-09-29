import pdb
from models.merchant import Merchant
from models.tag import Tag
from models.transaction import Transaction

import repositories.tag_repository as tag_repository
import repositories.merchant_repository as merchant_repository
import repositories.transaction_repository as transactions_repository

transactions_repository.delete_all()
merchant_repository.delete_all()
tag_repository.delete_all()

merchant1 = Merchant('Tesco')
merchant_repository.save(merchant1)
merchant2 = Merchant('Cineworld')
merchant_repository.save(merchant2)
merchant3 = Merchant('Morrisons')
merchant_repository.save(merchant3)
merchant4 = Merchant('Aldi')
merchant_repository.save(merchant4)
merchant5 = Merchant('M&S')
merchant_repository.save(merchant5)
merchant6 = Merchant('Odeon')
merchant_repository.save(merchant6)
merchant7 = Merchant('Vue')
merchant_repository.save(merchant7)
merchant8 = Merchant('Bryden Medical Ltd')
merchant_repository.save(merchant8)
merchant9 = Merchant('West Barbers')
merchant_repository.save(merchant9)
merchant10 = Merchant('END.')
merchant_repository.save(merchant10)


tag1 = Tag('Groceries')
tag_repository.save(tag1)
tag2 = Tag('Entertainment')
tag_repository.save(tag2)
tag3 = Tag('Housing')
tag_repository.save(tag3)
tag4 = Tag('Utilities')
tag_repository.save(tag4)
tag5 = Tag('Insurance')
tag_repository.save(tag5)
tag6 = Tag('Medical & Healthcare')
tag_repository.save(tag6)
tag7 = Tag('Personal Spending')
tag_repository.save(tag7)
tag7 = Tag('Clothing')
tag_repository.save(tag7)


transaction1 = Transaction(merchant1, tag1, 35.00)
transactions_repository.save(transaction1)
transaction2 = Transaction(merchant2, tag2, 10.00)
transactions_repository.save(transaction2)

pdb.set_trace()