import sqlite3

# Cria uma conexão com o banco de dados
conexao_DB = sqlite3.connect('DB_SUI.db')

# Cria um cursor para executar comandos SQL
cursor = conexao_DB.cursor()

def menu_instituicoes():
    while True:
        opcao = input("""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
|_____________________ INSTITUIÇÕES _____________________|
|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|
|                                                        |
|   [0] ....................................... VOLTAR   |
|                                                        |
|   [1] ....... Visualizar as instituições disponíveis   |
|   [2] ....................... Visualizar os contatos   |
|   [3] ..................... Visualizar as descrições   |
|   [4] ........................... Editar instituição   |
|   [5] .......................... Inserir instituição   |
|   [6] ........................... Buscar instituição   |
|   [7] .......................... Excluir instituição   |
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

>>> Escolha a opção: """)
        if opcao  == "0":
            print("\n - VOLTANDO - \n")
            break
        elif opcao == "1":
            instituicoes_disponiveis()
        elif opcao == "2":
            contatos_instituicoes()
        elif opcao == "3":
            descricoes_instituicoes()
        elif opcao == "4":
            edita_instituicao()
        elif opcao == "5":
            insere_instituicao()
        elif opcao == "6":
            busca_instituicao()
        elif opcao == "7":
            exclui_instituicao()
        else:
            print("\n - OPÇÃO INVÁLIDA - \n")

def obtem_instituicoes(): # Obtem as instituicoes em lista
    instituicoes = []

    # Obtem os valores da tabela instituicoes
    cursor.execute(""" SELECT * FROM instituicoes """)
    valores = cursor.fetchall() # Lista de tuplas

    for valor in valores:
        instituicao = list(valor) # Transforma cada tupla em lista
        instituicoes.append(instituicao) # Agrupa as listas em uma única lista

    return instituicoes

def instituicoes_disponiveis(): # Visualiza o ID e o nome das instituições disponíveis
    lista_instituicoes = obtem_instituicoes()
    
    # Exibe a tabela estilizada
    print("\n - INSTITUIÇÕES DISPONÍVEIS -")
    print(f"{'=-'*30}")
    print(f"| {'ID':<3} | {'NOME':<50} |")
    print(f"|{'='*5}|{'='*52}|")
    
    for instituicao in lista_instituicoes:
        print(f"| {instituicao[0]:<3} | {instituicao[3]:<50} |")
        print(f"|{'-'*5}|{'-'*52}|")
    print(f"{'=-'*30}\n")

def contatos_instituicoes(): # Visualiza os contatos de cada institiução
    lista_instituicoes = obtem_instituicoes()

    # Exibe a tabela estilizada
    print("\n - INSTITUIÇÕES DISPONÍVEIS (CONTATOS) -")
    print(f"{'=-'*55}")
    print(f"| {'ID':<3} | {'NOME':<30} | {'EMAIL':<45} | {'TELEFONE':<19} |")
    print(f"|{'='*5}|{'='*32}|{'='*47}|{'='*21}|")

    for instituicao in lista_instituicoes:
        print(f"| {instituicao[0]:<3} | {instituicao[3]:<30} | {instituicao[2]:<45} | {instituicao[4]:19} |")
        print(f"|{'-'*5}|{'-'*32}|{'-'*47}|{'-'*21}|")
    print(f"{'=-'*55}\n")

def descricoes_instituicoes(): # Visualiza a descrição de cada institiução
    lista_instituicoes = obtem_instituicoes()

    # Exibe a tabela estilizada
    print("\n - INSTITUIÇÕES DISPONÍVEIS (DESCRIÇÕES) -")
    print(f"{'=-'*82}")
    print(f"| {'ID':<3} | {'NOME':<30} | {'DESCRIÇÃO':<121} |")
    print(f"|{'='*5}|{'='*32}|{'='*123}|")
    
    for instituicao in lista_instituicoes:
        print(f"| {instituicao[0]:<3} | {instituicao[3]:<30} | {instituicao[1]:121} |")
        print(f"|{'-'*5}|{'-'*32}|{'-'*123}|")
    print(f"{'=-'*82}\n")

