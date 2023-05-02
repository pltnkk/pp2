import psycopg2
from psycopg2 import Error

connection = None

try:
    # Подключиться к существующей базе данных
    connection = psycopg2.connect(dbname='kpiltann', user='postgres',
                        password='KP_!2026', host='localhost')

    # Создайте курсор для выполнения операций с базой данных
    cursor = connection.cursor()

    cursor.callproc('pattern', ())
    row = cursor.fetchone()
    while row is not None:
        print(*row)
        row = cursor.fetchone()

    connection.commit()
    
    
    print("Таблица успешно создана в PostgreSQL")

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")