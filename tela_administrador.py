import sqlite3
from seguranca import getpass_with_mask

# Cria uma conexão com o banco de dados
conexao_DB = sqlite3.connect('DB_SUI.db')

# Cria um cursor para executar comandos SQL
cursor = conexao_DB.cursor()

def menu_administrador():
    while True:
        opcao = input("""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
|__________ LOGIN DO ADMINISTRADOR ___________|
|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|
|                                             |
|   [0] ............................ VOLTAR   |
|   [1] .......... Administrador cadastrado   |
|   [2] ........ Administrador sem cadastro   |
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

>>> Escolha a opção: """)
        
        if opcao == "0":
            print("\n - VOLTANDO - \n")
            break
        elif opcao == "1":
            administrador_cadastrado()
        elif opcao == "2":
            menu_cadastro_administrador()
        else:
            print("\n - OPÇÃO INVÁLIDA - \n")

def administrador_cadastrado():
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

def menu_cadastro_administrador():
    while True:
        opcao = input("""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
|____ DESEJA REALIZAR SEU CADASTRO? ____|
|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|
|   [1] ......................... Sim   |
|   [2] ......................... Não   |
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

>>> Escolha a opção: """)
        if opcao == "1":
            cadastrar_administrador()
        elif opcao == "2":
            menu_administrador()
        else:
            print(" - OPÇÃO INVÁLIDA - ")

def cadastrar_administrador():
    while True:
        nome_administrador = input(" Digite seu nome: ").upper()
        while nome_administrador == "":
            print("\n - INFORME UM NOME - \n")
            nome_administrador = input(" Digite seu nome: ").upper()

        data_nascimento_administrador = input(" Digite sua data de nascimento no formato dd/mm/aaaa: ")
        while data_nascimento_administrador == "":
            print("\n - INFORME UMA DATA - \n")
            data_nascimento_administrador = input(" Digite sua data de nascimento no formato dd/mm/aaaa: ")

        cpf_administrador = input(" Digite seu CPF no formato 000.000.000-00: ")
        while cpf_administrador == "":
            print("\n - INFORME UM CPF - \n")
            cpf_administrador = input(" Digite seu CPF no formato 000.000.000-00: ")

        telefone_administrador = input(" Digite seu telefone no formato (00)00000-0000: ")
        while telefone_administrador == "":
            print("\n - INFORME UM TELEFONE - \n")
            telefone_administrador = input(" Digite seu telefone no formato (00)00000-0000: ")

        email_administrador = input(" Digite seu email: ")
        while email_administrador == "":
            print("\n - INFORME UM EMAIL - \n")
            email_administrador = input(" Digite seu email: ")

        senha_administrador = getpass_with_mask(" Digite sua senha: ")
        while senha_administrador == "":
            print("\n - INFORME UMA SENHA - \n")
            senha_administrador = getpass_with_mask(" Digite sua senha: ")

        confirma_senha_administrador = getpass_with_mask(" Confirme sua senha: ")
        while senha_administrador != confirma_senha_administrador:
            print("\n - AS SENHAS FORNECIDAS NÃO CORRESPONDEM - \n")
            confirma_senha_administrador = getpass_with_mask(" Confirme sua senha: ")

        cursor.execute(""" INSERT INTO usuarios (categoria_usuario, cpf_usuario, data_nascimento_usuario, email_usuario, nome_usuario, senha_usuario, telefone_usuario) VALUES ('Administrador',?,?,?,?,?,?) """, (cpf_administrador, data_nascimento_administrador, email_administrador, nome_administrador, senha_administrador, telefone_administrador,))
        conexao_DB.commit()

        print(f"\n - ADMINISTRADOR > {nome_administrador} < CADASTRADO COM SUCESSO - \n")
        menu_administrador()

if __name__ == "__main__":
    menu_administrador()
