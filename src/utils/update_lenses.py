from lenses import lens
from collections import defaultdict

from .functools_ext import identity, uniq, compose


def add(field: str):
    def fn(n: int):
        stage = lens.Get(field)
        return stage.collect(), stage.modify(lambda m: (m or 0) + n)

    return fn


add_coffee = add('coffee')
add_travel = add('travel')


def lens_fields(new_data):
    incoming_fields = set(new_data.keys())

    stage = lens.Each().Filter(
        lambda tup: tup[0] in incoming_fields)

    def update_field(field_tup):
        key = field_tup[0]
        return (key, new_data[key])

    update = stage.modify(update_field)

    return stage.collect(), update


def lens_food(food):
    incoming_meals = set(food.keys())

    stage = lens.Get('food').Each().Filter(
        lambda tup: tup[0] in incoming_meals)

    def add_food(food_tup):
        meal, food_list = food_tup
        return (meal, uniq(food_list + food[meal]))

    update = stage.modify(add_food)

    return stage.collect(), update, True