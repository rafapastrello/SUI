import sqlite3

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
            print(" - VOLTANDO - ")
            break
        elif opcao == "1":
            cidadao_cadastrado()
        elif opcao == "2":
            menu_cadastro_cidadao()
        else:
            print(" - OPÇÃO INVÁLIDA - ")

def cidadao_cadastrado():
    while True:
        email_cidadao = input(" Digite seu email: ")
        
        cursor.execute(" SELECT email_usuario FROM usuarios WHERE categoria_usuario = 'Cidadão' AND email_usuario = ? ", (email_cidadao,))
        verifica_email = cursor.fetchone()
        
        if verifica_email == None:
            print(" - EMAIL CIDADÃO INEXISTENTE - ")
            menu_cidadao()
        else:
            senha_cidadao = input(" Digite sua senha: ")
            
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
            =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
            | - SEJA BEM-VINDO À SUI - Soluções Urbanas Integradas !!! - |
            |____________________________________________________________|
            |                                                            
            |      CIDADÃO LOGADO COMO > {nome_cidadao[0]} <
            |      SEU ID: > {id_cidadao[0]} <
            =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
            
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
        pass

if __name__ == "__main__":
    menu_cidadao()
