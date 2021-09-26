import unittest
from models.tag import Tag

class TestTag(unittest.TestCase):

    def setUp(self):
        self.tag = Tag("groceries")

    def test_tag_has_name(self):
        self.assertEqual("groceries", self.tag.name)
