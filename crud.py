from msilib.schema import ControlEvent, Error
from multiprocessing import connection
from tkinter import INSERT
#https://irias.com.br/blog/python-mysql-criando-um-crud-completo/

import mysql.connector
from mysql.connector import Error
import datetime
import sys
from colorama import Fore
from colorama import Style
from functions import *

#criar conexão com bancdo de dados diretamente na banco de dados biblioteca
def create_db_connection(user_name = 'root' ,host_name = 'localhost', database = 'biblioteca', port = 3306):
    connection = None
    try:
        connection = mysql.connector.connect(
        host = host_name,
        user = user_name,
        #password = user_password,
        database = database,
        port =  port
        )
    except Error as err:
        print(Fore.LIGHTGREEN_EX + f'Não foi possivel criar uma conexão com o banco de dados, iformado erro: {err} \n\n' + Style.RESET_ALL)
        sys.exit()
    
    return connection
        

def execute_query(connection,query, query_type):
    cursor = connection.cursor()
    try:
        if query_type == "INSERT" or query_type == "DELETE" or query_type == "UPDATE":
            cursor.execute(query)
            connection.commit()
            print(Fore.GREEN+f"Alteração {query_type} realizada com sucesso!"+ Style.RESET_ALL)
        elif query_type == "READ":
            cursor.execute(query)
            results = cursor.fetchall()
            for result in results:
                print(result)
            input('Preesione qualquer tecla para continuar')
            cls_term()
        elif query_type == 'CREATE': 
            cursor.execute(query)
            print(Fore.GREEN+"Base de dados criada"+ Style.RESET_ALL)
        elif query_type == 'DROP':
            cursor.execute(query)
            print(Fore.GREEN+"Base de dados excluida"+ Style.RESET_ALL)        

    except Error as err:
        print(Fore.RED + f'Não foi possível executar a ação, iformado erro: {err}' + Style.RESET_ALL) 
        cursor.close()
        connection.close()
        cls_term
        pass
               
    cursor.close()
    #connection.close()
    