def visualiza_instituicao_selecionada(id_instituicao):
    instituicoes = [] # Obtem as instituicoes em lista
    cursor.execute(" SELECT * FROM instituicoes WHERE id_instituicao = ? ", (id_instituicao,)) # Obtem os valores da tabela instituicoes
    valores = cursor.fetchall() # Lista de tuplas
    for valor in valores:
        instituicao = list(valor) # Transforma cada tupla em lista
        instituicoes.append(instituicao) # Agrupa as listas em uma única lista

    # Exibe a tabela estilizada
    print("\n - INSTITUIÇÃO SELECIONADA -")
    print(f"{'=-'*82}")
    print(f"| {'ID':<3} | {'NOME':<30} | {'DESCRIÇÃO':<121} |")
    print(f"|{'='*5}|{'='*32}|{'='*123}|")
    
    for instituicao in instituicoes:
        print(f"| {instituicao[0]:<3} | {instituicao[3]:<30} | {instituicao[1]:121} |")
        print(f"|{'-'*5}|{'-'*32}|{'-'*123}|")
    print(f"{'=-'*82}\n")

def edita_instituicao():
    while True:
        print("\n - EDITAR INSTITUIÇÃO - \n")
        id_instituicao = input(" Digite o ID da instituição que deseja editar: ")
        while id_instituicao == "":
            print("\n - INFORME UM ID - \n")
            id_instituicao = input(" Digite o ID da instituição que deseja editar: ")
        
        # Verifica se o ID informado é existente no DB
        cursor.execute(" SELECT id_instituicao FROM instituicoes WHERE id_instituicao = ? ", (id_instituicao,))
        verifica_instituicao = cursor.fetchall()
        
        if not verifica_instituicao:
            print("\n - INSTITUIÇÃO INEXISTENTE - \n")
            menu_instituicoes()
        else:
            visualiza_instituicao_selecionada(id_instituicao)
            opcao = input(f"""
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    |___________ EDITAR INSTITUIÇÃO {id_instituicao:<3} ___________|
    |-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|
    |                                              |
    |   [0] ............................. VOLTAR   |
    |                                              |
    |   [1] ................... Editar descrição   |
    |   [2] ....................... Editar email   |
    |   [3] ........................ Editar nome   |
    |   [4] .................... Editar telefone   |
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

    >>> Escolha a opção: """)
            if opcao  == "0":
                print("\n - VOLTANDO - \n")
                break
            elif opcao == "1":
                nova_descricao_instituicao = input(f" Digite a nova descrição da instituição {id_instituicao}: ").upper()
                while nova_descricao_instituicao == '':
                    print("\n - INFORME UMA DESCRIÇÃO - \n")
                    nova_descricao_instituicao = input(f" Digite a nova descrição da instituição {id_instituicao}: ").upper()
                cursor.execute(" UPDATE instituicoes SET descricao_instituicao = ? WHERE id_instituicao = ? ", (nova_descricao_instituicao,id_instituicao,))
                conexao_DB.commit()
                print("\n - DESCRIÇÃO EDITADA - \n")

            elif opcao == "2":
                novo_email_instituicao = input(f" Digite o novo email da instituição {id_instituicao}: ")
                while novo_email_instituicao == '':
                    print("\n - INFORME UM EMAIL - \n")
                    novo_email_instituicao = input(f" Digite o novo email da instituição {id_instituicao}: ")
                cursor.execute(" UPDATE instituicoes SET email_instituicao = ? WHERE id_instituicao = ? ", (novo_email_instituicao,id_instituicao,))
                conexao_DB.commit()
                print("\n - EMAIL EDITADO - \n")

            elif opcao == "3":
                novo_nome_instituicao = input(f" Digite o novo nome da instituição {id_instituicao}: ").upper()
                while novo_nome_instituicao == '':
                    print("\n - INFORME UM NOME - \n")
                    novo_nome_instituicao = input(f" Digite o novo nome da instituição {id_instituicao}: ").upper()
                cursor.execute(" UPDATE instituicoes SET nome_instituicao = ? WHERE id_instituicao = ? ", (novo_nome_instituicao,id_instituicao,))
                conexao_DB.commit()
                print("\n - NOME EDITADO - \n")

            elif opcao == "4":
                novo_telefone_instituicao = input(f" Digite o novo telefone da instituição {id_instituicao}: ")
                while novo_telefone_instituicao == '':
                    print("\n - INFORME UM TELEFONE - \n")
                    novo_telefone_instituicao = input(f" Digite o novo telefone da instituição {id_instituicao}: ")
                cursor.execute(" UPDATE instituicoes SET telefone_instituicao = ? WHERE id_instituicao = ? ", (novo_telefone_instituicao,id_instituicao,))
                conexao_DB.commit()
                print("\n - TELEFONE EDITADO - \n")

            else:
                print("\n - OPÇÃO INVÁLIDA - \n")
            
            menu_instituicoes()

