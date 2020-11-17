import unittest
documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def print_name():
    number = input('Введите номер документа')
    for doc in documents:
        if number in doc["number"]:
            a = doc["name"]

            return a


p = print(print_name())


def print_shelf_number():
    number = input('Введите номер документа')
    for shelf, doc_number in directories.items():
        if number in doc_number:
            docs_on_shelf = ('Документ на полке', shelf)
            return docs_on_shelf


s = print_shelf_number()


def add_data():
    dict_for_personal_data = {}
    name = input('Введите имя')
    doc_type = input('Введите тип документа')
    number = input('Введите номер документа')
    shelf_n = int(input('Введите номер полки'))
    dict_for_personal_data["type"] = doc_type
    dict_for_personal_data["number"] = number
    dict_for_personal_data["name"] = name
    documents.append(dict_for_personal_data)
    if shelf_n == 1:
        directories['1'].append(number)
    elif shelf_n == 2:
        directories['2'].append(number)
    elif shelf_n == 3:
        directories['3'].append(number)
    else:
        print('Полка не существует')
    print(documents)
    print(directories)


a = print(add_data())
docs = dict()


class TestSomething(unittest.TestCase):
    def setUp(self):
        docs.append({"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"})

    def tearDown(self):
        docs.remove({"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"})

    def test_print_names(self):
        self.assertMultiLineEqual(print_name(docs["number"]), docs["name"])


