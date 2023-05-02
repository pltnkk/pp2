import psycopg2

def delete_data(p_name):
    conn = None
    try:
        conn = psycopg2.connect(user="postgres",
                                    # пароль, который указали при установке PostgreSQL
                                    password="qwertyuiop",
                                    host="localhost",
                                    port="5432",
                                    database="pp2")

        # Создайте курсор для выполнения операций с базой данных
        cur = conn.cursor()
        cur.execute('call delete_data(%s)', (p_name, ))
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

delete_data('Val')