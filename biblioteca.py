from datetime import datetime
from multiprocessing.util import abstract_sockets_supported
from queue import PriorityQueue
from select import select
from tkinter.tix import COLUMN
import crud

#menu
user = input('Entre com seu usuário:\n')

connection = crud.create_db_connection()
 
exit= False

print(f'BEM VINDO {user} !!! \n')

while exit == False:   
    print('MENU\nSelecione atraves dos números qual o tipo de operaçãos deseja realizar:\n')
    print(' 1 - Criar e excluir tabelas.\n 2 - Adicionar novo registro a tabela.\n 3 - Atualizar registro exitente.\n 4 - Remover registro.\n 5 - Sair\n')
    change = input('Qual o procedimento devemos realizar?\n')
    
    if change == '1':        
        insert_table = input ('como deseja incluir a tabela no banco de dados? \n 1 - Comando SQL\n 2 - Modo interativo\n')
        if insert_table == '1':
            db_structure = input ('Entre com o comando SQL:\n')
            query_type = input('Qual ação vamos ralizar? \n1 - Criar \n2 - Excluir\n')

            if query_type == '1':
                query_type = 'CREATE'
            elif query_type == '2':
                query_type = 'DROP'

        elif insert_table == '2':  
            query_type = 'CREATE'          
            create_drop = input('Qual ação vamos ralizar? \n1 - Criar \n2 - Excluir\n' )  

            if create_drop == "1":
                db_name = input('Qual será o nome de sua tabela?\n')
                columns = input("Quantas colunas terão sua tabela fora a coluna id?\n")
                column = 1
                db_structure = ""
                
                while column <= int(columns):
                    col_name = input(f'Qual o nome da coluna {column} ?\n')
                    data_type = input(f'Qual o tipo de dado da coluna {column} ? INT, BOOLEAN, VARCHAR, DATE\n')
                    if data_type == "VARCHAR":
                        data_size = input(f'Qual o tamanho do dado da culuna {column} ?\n')
                        data_size = (f'({data_size})')
                    else:
                        data_size = ""
                    null = input(f'A coluna {column} pode ser nula?\n')
                    if null == 'Não' or null == "não" or null == 'Não':
                        null = "NOT NULL"
                    else:
                        null = "NULL"

                    if column == 1 and int(columns) == 1:
                        append_db_structure = (f'CREATE TABLE {db_name} (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,{col_name } {data_type}{data_size} {null})')
                    elif column == 1:
                        append_db_structure = (f'CREATE TABLE {db_name} (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,{col_name } {data_type}{data_size} {null}, ')
                    elif column == int(columns):
                        append_db_structure = (f'{col_name} {data_type}{data_size} {null});')
                    else:
                        append_db_structure = (f'{col_name} {data_type}{data_size} {null}, ')
                    
                    db_structure = db_structure + append_db_structure
                    column += 1
            elif create_drop == "2":
                query_type = 'DROP'
                db_name = input('Qual tabela deseja excluir?\n')
                db_structure = (f'DROP TABLE {db_name};') 

        action = db_structure

    elif change == '2':
        print('\n')
        query_type = 'INSERT'
        insert_table = input ('como deseja incluir a tabela no banco de dados? \n 1 - Comando SQL\n 2 - Modo interativo\n')
        if insert_table == '1':
            db_structure = input ('Entre com o comando SQL:\n')
        elif insert_table == '2':
            title_name = input('Qula o titulo da obra?')
            original_name = input('Qual o titulo da obra na lingua de publicação')
            author = input('Qual o autor desta obra?')
            dig_phy = input('Eata obra é fisica?')
            abstract = input('Conte um poco sobre esta obra:')
            released_chaps = input('Quantos capitulos foram lançados desta obra?')
            acquis_chaps = input ('Quantos capitulos você tem ?')
            acquis_date = input ('Quando adquiriu este capitulo?')
            register= datetime.datetime.today()

            #action = (f"INSERT INTO `titles`(`title_name`, `original_name`, `author`, `dig_phy`, `abstract`, `released_chap´s`, \
           #  `acquis_chap´s`, `acquis_date`, `register`) VALUES ('[value-1]','[value-2]','[value-3]','[value-4]','[value-5]','[value-6]','[value-7]','[value-8]','[value-9]')")
    elif change == '3':
        print('\n\n')
    elif change == '4':
        print('\n\n')
    elif change == '5':
        exit = True
        print('\n\n')
        print(f'Até logo {user} !')

    crud.execute_query(connection, action, query_type)
        