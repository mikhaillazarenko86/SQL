import sqlite3 as sq

# Создание базы данных
def ad_db(name_db):
    try:
        con = sq.connect(name_db)
        cursor = con.cursor()
        print("База данных успешно создана")
        con.commit()
    except sq.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (con):
            con.close()
            print("Соединение с SQLite закрыто")

# Обработка запросов
def query(name_db, query):
    try:
        con = sq.connect(name_db)
        cursor = con.cursor()
        print("База данных подключена к SQLite")
        cursor.execute(query)
        con.commit()
    except sq.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (con):
            con.close()
            print("Соединение с SQLite закрыто")
# ВЫборка данных
def select_values(name_db, query):
    try:
        con = sq.connect(name_db)
        cursor = con.cursor()
        print("База данных подключена к SQLite")
        cursor.execute(query)
        for result in cursor:
            print(result)
        con.commit()
    except sq.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (con):
            con.close()
            print("Соединение с SQLite закрыто")
# Множественное добавление данных в таблицу
def add_values(name_db, query, list_values):
    try:
        con = sq.connect(name_db)
        cursor = con.cursor()
        print("База данных подключена к SQLite")
        cursor.executemany(query, list_values)
        con.commit()
    except sq.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (con):
            con.close()
            print("Соединение с SQLite закрыто")

# Создание таблицы
create_table_query = '''CREATE TABLE mobile_phones(
     id INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT,
     product_name VARCHAR(45),
     manufacture VARCHAR(45),
     product_count INTEGER,
     price MONEY);'''
# Наполнение таблицы данными
mobile_phones =[
    ('Iphone X', 'Apple', 3, 76000),
    ('Iphone 8', 'Apple', 2, 51000),
    ('Galaxy S9', 'Samsung', 2, 56000),
    ('Galaxy S8', 'Samsung', 1, 41000),
    ('P20Pro', 'Huawei', 5, 36000)]


# Запрос на добавление данны из списка
sqlite_add_query = "INSERT INTO mobile_phones VALUES(NULL, ?, ?, ?, ?)"
# Запросы на выборку данных
select_values_manufacture = "SELECT * FROM mobile_phones WHERE manufacture == 'Samsung';"
select_manufacture_price =  "SELECT price, manufacture FROM mobile_phones WHERE product_count > 2;"
select_product_iphone =  "SELECT * FROM mobile_phones WHERE product_name LIKE '%iphone%';"
select_product_samsung =  "SELECT * FROM mobile_phones WHERE product_name LIKE '%galaxy%';"
select_product_number =  "SELECT * FROM mobile_phones WHERE product_name GLOB '* [0-9]';"
select_product_number_eight =  "SELECT * FROM mobile_phones WHERE product_name LIKE  '%8%';"
name_db = "/Users/mihaillazarenko/Documents/Developer/SQL/study.db"

select_values(name_db, select_product_number)
