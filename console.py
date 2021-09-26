import pdb
from models.merchant import Merchant
from models.tag import Tag

import repositories.tag_repository as tag_repository
import repositories.merchant_repository as merchant_repository

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

pdb.set_trace()