import json
import re


def load_file():
    with open('notebook.json', 'r', encoding = "utf-8") as nb:
        global notebook
        notebook = json.load(nb)
    print('Телефонный справочник был успешно загружен')

try:
    load_file()
except:
    notebook = {
        "Петров Василий" : {'phone_numbers': [11111, 22222], 'date_of_birth': '10.10.2001', 'email': 'petrov@mail.ru'},
        "Иванов Сергей" : {'phone_numbers': [742454, 464878713212], 'date_of_birth': '09.12.1998', 'email': 'ivanovs@gmail.com'}
        }

print('Для получения информации по использованию справочника введите команду "/help"')

def enter_the_name():
    second_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    patronymic_surname = input('Введите отчество: ')
    return second_name + " " + first_name + " " + patronymic_surname

def add_phone_number(name):
    notebook[name]['phone_numbers'].append(input('Пожалуйста, введите номер телефона контакта: '))

def ask_for_additional_num(add_num, name):
    while input('Хотели бы вы внести ещё один номер телефона? Если да - ответьте "Да", если нет - нажмите "enter" \n') == "Да":
        add_num(name)

def save():
    with open('notebook.json', 'w', encoding = "utf-8") as nb:
        nb.write(json.dumps(notebook, ensure_ascii = False))
    print('Телефонный справочник был успешно сохранён в файле notebook.json')

def print_not_found():
    print('К сожалению, контакт с таким именем отсутствует в справочнике. Возможно, в запросе присутствует опечатка.')

def print_success_changes():
    print('Изменения успешно сохранены.')

def print_list_of_numbers(name):
    numbers = list(enumerate(notebook[name]['phone_numbers'], 1))
    for i in numbers:
        print(*i)

def change_date(name):
    notebook[name]['date_of_birth'] = input('Введите дату рождения контакта: ')

def change_email(name):
    notebook[name]['email'] = input('Введите электронную почту контакта: ')


while True:
    command=input('Введите команду: ')
    if command == '/start': # это для будущего телеграм-бота
        print('Телефонный справочник начал свою работу')
    elif command == '/add':
        name = enter_the_name()
        notebook[name] = {'phone_numbers' : []}
        add_phone_number(name)
        ask_for_additional_num(add_phone_number, name)
        change_date(name)
        change_email(name)
        print('Контакт был успешно добавлен в записную книгу')
    elif command == '/save':
        save()
    elif command == '/load':
        load_file()
    elif command == '/stop':
        save()
        print('Телефонный справочник завершил работу. Будем ждать Вас снова')
        break
    elif command == '/search':
        contact = input('Введите имя для поиска: ')
        count_all = 0
        count_in = 0
        for i in notebook.keys():
            if re.search(contact, i):
                print(i, ":", notebook[i])
                count_in += 1
            count_all += 1
            if count_all == len(notebook.keys()) and count_in == 0:
                print_not_found()
    elif command == '/delete':
        contact = input('Введите ФИО контакта, который Вы хотели бы удалить: ')
        try:
            del notebook[contact]
            print('Контакт был успешно удалён из справочника.')
        except:
            print_not_found()
    elif command == '/show':
        print(notebook)

    elif command == '/interrupt':
        break
    elif command == '/help':
        print(f' Для запуска бота используйте команду "/start"\n Для просмотра всего справочника используйте команду "/show"\n Для добавления нового контакта используйте команду "/add"\n Для внесения изменений в имеющийся контакт используйте команду "/change"\n Для удаления одного из контактов используйте команду "/delete"\n Для сохранения справочника используйте команду "/save"\n Для загрузки справочника из файла используйте команду "/load"\n Для поиска контакта используйте команду "/search"\n Для прекращения работы справочника без сохранения внесённых изменений используйте команду "/interrupt"\n Для прекращения работы справочника с предварительным сохранением используйте команду "/stop"')
    else:
        print('Неизвестная команда. Пожалуйста, прочтите инструкцию по использованию телефонного справочника, используя команду /help')