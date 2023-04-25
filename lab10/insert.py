import psycopg2
from config import config

def insert_number(name, phone_number):
    sql = """
    INSERT INTO phonebook(name, phone_number)
    VALUES(%s, %s);
    """

    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (name, phone_number))
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

insert_number('Mum', '87770532777')
insert_number('Dad', '87779692000')