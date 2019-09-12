from lenses import lens

parse_json = lens.Json()
new_food = lens.Get('food')


if __name__ == '__main__':
    comb = parse_json & new_food
    print(comb.get()('{"food": {"dinner": []}}'))
