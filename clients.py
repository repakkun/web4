import csv


def load_csv(path):
    with open(path, encoding="utf-8") as file:
        return list(csv.DictReader(file))


def transform_gender(sex):
    return "женского пола" if sex.lower() == "female" else "мужского пола"


def transform_device(device):
    return "мобильного" if device.lower() == "mobile" else "десктопного"


def build_description(client):
    gender = transform_gender(client["sex"])
    device = transform_device(client["device_type"])

    return (
        f"Пользователь {client['name']} {gender}, {client['age']} лет "
        f"совершил(а) покупку на {client['bill']} у.е. "
        f"с {device} браузера {client['browser']}. "
        f"Регион, из которого совершалась покупка: {client['region']}."
    )


def save_txt(path, lines):
    with open(path, "w", encoding="utf-8") as file:
        for line in lines:
            file.write(line + "\n")


def main():
    input_file = "web_clients_correct.csv"
    output_file = "clients_descriptions.txt"

    clients = load_csv(input_file)
    descriptions = [build_description(client) for client in clients]
    save_txt(output_file, descriptions)


if __name__ == "__main__":
    main()