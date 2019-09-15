from .functools_ext import find, find_all
from .text_utils import remove_punct
from .update_lenses import add_coffee, add_travel, lens_food

meal_keys = set(['lunch', 'breakfast', 'dinner', 'other'])
possible_foods = set(['sweet', 'carb', 'proteins', 'water', 'veg'])


def check_for_food(words):
    meal = None
    foods = []
    breakpoint()
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

    if find(words_set, lambda word: 'coffee' in word):
        number = find(words_set, lambda s: type(s) == str and s.isdigit())
        if number:
            return add_coffee(int(number))
        else:
            return add_coffee(1)

    if find(words_set, lambda word: 'travel' in word):
        number = find(words_set, lambda s: type(s) == str and s.isdigit())
        if number:
            return add_travel(int(number))
        else:
            return add_travel(1)

    meal, food = check_for_food(words_set)

    if meal:
        return lens_food({
            meal: food
        })
