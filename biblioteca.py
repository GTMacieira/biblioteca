from queue import PriorityQueue
from tkinter.tix import COLUMN
import crud

#menu
user_name = input('Entre com seu usuário:\n')
user_password = input('Entre com sua senha:\n')

connection = crud.create_db_connection( user_name, user_password, host_name= 'localhost', database = "biblioteca")
 
exit= False

print(f'BEM VINDO {user_name} !!! \n')
#"create table titles  (id int not null auto_increment primary key, title_name  varchar(100) not null, jp_title_name  varchar(100), author varchar(100), dig_physicist boolean not null, subject varchar(500));" 
while exit == False:
    print('\n')    
    print('MENU\nSelecione atraves dos números qual o tipo de operaçãos deseja realizar:\n')
    print(' 1 - Criar nova base de dados.\n 2 - Adicionar novo registro a base.\n 3 - Atualizar registro exitente.\n 4 - Remover registro.\n 5 - Sair\n')
    change = input('Qual o procedimento devemos realizar?\n')
    if change == '1':
        print('\n')
        db_name = input('Qual sera o nome de sua tabela?\n')
        columns = input("Quantas colunas terão sua tabela fora a coluna id?\n")
        column = 1
        db_structure = ""
        while column <= int(columns):
            col_name = input(f'Qual o nome da coluna {column} ?\n')
            data_type = input(f'Qual o tipo de dado da coluna {column} ?\n')
            data_size = input(f'Qual o tamanho do dado da culuna {column} ?\n')
            null = input(f'A coluna {column} pode ser nula?\n')
            if null == 'sim' or null == "SIM" or null == 'Sim':
                null = "NOT NULL"
            else:
                null = ""

            if column == 1 and columns == 1:
                append_db_structure = (f'CREATE TABLE {col_name} (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,{col_name } {data_type}({data_size}) {null})')
            elif column == 1:
                append_db_structure = (f'CREATE TABLE {col_name} (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,{col_name } {data_type}({data_size}) {null}),')
            elif column == columns:
                append_db_structure = (f'{data_type.upper}({data_size}) {null});')
            else:
                append_db_structure = (f'{data_type.upper}({data_size}) {null},')
            
            db_structure = db_structure + append_db_structure
            column += 1
        table = db_structure
        #print('Utilize o exemplo a baixo para a criação de uma nova base de dados\n')
        #print('create table users (id int not null auto_increment primary key, name varchar(100) not null, email varchar(100) not null, created datetime not null);')
        #table = input('Escreva estrutura da tabela:\n')
        print(table)
        crud.execute_query(connection, table, "CREATE")
    elif change == '2':
        print('\n\n')
    elif change == '3':
        print('\n\n')
    elif change == '4':
        print('\n\n')
    elif change == '5':
        exit = True
        print('\n\n')
        print(f'Até logo {user_name} !')
        