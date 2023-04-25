import psycopg2

conn = psycopg2.connect(dbname='users', user='postgres',
                        password='KP_!2026', host='localhost')

cur = conn.cursor()


table = '''
    CREATE TABLE PhoneBook(
    
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    phone VARCHAR(255) UNIQUE

    )
    '''



cur.execute(table)

conn.commit()


