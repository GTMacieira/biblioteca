from msilib.schema import ControlEvent, Error
from multiprocessing import connection
from tkinter import INSERT
#https://irias.com.br/blog/python-mysql-criando-um-crud-completo/

import mysql.connector
from mysql.connectot import Error
import datetime


#criar conexão com bancdo de dados diretamente na banco de dados biblioteca
def create_db_connection( user_name, user_password,host_name = 'localhost', database = 'biblioteca'):
    connection = None
    try:
    connection = mysql.connector.connect(
        host = host_name,
        user = user_name,
        password = user_password,
        database = database
    )
    print(f"Olá, {user_name}, seja bem vindo!")
    except Error as err:
        print('Não foi possivel criar uma conexão com o banco de dados, iformado erro: {err}')
    
    return connection
        
def execute_query(connection,query,query_type):
    cursor = connection.cursor
    try:
        if query_type == "INSERT" or query_type == "DELETE" or query_type == "UPDATE":
            cursor.execute(query)
            results = cursor.commit
            print(f"Alteração {query_type} realizada com sucesso!")
        elif query_type == "READ":
            cursor.execute(query)
            results = cursor.fatchall
        else: #CREATE
            cursor.execute(query)
            print("Base de dados criada")
            
    except Error as err:
        print(f'Não foi possível executar a ação, iformado erro: {err}') 
               
    cursor.close()
    connection.close()
    



