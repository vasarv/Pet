import collections

pets = dict()

def get_pet(ID: int) -> dict:
    return pets[ID] if ID in pets.keys() else False


def pet_id(pet_name: str):
    for id, pet in pets.items():
        if pet_name in pet:
            return id


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
    for pet_id, pet in pets.items():
        for pet_name, info in pet.items():
            if (str(goal).lower() in pet_name.lower() or goal == info['Возраст питомца'] or str(goal).lower() in info['Имя владельца'].lower()):
                return f'{info['Вид питомца'].capitalize()} по кличке "{pet_name}". Возраст питомца: {info['Возраст питомца']} {get_suffix(info['Возраст питомца'])}. Имя владельца: {info['Имя владельца']}', pet_id
    return f"Не найдено записи с данной кличкой!"


def update(pet_name: str):
    ID = pet_id(pet_name)

    update_goal = int(input(f"Что Вы хотите изменить?\n"
                            f"1) Кличку\n"
                            f"2) Вид питомца\n"
                            f"3) Возраст питомца\n"
                            f"4) Имя владельца питомца\n\n"
                            "[Введите только цифру] -> ").strip())

    change = int(input("Введите новое значение -> ")) if update_goal == 3 else input("Введите новое значение -> ")

    if 0 < update_goal < 5:
        match update_goal:
            case 1:
                pets[ID] = {change: pets[ID].pop(pet_name)}
            case 2:
                pets[ID][pet_name]['Вид питомца'] = change
            case 3:
                pets[ID][pet_name]['Возраст питомца'] = change
            case 4:
                pets[ID][pet_name]['Имя владельца'] = change

    return pets


def delete(pet_name: str):
    pets.pop(pet_id(pet_name))
    print(f"Запись и о питомце {pet_name} удалена")


def main():
    command = ''
    while command != 'stop':
        command = input("Введите команду: ").strip().lower()

        match command:
            case "create":
                pet_info = input(f"Введите необходимые данные [Имя питомца, Тип питомца, Возраст питомца, Имя хозяина питомца] в формате (строка,строка) -> ").split(",")

                PetName, TypeOfPet, AgeOfPet, OwnerName = pet_info[0], pet_info[1], pet_info[2], pet_info[3]

                create(PetName, TypeOfPet, AgeOfPet, OwnerName)

                print('Питомец успешно добавлен!')
            case "read":
                read_input = input("Введите кличку питомца для поиска: ").strip()

                print(read(read_input))
            case "update":
                update_input = input("Введите кличку питомца для обновления информации о нем: ").strip()

                update(update_input)

                print("Информация успешно обновлена!")
            case "delete":
                delete_input = input("Введите кличку питомца для удаления информации о нем: ").strip()

                delete(delete_input)
            case "stop":
                ...
            case _:
                print("Команда не распознана!")

    raise KeyboardInterrupt


if __name__ == "__main__":
    main()
