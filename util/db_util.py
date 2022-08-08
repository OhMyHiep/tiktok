import psycopg2
from util.config_parser import config


def getConnection():
    connection = psycopg2.connect(
    database=config["database"]["name"],
    user=config["database"]["user"],
    password=config["database"]["password"],
    host=config["database"]["host"],
    port=config["database"]["port"]
    )
    return connection

def executeSimpleQuery(sql,*args):
    connection=getConnection()
    result=executeQuery(connection,sql,*args)
    connection.commit()
    close(connection)
    return result


def executeQuery(connection,sql,*args):
    cursor = connection.cursor()
    try:
        cursor.execute(sql, (args))
        result = cursor.fetchall()
        return result
    except(psycopg2.DatabaseError) as error:
        print(error)
        connection.rollback()


def commit(connection):
    connection.commit()


def close(connection):
    if connection is not None:
        connection.close()