from lenses import lens

from .functools_ext import find, find_all
from .text_utils import remove_punct
from .update_lenses import add_coffee, add_travel, lens_food, lens_mood

meal_keys = set(['lunch', 'breakfast', 'dinner', 'other'])
possible_foods = set(['sweet', 'carb', 'proteins', 'water', 'veg'])
default_moods = ['happy', 'fine', 'sad', 'depressed', 'lonely', 'anxious']
default_food = dict(zip(
    meal_keys,
    map(lambda _: [], range(len(meal_keys)))
))


def check_for_food(words):
    meal = None
    foods = []
    for word in words:
        found_meal = find(meal_keys, lambda m: m in word)
        if found_meal is not None:
            meal = found_meal
        else:
            food = find(possible_foods, lambda f: f in word)
            if food:
                foods.append(food)

    return meal, foods


def check_for_mood(words):
    moods = []

    for word in words:
        mood = find(default_moods, lambda m: m in word)
        if mood:
            moods.append(mood)

    return moods


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
        }, default=default_food)

    mood = check_for_mood(words_set)
    if mood:
        return lens_mood(mood)


get_message = lens.Json().Get('message', default='').get()
