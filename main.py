import collections

# pets = dict()
pets = {1 : {'Джек' : {'Вид питомца' : 'овчарка', 'Возраст питомца' : 5, 'Имя владельца' : 'Олег'}},
        2: {'Джек' : {'Вид питомца' : 'кот', 'Возраст питомца' : 1, 'Имя владельца' : 'Вика'}},
        3: {'Каркарыч': {'Вид питомца' : 'ворон', 'Возраст питомца' : 10, 'Имя владельца' : 'Миша'}},
        4: {'Мурзик': {'Вид питомца' : 'ворон', 'Возраст питомца' : 15, 'Имя владельца' : 'Антон'}},
        5: {'Маня': {'Вид питомца' : 'чихуа', 'Возраст питомца' : 3, 'Имя владельца' : 'Женя'}},
        6: {'Рекс': {'Вид питомца' : 'кот', 'Возраст питомца' : 5, 'Имя владельца' : 'Анна'}}}

def help():
    print(
        "Список возможных команд для ввода:\n"
        "create - Создать новую запись о питомце\n"
        "read - Прочитать запись о питомце\n"
        "update - Обновить запись о питомце\n"
        "delete - Удалить запись о питомце"
        )

def get_pet(ID: int) -> dict:
    return pets[ID] if ID in pets.keys() else False


def pet_id(pet_name: str):
    for id, pet in pets.items():
        if pet_name in pet:
            return id
    return None

def search_pet(pet_name: str):
    ids = []
    for id, pet in pets.items():
        if pet_name in pet:
            ids.append(id)

    return None if ids == [] else ids #, [pets[ID] for ID in ids]

def get_suffix(age: int) -> str:
    if age == 1:
        return 'год'
    elif age in [2, 3, 4]:
        return 'года'
    else:
        return 'лет'


def pets_list():
    output = list()
    for pet_id, pet in pets.items():
        for pet_name, info in pet.items():
            output.append(f'{pet_id} | {info['Вид питомца'].capitalize()} по кличке "{pet_name}". Возраст питомца: {info['Возраст питомца']} {get_suffix(info['Возраст питомца'])}. Имя владельца: {info['Имя владельца']}')

    return "\n".join(output)


def create(PetName: int, TypeOfPet: str, AgeOfPet: int, OwnerName: str) -> None:
    new_pet = {
        PetName: {
            'Вид питомца': TypeOfPet.capitalize(),
            'Возраст питомца': AgeOfPet,
            'Имя владельца': OwnerName
        }
    }

    if len(pets) == 0:
        pet_id = 1
    else:
        pet_id = collections.deque(pets, maxlen=1)[0] + 1

    pets[pet_id] = new_pet


def read(goal: str or int) -> str:
    out = "Записи найдены:\n"
    for pet_id, pet in pets.items():
        for pet_name, info in pet.items():
            if (str(goal).lower() in pet_name.lower() or goal == info['Возраст питомца'] or str(goal).lower() in info['Имя владельца'].lower()):
                out += f'{info['Вид питомца'].capitalize()} по кличке "{pet_name}". Возраст питомца: {info['Возраст питомца']} {get_suffix(info['Возраст питомца'])}. Имя владельца: {info['Имя владельца']}\n'
    return f"Не найдено записи с данной кличкой!" if out == "Записи найдены:\n" else out

