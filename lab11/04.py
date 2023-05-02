import psycopg2

def getrows(pagenumber, pagesize):
    conn = None
    try:
        conn = psycopg2.connect(dbname='kpiltann', user='postgres',
                        password='KP_!2026', host='localhost')
        cur = conn.cursor()

        cur.execute('select * from getrows(%s, %s)', (pagenumber, pagesize))

        conn.commit()

        cur.close()

    except Exception as e:

        print(str(e))

    finally:
        if conn is not None:
            conn.close()

getrows(1, 2)