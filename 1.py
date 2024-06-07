def create_todo_list():
    n = int(input("Р’РІРµРґРёС‚Рµ РєРѕР»РёС‡РµСЃС‚РІРѕ РґРµР»: "))
    todo_list = []

    for i in range(n):
        todo = input("Р’РІРµРґРёС‚Рµ РґРµР»Рѕ {}: ".format(i + 1))
        todo_list.append(todo)

    with open("todo_list.txt", "w") as file:
        for i in range(0, n, 2):
            file.write(todo_list[i] + " ")

    print("Р”РµР»Р° Р±С‹Р»Рё СѓСЃРїРµС€РЅРѕ Р·Р°РїРёСЃР°РЅС‹ РІ С„Р°Р№Р» todo_list.txt.")


create_todo_list()
