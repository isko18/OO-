'''1.  git config --global user.name "YOUR USERNAME ON GITHUB"
   2.  git config --global user.email "YOUR EMAIL ON GITHUB"'''

"БД - База Данных"
"СУБД - Система управления базой данных"
"CRUD - Create, Reade, Update, Delete"

import sqlite3

connect = sqlite3.connect("instagram.db")
cursor = connect.cursor()

cursor.execute("""
                CREATE TABLE IF NOT EXISTS instagram(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    full_name VARCHAR (30) NOT NULL,
                    username VARCHAR (50),
                    age INT DEFAULT NULL, 
                    birth_date DATE,
                    raiting DOUBLE (4,2) DEFAULT 0.0,
                    is_activ BOOLEAN NOT NULL DEFAULT FALSE
                )""")

def register():
    full_name = input("Введите ФИО: ")
    username = input("Введите свой username: ")
    age = int(input("Введите возраст: "))
    birth_date = input("Введите дату рождения: ")
    raiting = float(input("Оцените приложение: "))
    is_activ = bool(input("Принятие соглашения о конфедициальности: "))
    print("Успешно зарегистрированы!")
    
    # cursor.execute("""INSERT INTO  instagram 
    #                (full_name, username, age, birth_date, raiting, is_activ)
    #                VALUES ('?', '?', ?, '?', ?, ?)""", full_name, username, age, birth_date, raiting, is_activ)

    cursor.execute(f"""INSERT INTO  instagram 
                   (full_name, username, age, birth_date, raiting, is_activ)
                   VALUES ('{full_name}', '{username}', {age}, '{birth_date}', {raiting}, {is_activ})""")
    
    connect.commit()
    
def all_studets():
    cursor.execute("SELECT * FROM instagram")
    student = cursor.fetchall()
    print(student)
    
# register()
all_studets()

