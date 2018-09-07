import psycopg2


def db_connection():
    
    con = psycopg2.connect(host="localhost", database="lite", user="postgres", password="postgres")
    cursor = con.cursor()
    """ call the routes in the database open connection """
    
    
    cursor.close()
    con.commit()
    con.close()

