if __name__ == "__main__":
    file = open('C:/Users/user/Desktop/files/recipes.txt', encoding="UTF-8")
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
    file.close()
    print(recipes)