from datetime import datetime
import imp
from multiprocessing.util import abstract_sockets_supported
from queue import PriorityQueue
from select import select
from this import d
from tkinter.tix import COLUMN
import crud
import sys
from functions import cls_term
from colorama import Fore
from colorama import Style

#menu
cls_term()
user = input('Entre com seu usuário:\n')
cls_term()
connection = crud.create_db_connection()
 
exit= False

print(f'BEM VINDO {user} !!! \n')

while exit == False:   
    print('MENU\nSelecione através dos números qual o tipo de operação deseja realizar:\n')
    print(Fore.YELLOW+' 1 - Criar e excluir tabelas.\n 2 - Adicionar novo registro a tabela.\n 3 - Atualizar registro exitente.\n 4 - Remover registro.\n 5 - Exibir tabela.\n 6 - Sair' + Style.RESET_ALL)
    print('\n')
    change = input('Qual o procedimento devemos realizar?\n')
    cls_term()
    
    if change == '1':        
        insert_table = input (Fore.YELLOW+'Como deseja incluir ou excluir a tabela no banco de dados? \n 1 - Comando SQL\n 2 - Modo interativo\n'+ Style.RESET_ALL)
        if insert_table == '1':
            print('\n')
            db_structure = input ('Entre com o comando SQL:\n')
            print('\n')
            query_type = input(Fore.YELLOW+'Qual ação vamos ralizar? \n1 - Criar \n2 - Excluir\n'+ Style.RESET_ALL)
            print('\n')
            if query_type == '1':
                query_type = 'CREATE'
            elif query_type == '2':
                query_type = 'DROP'
            cls_term()
        elif insert_table == '2':  
            query_type = 'CREATE'          
            create_drop = input(Fore.YELLOW+'Qual ação vamos ralizar? \n1 - Criar \n2 - Excluir\n'+ Style.RESET_ALL )  

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

    #INSERT INTO `titles`(`title_name`, `original_name`, `author`, `dig_phy`, `abstract`, `acquis_date`, `released_chapters`, `acquis_chap´s`) VALUES ('Goblin Slayer','ゴブリンスレイヤー','Kagyuu Kumo','0','Um homem deseja tornar-se um "aventureiro", cujo lema é: "Eu não vou salvar o mundo, eu apenas vou matar goblins." Após ouvir rumores sobre ele, uma elfa se aproxima dele com um pedido.','15-03-1994',75,10);
    elif change == '2':
        print('\n')
        query_type = 'INSERT'
        insert_table = input (Fore.YELLOW+'Como deseja incluir a tabela no banco de dados? \n 1 - Comando SQL\n 2 - Modo interativo\n'+ Style.RESET_ALL)
        if insert_table == '1':
            action = input ('Entre com o comando SQL:\n')
            print(action)
        elif insert_table == '2':
            title_name = input('Qual o título da obra?\n')
            original_name = input('\nQual o título da obra na língua de publicação?\n')
            author = input('\nQual o autor desta obra?\n')
            dig_phy = input('\nA obra está em formato físico?\n')
            abstract = input('\nConte um poco sobre esta obra:\n')
            released_chaps = int(input('\nQuantos capítulos foram lançados desta obra?\n'))
            acquis_chaps = int(input ('\nQuantos capítulos você tem ?\n'))                   
            acquis_date = input ('\nQuando adquiriu este capítulo?\n')
            user = user
            register= datetime.now()
            cls_term()

            action = (f"INSERT INTO `titles`(`title_name`, `original_name`, `author`, `dig_phy`, `abstract`, `released_chaps`,`acquis_chaps`, `acquis_date`, `user`, `register`)VALUES ('{title_name}','{original_name}','{author}','{dig_phy}','{abstract}',{released_chaps},{acquis_chaps},'{acquis_date}','{user}','{register}')")
    
    #UPDATE `titles` SET `original_name`='[value-3]' WHERE title_name='value-2';
    elif change == '3':
        print('\n')
        query_type = 'UPDATE'
        insert_table = input (Fore.YELLOW+'Como deseja alterar a tabela no banco de dados? \n 1 - Comando SQL\n 2 - Modo interativo\n'+ Style.RESET_ALL)
        cls_term
        if insert_table == '1':
            action = input ('Entre com o comando SQL:\n')
        elif insert_table == '2':
            db_name = input('Qual o nome da tabela\n')
            title_name = input('Qual o título que devemos realizar a altereção?\n')
            column_Update= input(Fore.YELLOW+'Qual a o campo sará alterado?\n 1 - Título\n 2 - Nome original\n 3 - Autor\n 4 - Digital ou fisíco\n 5 - Resumo \n 6 - Data de aquisição \n 7 - Capitulos lançados \n 8 - Capitulos adquiridos\n'+ Style.RESET_ALL) 
            cls_term
            if column_Update == '1':
                column_Update= 'title_name'
            elif column_Update == '2':
                column_Update= 'original_name'
            elif column_Update == '3':
                column_Update= 'author'
            elif column_Update == '4':
                column_Update= 'dig_phy'
            elif column_Update == '5':
                column_Update= 'abstract'
            elif column_Update == '6':
                column_Update= 'acquis_date'
            elif column_Update == '7':
                column_Update= 'released_chaps'
            elif column_Update == '8':
                column_Update= "acquis_chaps"
            
            new_date = input('Qual novo valor do campo?\n')
            cls_term
            action = (f"UPDATE {db_name} SET {column_Update}='{new_date}' WHERE title_name='{title_name}'")
    
    #DELETE FROM users WHERE id = %s
    elif change == '4':
        print('\n')
        query_type = 'DELETE'
        insert_table = input (Fore.YELLOW+'como deseja excluir dados da tabela? \n 1 - Comando SQL\n 2 - Modo interativo\n'+ Style.RESET_ALL)
        if insert_table == '1':
            action = input ('Entre com o comando SQL:\n')
            print(action)
        elif insert_table == '2':
            db_name = input('Qual o nome da tabela\n')
            title_name = input('Qual o titulo que devemos excluir')               
            action = (f"DELETE FROM {db_name} WHERE title_name = '{title_name}'")

    elif change == '5':
        query_type = 'READ'
        action = 'SELECT * FROM titles'
        
    elif change == '6':
        exit = True
        cls_term()
        print(f'Até logo {user} !')
        sys.exit()

    crud.execute_query(connection, action, query_type)
        