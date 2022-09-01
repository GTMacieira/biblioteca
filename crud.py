from msilib.schema import ControlEvent, Error
from multiprocessing import connection
#https://irias.com.br/blog/python-mysql-criando-um-crud-completo/

import mysql.connector
from mysql.connectot import Error
import datetime

#criar conexão com bancdo de dados 
def create_db_connection(host_name, user_name, user_password)
    connection = None
    try:
    connection = mysql.connector.connect(
        host = host_name,
        user = user_name,
        password = user_password,
        database = "biblioteca"
    )
    print(f"Olá, {user_name}, seja bem vindo!")
    except Error as err:
        print('Não foi possivel criar uma conexão com o banco de dados')
    
    return connection
        



