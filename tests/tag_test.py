import unittest
from models.tag import Tag

class TestTag(unittest.TestCase):

    def setUp(self):
        self.tag = Tag("Groceries")

    def test_tag_has_name(self):
        self.assertEqual("Groceries", self.tag.name)