def update(pet_name: str):
    from pprint import pprint
    IDs = search_pet(pet_name)

    if IDs == None:
        print("Данной записи не найдено!")
        return
    elif len(IDs) > 1:
        print("Найдено несколько записей: ")
        choise = {}
        for num in range(len(IDs)):
            
            choise[num + 1] = IDs[num]
            for pet_name, info in pets[IDs[num]].items():
                print(f'Номер: {num + 1} | {info['Вид питомца'].capitalize()} по кличке "{pet_name}". Возраст питомца: {info['Возраст питомца']} {get_suffix(info['Возраст питомца'])}. Имя владельца: {info['Имя владельца']}')
        ID = str()
        while type(ID) == str:
            ID = input(f"\nВведите номер нужной записи для обновления информации о питомце -> ")
            if not ID.strip() or not ID.isdigit() or isinstance(ID, int):
                        print("Номер должен быть числом! Попробуйте ещё раз")
            else:
                ID = int(ID)
    else:
        ID = int(IDs[0])
    
    update_goal = int(input(f"Что Вы хотите изменить?\n"
                            f"1) Кличку\n"
                            f"2) Вид питомца\n"
                            f"3) Возраст питомца\n"
                            f"4) Имя владельца питомца\n\n"
                            "[Введите только цифру] -> ").strip())

    change = input("Введите новое значение -> ") if update_goal == 3 else input("Введите новое значение -> ")



    if 0 < update_goal < 5:
        match update_goal:
            case 1:
                if not change.strip():
                    print("Кличка не может быть пустой! Попробуйте ещё раз")
                    return
                pets[ID] = {change: pets[ID].pop(pet_name)}
            case 2:
                if not change.strip(): 
                    print("Тип питомца не может быть пустым! Попробуйте ещё раз")
                    return
                pets[ID][pet_name]['Вид питомца'] = change
            case 3:
                if not change.strip() or not change.isdigit() or isinstance(change, int):
                    print("Возраст должен быть числом! Попробуйте ещё раз")
                    return
                pets[ID][pet_name]['Возраст питомца'] = int(change)
            case 4:
                if not change.strip():
                    print("Имя хозяина не может быть пустым! Попробуйте ещё раз")
                    return
                pets[ID][pet_name]['Имя владельца'] = change

    print("Информация успешно обновлена!")
    
    return pets


def delete(pet_name: str):
    from pprint import pprint
    IDs = search_pet(pet_name)

    if IDs == None:
        print("Данной записи не найдено!")
        return
    elif len(IDs) > 1:
        print("Найдено несколько записей: ")
        choise = {}
        for num in range(len(IDs)):
            
            choise[num + 1] = IDs[num]
            for pet_name, info in pets[IDs[num]].items():
                print(f'Номер: {num + 1} | {info['Вид питомца'].capitalize()} по кличке "{pet_name}". Возраст питомца: {info['Возраст питомца']} {get_suffix(info['Возраст питомца'])}. Имя владельца: {info['Имя владельца']}')
        ID = str()
        while type(ID) == str:
            ID = input(f"\nВведите номер нужной записи для удаления -> ")
            if not ID.strip() or not ID.isdigit() or isinstance(ID, int):
                        print("Номер должен быть числом! Попробуйте ещё раз")
            else:
                ID = int(ID)
    else:
        ID = int(IDs[0])

    pets.pop(ID)
    print(f"Запись и о питомце {pet_name} удалена")


def main():
    command = ''
    while command != 'stop':
        help()
        command = input("Введите команду: ").strip().lower()

        match command:
            case "create":
                PetName = input("Введите кличку питомца -> ")
                if not PetName.strip():
                    print("Кличка не может быть пустой! Попробуйте ещё раз")
                    continue

                TypeOfPet = input("Введите тип (пароду) питомца -> ")
                if not TypeOfPet.strip(): 
                    print("Тип питомца не может быть пустым! Попробуйте ещё раз")
                    continue

                AgeOfPet = input("Введите возраст питомца -> ")
                if not AgeOfPet.strip() or not AgeOfPet.isdigit() or isinstance(AgeOfPet, int):
                    print("Возраст должен быть числом! Попробуйте ещё раз")
                    continue

                OwnerName = input("Введите имя хозяина питомца -> ")
                if not OwnerName.strip():
                    print("Имя хозяина не может быть пустым! Попробуйте ещё раз")
                    continue

                create(PetName, TypeOfPet, AgeOfPet, OwnerName)
                
                print('Питомец успешно добавлен!')
            case "read":
                read_input = input("Введите кличку питомца для поиска -> ").strip()

                print(read(read_input))
            case "update":
                update_input = input("Введите кличку питомца для обновления информации о нем -> ").strip()

                update(update_input)
            case "delete":
                delete_input = input("Введите кличку питомца для удаления информации о нем -> ").strip()

                delete(delete_input)
            case "stop":
                print("До встречи!")
            case _:
                print("Команда не распознана!")


if __name__ == "__main__":
    main()
