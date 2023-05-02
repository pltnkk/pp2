import psycopg2
from psycopg2 import Error

connection = None
def edit(r_id, r_name, r_number):
    try:
    # Подключиться к существующей базе данных
        connection = psycopg2.connect(dbname='kpiltann', user='postgres',
                        password='KP_!2026', host='localhost')

        # Создайте курсор для выполнения операций с базой данных
        

        cursor = connection.cursor()

        cursor.callproc('call edit(%s, %s, %s)', (r_id, r_name, r_number))

        
        connection.commit()
        print("Таблица успешно создана в PostgreSQL")

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")

edit(10, "Kobeisin", "87776665544")