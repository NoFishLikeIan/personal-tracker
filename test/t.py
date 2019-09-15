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

    def test_food(self):
        dinner = 'I ate carbs for dinner'
        breakfast = 'Sweets for breakfast'

        _, update_food = keyword_mapping(dinner)
        dinner_mapped = update_food({})
        self.assertDictEqual(dinner_mapped, {
                             'food': {'breakfast': [], 'dinner': ['carb'], 'lunch': [], 'other': []}})

        _, update_existing_f = keyword_mapping(breakfast)
        existing_f = update_existing_f({
            'food': {
                'breakfast': ['carbs']
            }
        })

        updated_meals = set(existing_f['food']['breakfast'])

        self.assertEqual(updated_meals, set(['carbs', 'sweet']))


if __name__ == '__main__':
    unittest.main()
