from configparser import ConfigParser

def config(section='postgresql'):
    parser = ConfigParser()
    parser.read(dbname='users', user='postgres',
                        password='KP_!2026', host='localhost')

    db = {}

    if parser.has_section(section):

        params = parser.items(section)

        for param in params:

            db[param[0]] = param[1]
    else:

        raise Exception("Error")
    
    return db
