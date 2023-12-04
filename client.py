import json

client_info = {}


def load(name='client_info.json'):
    global client_info
    with open(name, 'r', encoding='utf-8') as data:
        client_info = json.load(data)


def show_info():
    load()
    global client_info
    print('Информация о счетах')

    for account in client_info['accounts']:
        print('----------------------------------')
        print("Имя: ", account['name'])
        print("Платежная системма", account['system'])
        print("Номер: ", account['number'])
        print("Тип: ", account['type'])
        print("Баланс: ", account['balance'])
        print("Срок действия: ", account['validity period'])
        print('----------------------------------')


def predict():
    load()
    global client_info
    expenses = 0.0
    income = 0.0
    months = []
    for t in client_info['transactions']:
        if t["type"] == 'зачисление':
            expenses += t["amount"]
        if t["type"] == 'списание':
            income += t["amount"]

        if t["date"] not in months:
            months.append(t["date"])

    print('Предполагаемые расходы в следующем месяце:', int(income) / int(len(months)))
    print('Предполагаемые доходы в следующем месяце:', int(expenses) / int(len(months)))
    # return expenses, income



def restaurant_data():
    restaurant = {"details": []}
    with open('input.txt', 'r', encoding='utf-8') as data:
        f = data.read()
        f = f.split('***')
        for s in f:
            a = s.strip().split('\n')
            restaurant['details'].append({'administrator': a[0], 'workers': a[1].split(', '), 'turnover': int(a[2]), 'revenue': int(a[3]), 'tips': int(a[4])})

    return restaurant


def save(name='client_info.json'):
    global client_info
    with open(name, 'w', encoding='utf-8') as outdata:
        json.dump(client_info, outdata)


def suggestions():
    with open('suggestions.txt', 'r', encoding='utf-8') as f:
        print('Предложения от SkysmartBank')
        print(f.read())





def make_transaction():
    load()
    global client_info
    transaktion_types = ['списание', 'зачисление']
    print("Доступные счета:")
    i = 1
    for account in client_info["accounts"]:
        print(i, "-", account["name"], "-", account["number"])
        i += 1

    account_num = input("Введите счёт: ")

    try:
        account_num = int(account_num)
    except:
        print("Ошибка ввода. Прерываю транзакцию...")
        return

    for i in range(len(client_info["accounts"])):
        if i + 1 == account_num:
            account = client_info["accounts"][i]["number"]
            break
    else:
        print("Такого счёта не существует. Прерываю транзакцию...")
        return
    print("Типы транзакций:")
    print('1 -', transaktion_types[0])
    print('2 -', transaktion_types[1])
    transaction_type = input("Выберите тип транзакции: ")
    if transaction_type == "1":
        transaction_type = transaktion_types[0]
    elif transaction_type == "2":
        transaction_type = transaktion_types[1]
    else:
        print("Такого типа не существует. Прерываю транзакцию...")
        return

    print("Дата транзакции")
    year = input("Введите год: ")
    month = input("Введите месяц: ")

    if int(year) > 2023 or int(month) > 12 or int(month) < 1:
        print("Неверная дата. Прерываю транзакцию...")
        return

    try:
        amount = int(input("Введите сумму: "))
    except:
        print('Ошибка ввода. Прерываю транзакцию...')
        return

    if amount < 1:
        print("Сумма не может быть меньше 1. Прерываю транзакцию...")
        return

    new_data = {"account": account,
                "type": transaction_type,
                "date": {"year": year, "month": month},
                "amount": amount}

    for i in range(len(client_info['accounts'])):
        if client_info['accounts'][i]['number'] == new_data['account']:
            if new_data['type'] == 'списание':
                client_info['accounts'][i]['balance'] -= new_data['amount']
            else:
                client_info['accounts'][i]['balance'] += new_data['amount']
    print(new_data)
    for i in range(len(client_info['accounts'])):
        if client_info['accounts'][i]['number'] == new_data['account']:
            print('Транзакция записана. Текущий баланс на счёте:', client_info['accounts'][i]['balance'])
            client_info['transactions'].append(new_data)


def complain():
    with open('complains.txt', 'a', encoding='utf-8') as f:
        comp = input('Введите свою жалобу/похвалу: ')
        f.write(comp + '\n')
        print('Ваша жалоба будет рассмотрена в скором времени.')
