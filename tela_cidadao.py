import sqlite3
import getpass # Utilizado na função 'getpass()'
import sys # Utilizado na função 'getpass()'

# Cria uma conexão com o banco de dados
conexao_DB = sqlite3.connect('DB_SUI.db')

# Cria um cursor para executar comandos SQL
cursor = conexao_DB.cursor()

def menu_cidadao():
    while True:
        opcao = input("""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
|__________ LOGIN DO CIDADÃO ___________|
|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|
|                                       |
|   [0] ...................... VOLTAR   |
|   [1] .......... Cidadão cadastrado   |
|   [2] ........ Cidadão sem cadastro   |
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

>>> Escolha a opção: """)
        
        if opcao == "0":
            print("\n - VOLTANDO - \n")
            break
        elif opcao == "1":
            cidadao_cadastrado()
        elif opcao == "2":
            menu_cadastro_cidadao()
        else:
            print("\n - OPÇÃO INVÁLIDA - \n")

def cidadao_cadastrado():
    email_cidadao = input(" Digite seu email: ")

    while email_cidadao == "":
        print("\n - INFORME UM EMAIL - \n")
        email_cidadao = input(" Digite seu email: ")
    
    cursor.execute(" SELECT email_usuario FROM usuarios WHERE categoria_usuario = 'Cidadão' AND email_usuario = ? ", (email_cidadao,))
    verifica_email = cursor.fetchone()
    
    if verifica_email == None:
        print("\n - EMAIL CIDADÃO INEXISTENTE - \n")
        menu_cidadao()
    else:
        senha_cidadao = getpass_with_mask(" Digite sua senha: ")
        while senha_cidadao == "":
            print("\n - INFORME UMA SENHA - \n")
            senha_cidadao = getpass_with_mask(" Digite sua senha: ")
        
        cursor.execute(" SELECT senha_usuario FROM usuarios WHERE categoria_usuario = 'Cidadão' AND email_usuario = ? AND senha_usuario = ? ", (email_cidadao, senha_cidadao,))
        verifica_senha = cursor.fetchone()
        
        if verifica_senha == None:
            print("\n - SENHA INVÁLIDA - \n")
            menu_cidadao()
        else:
            cursor.execute(" SELECT nome_usuario FROM usuarios WHERE categoria_usuario = 'Cidadão' AND email_usuario = ? AND senha_usuario = ? ", (email_cidadao, senha_cidadao,))
            nome_cidadao = cursor.fetchone()

            cursor.execute(" SELECT id_usuario FROM usuarios WHERE categoria_usuario = 'Cidadão' AND email_usuario = ? AND senha_usuario = ? ", (email_cidadao, senha_cidadao,))
            id_cidadao = cursor.fetchone()
            print(f"""
        =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        |    - SEJA BEM-VINDO À SUI - Soluções Urbanas Integradas !!! -    |
        |__________________________________________________________________|
        |                                        
        |      CIDADÃO LOGADO COMO > {nome_cidadao[0]} <
        |      >>> SEU ID:  {id_cidadao[0]}
        =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        
        """)

def menu_cadastro_cidadao():
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
            cadastrar_cidadao()
        elif opcao == "2":
            menu_cidadao()
        else:
            print(" - OPÇÃO INVÁLIDA - ")

def cadastrar_cidadao():
    while True:
        nome_cidadao = input(" Digite seu nome: ").upper()
        while nome_cidadao == "":
            print("\n - INFORME UM NOME - \n")
            nome_cidadao = input(" Digite seu nome: ").upper()

        data_nascimento_cidadao = input(" Digite sua data de nascimento no formato dd/mm/aaaa: ")
        while data_nascimento_cidadao == "":
            print("\n - INFORME UMA DATA - \n")
            data_nascimento_cidadao = input(" Digite sua data de nascimento no formato dd/mm/aaaa: ")

        cpf_cidadao = input(" Digite seu CPF no formato 000.000.000-00: ")
        while cpf_cidadao == "":
            print("\n - INFORME UM CPF - \n")
            cpf_cidadao = input(" Digite seu CPF no formato 000.000.000-00: ")

        telefone_cidadao = input(" Digite seu telefone no formato (00)00000-0000: ")
        while telefone_cidadao == "":
            print("\n - INFORME UM TELEFONE - \n")
            telefone_cidadao = input(" Digite seu telefone no formato (00)00000-0000: ")

        email_cidadao = input(" Digite seu email: ")
        while email_cidadao == "":
            print("\n - INFORME UM EMAIL - \n")
            email_cidadao = input(" Digite seu email: ")

        senha_cidadao = getpass_with_mask(" Digite sua senha: ")
        while senha_cidadao == "":
            print("\n - INFORME UMA SENHA - \n")
            senha_cidadao = getpass_with_mask(" Digite sua senha: ")

        confirma_senha_cidadao = getpass_with_mask(" Confirme sua senha: ")
        while senha_cidadao != confirma_senha_cidadao:
            print("\n - AS SENHAS FORNECIDAS NÃO CORRESPONDEM - \n")
            confirma_senha_cidadao = getpass_with_mask(" Confirme sua senha: ")

        cursor.execute(""" INSERT INTO usuarios (categoria_usuario, cpf_usuario, data_nascimento_usuario, email_usuario, nome_usuario, senha_usuario, telefone_usuario) VALUES ('Cidadão',?,?,?,?,?,?) """, (cpf_cidadao, data_nascimento_cidadao, email_cidadao, nome_cidadao, senha_cidadao, telefone_cidadao,))
        conexao_DB.commit()

        print(f"\n - CIDADÃO > {nome_cidadao} < CADASTRADO COM SUCESSO - \n")

def getpass_with_mask(prompt):
    # Exibe " * " quando o usuário digita sua senha
    password = ""
    print(prompt, end='', flush=True)
    while True:
        char = None
        if sys.platform == 'win32':
            import msvcrt
            char = msvcrt.getwch()
        else:
            import termios
            import tty
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(fd)
                char = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        if char == '\r' or char == '\n':
            print('')
            break
        elif char == '\b' or ord(char) == 127:  # Handle backspace
            if password:
                password = password[:-1]
                print('\b \b', end='', flush=True)
        else:
            password += char
            print('*', end='', flush=True)
    return password

if __name__ == "__main__":
    menu_cidadao()
