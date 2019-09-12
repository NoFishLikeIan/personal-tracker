from .functools_ext import find, find_all
from .text_utils import remove_punct
from .update_lenses import add_coffee, add_travel

meal_keys = set(['lunch', 'breakfast', 'dinner', 'other'])
possible_foods = set(['sweet', 'carb', 'proteins', 'water', 'veg'])


def check_for_food(words):
    meal = None
    foods = []

    for w in words:
        found_meal = find(meal_keys, lambda meal: meal in w)
        if found_meal is not None:
            meal = found_meal
        else:
            food = find(possible_foods, lambda food: food in w)
            if food:
                foods.append(food)

    return meal, foods


def keyword_mapping(text_content: str):
    words = remove_punct(text_content).lower().split()
    words_set = set(words)

    if 'coffee' in words_set:
        number = find(words_set, lambda s: type(s) == str and s.isdigit())
        if number:
            return add_coffee(int(number))
        else:
            return add_coffee(1)

    if 'travel':
        number = find(words_set, lambda s: type(s) == str and s.isdigit())
        if number:
            return add_travel(int(number))
        else:
            return add_travel(1)
