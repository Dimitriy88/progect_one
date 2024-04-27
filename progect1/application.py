from data import Postgres
def show():
    sql = Postgres()
    print("Добро пожаловать в наш автосалон!")
    while True:
        client_inf = input('''### Данные клиента. ###
    1. Вывести данные клиента
    2. Добавить данные клиента
    3. Удалить данные клиента
    4. Обновить данные клиента
    5. Выбрать автомобиль
    6. Выход
    
    Выбор: ''')

        match client_inf:
            case '1':
                sql.select_client()
            case '2':
                surname = input('Surname: ')
                name = input('Name: ')
                sql.insert_client(surname, name)
            case '3':
                id = input('id: ')
                sql.delete(id)
            case '4':
                id = input('id: ')
                surname = input('surname: ')
                name = input('name: ')
                sql.update_client(id, surname, name)
            case '5':
                while True:
                    avto_inf = input('''### Данные автомобиля. ###
    1. Вывести данные автомобиля
    2. Добавить данные автомобиля
    3. Обновить данные автомобиля
    4. Выход
    
    Выбор: ''')

                    match avto_inf:
                        case '1':
                            sql.select_cars()
                        case '2':
                            brand = input('brand: ')
                            model = input('model: ')
                            color = input('color: ')
                            engine = input('engine: ')
                            sql.insert_cars(brand, model, color, engine)
                        case '3':
                            id = input('id: ')
                            client_id = input('client_id: ')
                            brand = input('brand: ')
                            model = input('model: ')
                            color = input('color: ')
                            engine = input('engine: ')
                            sql.update_cars(id, client_id, brand, model, color, engine)
                        case '4':
                            break
                        case _:
                            print('Что-то пошло не так! Выбирайте из списка.')
            case '6':
                break
            case _:
                print('Что-то пошло не так! Выбирайте из списка.')


