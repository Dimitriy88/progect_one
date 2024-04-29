from abc import ABC, abstractmethod
import psycopg2
class Data(ABC):

    @abstractmethod
    def select_client(self):
        pass

    @abstractmethod
    def select_cars(self):
        pass

    @abstractmethod
    def insert_cars(self):
        pass

    @abstractmethod
    def insert_client(self):
        pass

    @abstractmethod
    def update_client(self):
        pass

    @abstractmethod
    def update_cars(self):
        pass

    @abstractmethod
    def delete_client(self):
        pass

    @abstractmethod
    def delete_cars(self):
        pass

class Postgres(Data):


    __CONNECTION = psycopg2.connect(host="localhost", database="progect1", user="postgres",password="111",port="5432")
    __CREATE_SCRIPTS = '''CREATE TABLE IF NOT EXISTS client(
    id serial PRIMARY KEY,
    surname TEXT,
    name TEXT);
    
    CREATE TABLE IF NOT EXISTS cars(
    id serial PRIMARY KEY,
    client_id INTEGER,
    brand TEXT,
    model TEXT,
    color TEXT,
    engine TEXT,
    FOREIGN KEY (client_id) REFERENCES client(id));'''


    def __init__(self):
        with self.__CONNECTION as self.sql:
            self.cursor = self.sql.cursor()
            self.cursor.execute(self.__CREATE_SCRIPTS)


    def select_client(self):
        with self.__CONNECTION as self.sql:
            self.cursor = self.sql.cursor()
            self.cursor.execute('''SELECT * FROM client;''')
            for data in self.cursor.fetchall():
                print(*data)

    def select_cars(self):
        with self.__CONNECTION as self.sql:
            self.cursor = self.sql.cursor()
            self.cursor.execute('''SELECT * FROM cars;''')
            for car in self.cursor.fetchall():
                print(*car)

    def insert_client(self, surname, name):
        with self.__CONNECTION.cursor() as self.sql:
            self.sql.execute('''INSERT INTO client(surname, name) VALUES(%s, %s)''', (surname, name))

    def insert_cars(self, client_id, brand, model, color, engine):
        with self.__CONNECTION.cursor() as self.sql:
            self.sql.execute('''INSERT INTO cars(client_id, brand, model, color, engine) 
                                        VALUES(%s, %s, %s, %s, %s)''', (client_id, brand, model, color, engine))

    def update_client(self, id, surname, name):
        with self.__CONNECTION.cursor() as self.sql:
            self.sql.execute('''UPDATE client SET surname = %s, name = %s  WHERE id = %s''', (surname, name, id))

    def update_cars(self, id, client_id, brand, model, color, engine):
        with self.__CONNECTION.cursor() as self.sql:
            self.sql.execute('''UPDATE cars SET client_id = %s, brand = %s, model = %s, color = %s, engine = %s  
                                        WHERE id = %s''', (client_id, brand, model, color, engine, id))

    def delete_client(self, id):
        with self.__CONNECTION.cursor() as self.sql:
            self.sql.execute('''DELETE FROM client WHERE id = %s''', (id))

    def delete_cars(self, client_id):
        with self.__CONNECTION.cursor() as self.sql:
            self.sql.execute('''DELETE FROM cars WHERE client_id = %s''', (client_id))