import psycopg2
from config import config

def delete_user(user_id):
    sql = """
    delete from phonebook
    where user_id = %s;
    """

    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (user_id))
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

delete_user('3')