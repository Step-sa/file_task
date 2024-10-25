def get_cook_book(file):
    recipes = dict()
    flag = True
    for row in file:
        if flag:
            current_food = row[:-1]
            recipes[current_food] = []
            file.readline()
            flag = False
            continue
        if row == "\n":
            flag = True
            continue
        t = dict()
        split_row = row.split(" | ")
        t['ingredient_name'] = split_row[0]
        t['quantity'] = split_row[1]
        t['measure'] = split_row[2][:-1]
        recipes[current_food].append(t)
    return recipes


def cool_print(d: dict):
    for key in d.keys():
        print(key, d[key])


# Исправлен первоначальный вариант
def get_shop_list_by_dishes(cook_book: dict, dishes: list[str], person_count: int):
    shop_list = dict()
    for dish in dishes:
        for item in cook_book[dish]:
            quantity = int(item['quantity'])
            quantity = quantity * person_count
            if item['ingredient_name'] not in shop_list.keys():
                shop_list[item['ingredient_name']] = {'measure': item['measure'], 'quantity': quantity}
            else:
                shop_list[item['ingredient_name']]['quantity'] += quantity
    return shop_list

# Новый вариант с другой логикой
def get_shop_list_by_dishes2(cook_book: dict, dishes: list[str], person_count: int):
    to_set_to_list_dishes = list(set(dishes))
    for dish in to_set_to_list_dishes:
        for item in cook_book[dish]:
            item['quantity'] = int(item['quantity']) * person_count * dishes.count(dish)
    shop_list = dict()
    for dish in to_set_to_list_dishes:
        for item in cook_book[dish]:
            shop_list[item['ingredient_name']] = {'measure': item['measure'], 'quantity': item['quantity']}
    return shop_list


if __name__ == "__main__":
    file = open('C:/Users/user/Desktop/files/recipes.txt', encoding="UTF-8")
    my_cook_book = get_cook_book(file)

    cool_print(get_shop_list_by_dishes(my_cook_book, ['Омлет', 'Омлет'], 2))
    print()
    cool_print(get_shop_list_by_dishes2(my_cook_book, ['Омлет', 'Омлет'], 2))

