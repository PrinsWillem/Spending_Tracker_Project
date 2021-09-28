import unittest
from models.transaction import Transaction
from models.merchant import Merchant
from models.tag import Tag

class TestTransaction(unittest.TestCase):

    def setUp(self):
        self.transaction_1 = Transaction("Tesco", "Groceries", 12.00)
        self.transaction_2 = Transaction("Scotrail", "Transport", 9.00)
        self.transaction_3 = Transaction("Aldi", "Groceries", 5.00)
        self.transaction_4 = Transaction("Cineworld", "Entertainment", 9.00)

    # @unittest.skip("delete this line to run the test")
    def test_transaction_has_amount(self):
        self.assertEqual(12.00, self.transaction_1.amount)

    # @unittest.skip("delete this line to run the test")
    def test_transaction_has_merchant(self):
        self.assertEqual("Tesco", self.transaction_1.merchant)

    # @unittest.skip("delete this line to run the test")
    def test_transaction_has_tag(self):
        self.assertEqual("Groceries", self.transaction_1.tag)


    
