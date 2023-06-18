import re


def index_check(book: dict[int,dict]):
    id_contact = list(book.keys())
    return id_contact


def user_name():
    name = " ".join(word.capitalize() for word in input("Введите имя: ").split())
    return name


def mobile_num():
    mobile = input("Введи номер:")
    check_num = re.fullmatch(r"^(\+7|8)(\d{10}|[-(]\d{3}[-)]\d{3}-\d{4})", mobile)
    while not check_num:
        mobile = input("Номер указан некорректно. Повтори ввод: ")
        check_num = re.fullmatch(r"^(\+7|8)(\d{10}|[-(]\d{3}[-)]\d{3}-\d{4})", mobile)

    return mobile

def user_city(mess = "Название города: "):
    city = f"г. {input(mess).capitalize()}"
    return city

def check_cache():
    check_book = {}
    with open("cache.txt", 'r', encoding="UTF-8") as file:
        data = file.readlines()
    for contact in data:
        nc = contact.strip().split(':')
        check_book[int(nc[0])] = {"name": nc[1], "phone": nc[2], "city": nc[3]}
    if check_book == {}:
        return False
    return True
def caching_file(check: False):
    phone_book = {}
    if not check:
        file_name = "data.txt"
    else:
        file_name = "cache.txt"
    file = open(file_name, 'r', encoding="UTF-8")
    data = file.readlines()
    file.close()
    for contact in data:
        nc = contact.strip().split(':')
        phone_book[int(nc[0])] = {"name": nc[1], "phone": nc[2], "city": nc[3]}
    return phone_book

def print_contacts(book: dict[int,dict]):
    for i, contact in book.items():
        print(f'{i}. {contact.get("name")}: {contact.get("phone")} {contact.get("city")} ')
    print("--" * 50 + "\n")


# print_contacts(caching_file())

def save_file(book: dict[int,dict], main_data = "data.txt"):
    data = []
    for i, contact in book.items():
        new = ":".join([str(i),contact.get("name"), contact.get("phone"), contact.get("city")])
        data.append(new)
    data = '\n'.join(data)
    with open(main_data, "w", encoding='utf-8') as file:
        file.write(data)
    if main_data == "data.txt":
        with open("cache.txt", "w", encoding='utf-8') as file:
            file.write('')

def add_contact(book: dict[int,dict]):
    phone_book = book
    uid = max(list(phone_book.keys())) + 1
    phone_book[uid] = {"name": user_name(), "phone": mobile_num(), "city": user_city()}
    print_contacts(phone_book)
    save_file(phone_book, "cache.txt")
def search(book: dict[int,dict], mess = "Что ищем: "):
    result = {}
    word = input(mess)
    for i, contact in book.items():
        if word.lower() in ' '.join(list(contact.values())).lower():
            result[i] = contact
    return result

def remove(book: dict[int,dict]):
    result = search(book)
    print_contacts(result)
    index = int(input("Введи ID, который необходимо удалить."))
    del_cnt = book.pop(index)
    print(f'\nКонтакт {del_cnt.get("name")} удален!')
    save_file(book, "cache.txt")

def change_info(book: dict[int,dict]):
    actions = '''1. Изменить контакт полностью.
2. Изменить фамилию и имя.
3. Изменить номер.
4. Изменить город.
5. Отмена.
Введи номер команды: 
'''
    phone_book = book
    result = search(book, "Поиск контакта, который необходимо изменить: ")
    print_contacts(result)
    index = index_check(result)
    select = input("Введи ID контакта для изменения: ")
    while True:
        if select.isdigit() and int(select) in index:
            change_options = input(actions)
            select = int(select)
            if change_options.isdigit() and 0 < int(change_options) < 6:
                match int(change_options):
                    case 1:
                        phone_book[select] = {"name": user_name(), "phone": mobile_num(), "city": user_city()}
                        save_file(phone_book, "cache.txt")

                    case 2:
                        phone_book[select]["name"] = user_name()
                        save_file(phone_book, "cache.txt")

                    case 3:
                        phone_book[select]["phone"] = mobile_num()
                        save_file(phone_book, "cache.txt")

                    case 4:
                        phone_book[select]["city"] = user_city()
                        save_file(phone_book, "cache.txt")

                    case 5:
                        print("Изменение отменено!")
                        break
                print_contacts(phone_book)
                break
            print("Указанная команта не найдена.")

        else:
            print("Среди найденных контактов нет указанного ID!")
            select = input("Введи ID контакта для изменения: ")















