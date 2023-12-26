import sqlite3
from seguranca import getpass_with_mask

# Cria uma conexão com o banco de dados
conexao_DB = sqlite3.connect('DB_SUI.db')

# Cria um cursor para executar comandos SQL
cursor = conexao_DB.cursor()

def menu_administrador():
    while True:
        opcao = input("""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
|________ LOGIN DO ADMINISTRADOR ________|
|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|
|                                        |
|   [0] ....................... VOLTAR   |
|   [1] .................. Fazer login   |
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

>>> Escolha a opção: """)
        
        if opcao == "0":
            print("\n - VOLTANDO - \n")
            break
        elif opcao == "1":
            login_administrador()
        else:
            print("\n - OPÇÃO INVÁLIDA - \n")

def login_administrador():
    email_administrador = input(" Digite seu email: ")
    while email_administrador == "":
        print("\n - INFORME UM EMAIL - \n")
        email_administrador = input(" Digite seu email: ")
    
    cursor.execute(" SELECT email_usuario FROM usuarios WHERE categoria_usuario = 'Administrador' AND email_usuario = ? ", (email_administrador,))
    verifica_email = cursor.fetchone()
    
    if verifica_email == None:
        print("\n - EMAIL ADMINISTRADOR INEXISTENTE - \n")
        menu_administrador()
    else:
        senha_administrador = getpass_with_mask(" Digite sua senha: ")
        while senha_administrador == "":
            print("\n - INFORME UMA SENHA - \n")
            senha_administrador = getpass_with_mask(" Digite sua senha: ")
        
        cursor.execute(" SELECT senha_usuario FROM usuarios WHERE categoria_usuario = 'Administrador' AND email_usuario = ? AND senha_usuario = ? ", (email_administrador, senha_administrador,))
        verifica_senha = cursor.fetchone()
        
        if verifica_senha == None:
            print("\n - SENHA INVÁLIDA - \n")
            menu_administrador()
        else:
            cursor.execute(" SELECT nome_usuario FROM usuarios WHERE categoria_usuario = 'Administrador' AND email_usuario = ? AND senha_usuario = ? ", (email_administrador, senha_administrador,))
            nome_administrador = cursor.fetchone()

            cursor.execute(" SELECT id_usuario FROM usuarios WHERE categoria_usuario = 'Administrador' AND email_usuario = ? AND senha_usuario = ? ", (email_administrador, senha_administrador,))
            id_administrador = cursor.fetchone()
            print(f"""
        =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        |    - SEJA BEM-VINDO À SUI - Soluções Urbanas Integradas !!! -    |
        |__________________________________________________________________|
        |                                        
        |      ADMINISTRADOR LOGADO COMO > {nome_administrador[0]} <
        |      >>> SEU ID:  {id_administrador[0]}
        =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        
        """)

if __name__ == "__main__":
    menu_administrador()