def insere_instituicao():
    while True:
        opcao = input(f"""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
|____________ INSERIR INSTITUIÇÃO _____________|
|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|
|                                              |
|   [0] ............................. VOLTAR   |
|   [1] ................ Inserir Instituição   |
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

>>> Escolha a opção: """)
        if opcao  == "0":
            print("\n - VOLTANDO - \n")
            break
        elif opcao == "1":
            nome_instituicao = input(" Digite o nome da Instituição: ").upper()
            while nome_instituicao == '':
                print("\n - INFORME UM NOME - \n")
                nome_instituicao = input(" Digite o nome da Instituição: ").upper()

            descricao_instituicao = input(" Digite a descrição da instituição: ").upper()
            while descricao_instituicao == '':
                print("\n - INFORME UMA DESCRIÇÃO - \n")
                descricao_instituicao = input(" Digite a descrição da instituição: ").upper()

            email_instituicao = input(" Digite o email da instituição: ")
            while email_instituicao == '':
                print("\n - INFORME UM EMAIL - \n")
                email_instituicao = input(" Digite o email da instituição: ")

            telefone_instituicao = input(" Digite o telefone da instituição ")
            while telefone_instituicao == '':
                print("\n - INFORME UM TELEFONE - \n")
                telefone_instituicao = input(" Digite o telefone da instituição: ")

            cursor.execute(" INSERT INTO instituicoes (descricao_instituicao, email_instituicao, nome_instituicao, telefone_instituicao) VALUES (?,?,?,?) ", (descricao_instituicao, email_instituicao, nome_instituicao, telefone_instituicao,))
            conexao_DB.commit()

            print("\n - INSTITUIÇÃO ADICIONADA - \n")

def busca_instituicao():
    while True:
        opcao = input(f"""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
|___________ BUSCAR INSTITUIÇÃO ___________|
|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|
|                                          |
|   [0] ......................... VOLTAR   |
|   [1] ................. Buscar pelo ID   |
|   [2] .......... Buscar pela descrição   |
|   [3] .............. Buscar pelo email   |
|   [4] ............... Buscar pelo nome   |
|   [5] ........... Buscar pelo telefone   |
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

>>> Escolha a opção: """)
        if opcao  == "0":
            print("\n - VOLTANDO - \n")
            break

        elif opcao == "1":
            busca_id = input(" Busca pelo ID da Instituição: ")
            while busca_id == '':
                print("\n - INFORME UM VALOR - \n")
                busca_id = input(" Busca pelo ID da Instituição: ")

            cursor.execute(" SELECT * FROM instituicoes WHERE id_instituicao = ? ", (busca_id,))
            verifica_id = cursor.fetchall()

            if not verifica_id: # Verifica se a variável 'verifica_id' está vazia
                print("\n - A BUSCA PELO ID INFORMADO NÃO FOI ENCONTRADA - \n")
                busca_instituicao()
            else:
                print("\n - RESULTADO(S): - \n")
                print(" >>> Considere a sequência: ID, Descrição, Email, Nome e Telefone separados por vírgula: \n")
                print(verifica_id) # Exibe a variável 'verifica_id' pois existe apenas um ID instituição

        elif opcao == "2":
            busca_descricao = input(" Buscar pela descrição da Instituição: ").upper()
            while busca_descricao == '':
                print("\n - INFORME UM VALOR - \n")
                busca_descricao = input(" Buscar pela descrição da Instituição: ").upper()

            cursor.execute(" SELECT * FROM instituicoes WHERE descricao_instituicao LIKE ? ", ('%' + busca_descricao + '%',))
            verifica_descricao = cursor.fetchall()

            if not verifica_descricao: # Verifica se a variável 'verifica_descricao' está vazia
                print("\n - A BUSCA PELA DESCRIÇÃO INFORMADA NÃO FOI ENCONTRADA - \n")
                busca_instituicao()
            else:
                print("\n - RESULTADO(S): - \n")
                print(" >>> Considere a sequência: ID, Descrição, Email, Nome e Telefone separados por vírgula: \n")
                for instituicao in verifica_descricao:
                    print(instituicao) # Exibe a variável 'instituicao' pois pode existir mais de um resultado, ou seja, exibe todos os resultados

        elif opcao == "3":
            busca_email = input(" Buscar pelo email da Instituição: ")
            while busca_email == '':
                print("\n - INFORME UM VALOR - \n")
                busca_email = input(" Buscar pelo email da Instituição: ")

            cursor.execute(f" SELECT * FROM instituicoes WHERE email_instituicao LIKE ? ", ('%' + busca_email + '%',))
            verifica_email = cursor.fetchall()

            if not verifica_email: # Verifica se a variável 'verifica_email' está vazia
                print("\n - A BUSCA PELO EMAIL INFORMADO NÃO FOI ENCONTRADA - \n")
                busca_instituicao()
            else:
                print("\n - RESULTADO(S): - \n")
                print(" >>> Considere a sequência: ID, Descrição, Email, Nome e Telefone separados por vírgula: \n")
                for instituicao in verifica_email:
                    print(instituicao) # Exibe a variável 'instituicao' pois pode existir mais de um resultado, ou seja, exibe todos os resultados

        elif opcao == "4":
            busca_nome = input(" Buscar pelo nome da Instituição: ").upper()
            while busca_nome == '':
                print("\n - INFORME UM VALOR - \n")
                busca_nome = input(" Buscar pelo nome da Instituição: ").upper()

            cursor.execute(f" SELECT * FROM instituicoes WHERE nome_instituicao LIKE ? ", ('%' + busca_nome + '%',))
            verifica_nome = cursor.fetchall()

            if not verifica_nome: # Verifica se a variável 'verifica_nome' está vazia
                print("\n - A BUSCA PELO NOME INFORMADO NÃO FOI ENCONTRADA - \n")
                busca_instituicao()
            else:
                print("\n - RESULTADO(S): - \n")
                print(" >>> Considere a sequência: ID, Descrição, Email, Nome e Telefone separados por vírgula: \n")
                for instituicao in verifica_nome:
                    print(instituicao) # Exibe a variável 'instituicao' pois pode existir mais de um resultado, ou seja, exibe todos os resultados

        elif opcao == "5":
            busca_telefone = input(" Buscar pelo telefone da Instituição: ")
            while busca_telefone == '':
                print("\n - INFORME UM VALOR - \n")
                busca_telefone = input(" Buscar pelo telefone da Instituição: ")
            
            cursor.execute(f" SELECT * FROM instituicoes WHERE telefone_instituicao LIKE ? ", ('%' + busca_telefone + '%',))
            verifica_telefone = cursor.fetchall()

            if not verifica_telefone: # Verifica se a variável 'verifica_telefone' está vazia
                print("\n - A BUSCA PELO NOME INFORMADO NÃO FOI ENCONTRADA - \n")
                busca_instituicao()
            else:
                print("\n - RESULTADO(S): - \n")
                print(" >>> Considere a sequência: ID, Descrição, Email, Nome e Telefone separados por vírgula: \n")
                for instituicao in verifica_telefone:
                    print(instituicao) # Exibe a variável 'instituicao' pois pode existir mais de um resultado, ou seja, exibe todos os resultados
        
        else:
            print("\n - OPÇÃO INVÁLIDA - \n")

