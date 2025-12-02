documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def get_owner_by_doc_number(doc_number: str):
    """Возвращает имя владельца документа по его номеру или None, если документ не найден."""
    for doc in documents:
        if doc["number"] == doc_number:
            return doc["name"]
    return None


def handle_command_p():
    """Обработка команды p — поиск владельца документа по номеру."""
    doc_number = input("Введите номер документа:\n")
    owner = get_owner_by_doc_number(doc_number)
    if owner:
        print(f"Владелец документа: {owner}")
    else:
        print("Документ с таким номером не найден.")


def main():
    """Главный цикл работы программы."""
    while True:
        command = input("Введите команду (p - найти владельца, q - выход):\n").strip().lower()

        if command == "q":
            print("Работа программы завершена.")
            break
        elif command == "p":
            handle_command_p()
        else:
            print("Неизвестная команда, попробуйте снова.")


if __name__ == "__main__":
    main()