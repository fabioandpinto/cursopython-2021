"""
CRUD - PosgreSQL
paquete psycopg2 para conectarnos
"""
import psycopg2

def get_connection():
    con = psycopg2.connect(
        host = '127.0.0.1',
        port = '5432',
        database = 'pyPost',
        user='postgres',
        password='F.123abio')
    return con

def close_connection(connection):
    if connection:
        connection.close()

# Select * from peliculas
def get_peliculas():
    try:
        con = get_connection()
        cursor = con.cursor()
        query = "select * from peliculas order by idpeli"
        cursor.execute(query)
        results = cursor.fetchall()
        close_connection(con)
    except(Exception, psycopg2.Error) as er:
        print(er)
    return results

def get_by_name(gender):
    try:
        con = get_connection()
        cursor = con.cursor()
        query = "select * from peliculas where genderpeli=%s order by namepeli"
        cursor.execute(query, (gender,))
        results = cursor.fetchall()
        close_connection(con)
    except(Exception, psycopg2.Error) as er:
        print(er)
    return results

def get_by_name(name):
    try:
        con = get_connection()
        cursor = con.cursor()
        query = "select * from peliculas where namepeli=%s order by namepeli"
        cursor.execute(query, (name,))
        results = cursor.fetchall()
        close_connection(con)
    except(Exception, psycopg2.Error) as er:
        print(er)
    return results

# insert
def add_pelicula(id, name, gender):
    try:
        con = get_connection()
        cursor = con.cursor()
        query = "insert into peliculas(idpeli, namepeli, genderpeli) values (%s,%s,%s)"
        cursor.execute(query, (id, name, gender))
        con.commit()
        close_connection(con)
    except(Exception, psycopg2.Error) as error:
        pass
    return "Inserted"

# update
def update_name(id, name):
    try:
        con = get_connection()
        cursor = con.cursor()
        query = "update peliculas set namepeli = %s where idpeli = %s"
        cursor.execute(query, (name, id))
        con.commit()
        close_connection(con)
    except(Exception, psycopg2.Error) as error:
        pass
    return "Updated"

#delete
def delete_pelicula(id):
    try:
        con = get_connection()
        cursor = con.cursor()
        query = "delete from peliculas where idpeli = %s"
        cursor.execute(query, (id,))
        con.commit()
        close_connection(con)
    except(Exception, psycopg2.Error) as error:
        pass
    return print("Deleted")





