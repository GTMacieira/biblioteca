from queue import PriorityQueue
#from crud import *

#menu
user_name = input('Entre com seu usuário:\n')
user_password = input('Entre com sua senha:\n')

#create_db_connection( user_name, user_password, host_name, database = "biblioteca")
 
exit= False

print(f'BEM VINDO {user_name} !!! \n')

while exit == False:
    print('\n\n')    
    print('MENU \n \nSelecione atraves dos números qual o tipo de operaçãos deseja realizar:\n')
    print(' 1 - Criar nova base de dados.\n 2 - Adicionar novo registro a base.\n 3 - Atualizar registro exitente.\n 4 - Remover registro.\n 5 - Sair\n\n')
    change = input('Qual o procedimento devemos realizar?\n')
    if change == '1':
        print('\n')
        print('Utilize o exemplo a baixo para a criação de uma nova base de dados\n')
        print('create table users (\nid int not null auto_increment primary key,\nname varchar(100) not null,\nemail varchar(100) not null,\ncreated datetime not null\n);')
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
        