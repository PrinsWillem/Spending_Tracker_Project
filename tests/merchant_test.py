import unittest
from models.merchant import Merchant

class TestMerchant(unittest.TestCase):

    def setUp(self):
        self.merchant = Merchant("Aldi")

    def test_merchant_has_name(self):
        self.assertEqual("Aldi", self.merchant.name)