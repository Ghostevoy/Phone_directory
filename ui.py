from functions import *



def menu():
    menu = '''Меню:
1. Показать контакты.
2. Поиск
3. Добавить контакт.
4. Изменить контакт. 
5. Удалить контакт.
6. Сохранить изменения. 
7. Выход
=================
    '''
    print(menu)
    choice = input("Выбери команду: ")

    while True:
        if choice.isdigit() and 0 < int(choice) < 8:
            return int(choice)

        choice = input("Указана неверная команда. Повтори ввод: ")

def interface():
    while True:
        phone_book = caching_file(check_cache())
        choice = menu()
        match choice:
            case 1:
                print_contacts(phone_book)
                input("Нажми Enter для продолжения")
            case 2:
                print_contacts(search(phone_book))
                input("Нажми Enter для продолжения")
            case 3:
                add_contact(phone_book)
                print("Контакт добавлен! ")
                input("Нажми Enter для продолжения")
            case 4:
                change_info(phone_book)
                print("Изменения внесены! ")
                input("Нажми Enter для продолжения")
            case 5:
                remove(phone_book)
                input("Нажми Enter для продолжения")
            case 6:
                save_file(phone_book)
                print("Сохранено!")
                input("Нажми Enter для продолжения")
            case 7:
                print("Валим отсюда! ")
                break


