data = [(111, 'Aliya', '87023981276'), (112, 'Dan', '87789127359'), (113, 'Val', '87778126349')]

import psycopg2

def insert_list(object):
    connection = None
    try:
        connection = psycopg2.connect(dbname='kpiltann', user='postgres',
                        password='KP_!2026', host='localhost')

        # Создайте курсор для выполнения операций с базой данных
        cur = connection.cursor()
        cur.executemany('call insert_list(%s, %s, %s)', object)
        connection.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if connection is not None:
            connection.close()
            
insert_list(data)