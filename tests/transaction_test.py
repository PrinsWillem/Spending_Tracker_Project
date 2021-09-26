import unittest
from models.transaction import Transactions
from models.merchant import Merchant
from models.tag import Tag

class TestTransaction(unittest.TestCase):

    def setUp(self):
        self.transaction = Transactions("Tesco", "Groceries", 12.00)

    def test_transaction_has_amount(self):
        self.assertEqual(12.00, self.transaction.amount)

    def test_transaction_has_merchant(self):
        self.assertEqual("Tesco", self.transaction.merchant)

    def test_transaction_has_tag(self):
        self.assertEqual("Groceries", self.transaction.tag)