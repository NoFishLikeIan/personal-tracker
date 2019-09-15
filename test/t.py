import unittest
from src.utils.update_parser import keyword_mapping


class TestKeywordMapping(unittest.TestCase):
    def test_adding_coffee(self):
        coffee_m = 'I had 2 coffees today'
        _, update_m = keyword_mapping(coffee_m)
        updated_m = update_m({'coffee': 1, 'food': {}})
        self.assertDictEqual(updated_m, {'coffee': 3, 'food': {}})

        coffee_s = 'Coffee'
        _, update_s = keyword_mapping(coffee_s)
        updated_s = update_s({})
        self.assertDictEqual(updated_s, {'coffee': 1})


if __name__ == '__main__':
    unittest.main()