def exclui_instituicao():
    while True:
        opcao = input(f"""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
|____________ EXCLUIR INSTITUIÇÃO _____________|
|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|
|                                              |
|   [0] ............................. VOLTAR   |
|   [1] .......... Excluir Instituição por ID  |
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

>>> Escolha a opção: """)
        if opcao  == "0":
            print("\n - VOLTANDO - \n")
            break
        elif opcao == "1":
            id_instituicao = input(" Digite o ID da Instituição que deseja excluir: ")
            while id_instituicao == '':
                print("\n - INFORME UM ID - \n")
                id_instituicao = input(" Digite o ID da Instituição que deseja excluir: ")

            cursor.execute(" SELECT id_instituicao FROM instituicoes WHERE id_instituicao = ? ", (id_instituicao,))
            verifica_id = cursor.fetchall()

            if not verifica_id:
                print(f"\n - INSTITUIÇÃO > {id_instituicao} < INEXISTENTE - \n")
                exclui_instituicao()
            else:
                visualiza_instituicao_selecionada(id_instituicao)
                confirma_exclusao = input(f" Tem certeza que deseja excluir a instituição {id_instituicao}? (s/n): ").upper()
                if confirma_exclusao == "S":
                    cursor.execute(" DELETE FROM instituicoes WHERE id_instituicao = ? ", (id_instituicao,))
                    conexao_DB.commit()
                    print("\n - INSTITUIÇÃO DELETADA - \n")
                elif confirma_exclusao == "N":
                    print("\n - EXCLUSÃO NÃO CONFIRMADA - \n")
                    exclui_instituicao()
                else:
                    print("\n - OPÇÃO INVÁLIDA - \n")        
        else:
            print("\n - OPÇÃO INVÁLIDA - \n")

if __name__ == "__main__":
    menu_instituicoes()
