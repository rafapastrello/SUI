import sqlite3

# Cria uma conexão com o banco de dados
conexao_DB = sqlite3.connect('DB_SUI.db')

# Cria um cursor para executar comandos SQL
cursor = conexao_DB.cursor()

def menu_solicitacoes():
    while True:
        opcao = input("""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
|__________________ SOLICITAÇÕES __________________|
|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|
|                                                  |
|   [0] ................................. VOLTAR   |
|                                                  |
|   [1] ............. Visualizar as solicitações   |
|   [2] ..................... Editar solicitação   |
|   [3] .................... Inserir solicitação   |
|   [4] ..................... Buscar solicitação   |
|   [5] .................... Excluir solicitação   |
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

>>> Escolha a opção: """)
        if opcao  == "0":
            print("\n - VOLTANDO - \n")
            break
        elif opcao == "1":
            visualiza_solicitacoes()
        elif opcao == "2":
            edita_solicitacao()
        elif opcao == "3":
            insere_solicitacao()
        elif opcao == "4":
            busca_solictacao()
        elif opcao == "5":
            exclui_solicitacao()
        else:
            print("\n - OPÇÃO INVÁLIDA - \n")

def obtem_solicitacoes(): # Obtem as solicitacoes em lista
    solicitacoes = []

    # Obtem os valores da tabela solicitacoes
    cursor.execute(""" SELECT * FROM solicitacoes """)
    valores = cursor.fetchall() # Lista de tuplas

    for valor in valores:
        solicitacao = list(valor) # Transforma cada tupla em lista
        solicitacoes.append(solicitacao) # Agrupa as listas em uma única lista

    return solicitacoes

def visualiza_solicitacoes():
    lista_solicitacoes = obtem_solicitacoes()
    
    # Exibe a tabela estilizada
    print("\n - SOLICITAÇÕES DISPONÍVEIS -")
    print(f"{'=-'*92}")
    print(f"| {'ID':<2} || {'ID SERVIÇO':<10} | {'ID USUÁRIO':<10} | {'DESCRIÇÃO':<80} | {'ENDEREÇO':<50} | {'STATUS':<12} |")
    print(f"|{'='*4}||{'='*12}|{'='*12}|{'='*82}|{'='*52}|{'='*14}|")

    for solicitacao in lista_solicitacoes:
        print(f"| {solicitacao[0]:<2} || {solicitacao[1]:<10} | {solicitacao[2]:<10} | {solicitacao[3]:<80} | {solicitacao[4]:<50} | {solicitacao[5]:<12} |")
        print(f"|{'-'*4}||{'-'*12}|{'-'*12}|{'-'*82}|{'-'*52}|{'-'*14}|")
    print(f"{'=-'*92}\n")

def visualiza_solicitacao_selecionada(id_solicitacao):
    solicitacoes = [] # Obtem as solicitacoes em lista
    cursor.execute(" SELECT * FROM solicitacoes WHERE id_solicitacao = ? ", (id_solicitacao,)) # Obtem os valores da tabela solicitacoes
    valores = cursor.fetchall() # Lista de tuplas
    for valor in valores:
        solicitacao = list(valor) # Transforma cada tupla em lista
        solicitacoes.append(solicitacao) # Agrupa as listas em uma única lista

    # Exibe a tabela estilizada
    print("\n - SOLICITAÇÕES DISPONÍVEIS -")
    print(f"{'=-'*92}")
    print(f"| {'ID':<2} || {'ID SERVIÇO':<10} | {'ID USUÁRIO':<10} | {'DESCRIÇÃO':<80} | {'ENDEREÇO':<50} | {'STATUS':<12} |")
    print(f"|{'='*4}||{'='*12}|{'='*12}|{'='*82}|{'='*52}|{'='*14}|")

    for solicitacao in lista_solicitacoes:
        print(f"| {solicitacao[0]:<2} || {solicitacao[1]:<10} | {solicitacao[2]:<10} | {solicitacao[3]:<80} | {solicitacao[4]:<50} | {solicitacao[5]:<12} |")
        print(f"|{'-'*4}||{'-'*12}|{'-'*12}|{'-'*82}|{'-'*52}|{'-'*14}|")
    print(f"{'=-'*92}\n")

def edita_solicitacao():
    while True:
        print("\n - EDITAR solicitação - \n")
        id_solicitacao = input(" Digite o ID da solicitação que deseja editar: ")
        while id_solicitacao == "":
            print("\n - INFORME UM ID - \n")
            id_solicitacao = input(" Digite o ID da solicitação que deseja editar: ")
        
        # Verifica se o ID informado é existente no DB
        cursor.execute(" SELECT id_solicitacao FROM solicitacoes WHERE id_solicitacao = ? ", (id_solicitacao,))
        verifica_solicitacao = cursor.fetchall()
        
        if verifica_solicitacao == None:
            print("\n - solicitação INEXISTENTE - \n")
            menu_solicitacoes()
        else:
            visualiza_solicitacao_selecionada(id_solicitacao)
            opcao = input(f"""
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    |___________ EDITAR solicitação {id_solicitacao:<3} ___________|
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
                nova_descricao_solicitacao = input(f" Digite a nova descrição da solicitação {id_solicitacao}: ").upper()
                while nova_descricao_solicitacao == '':
                    print("\n - INFORME UMA DESCRIÇÃO - \n")
                    nova_descricao_solicitacao = input(f" Digite a nova descrição da solicitação {id_solicitacao}: ").upper()
                cursor.execute(" UPDATE solicitacoes SET descricao_solicitacao = ? WHERE id_solicitacao = ? ", (nova_descricao_solicitacao,id_solicitacao,))
                conexao_DB.commit()
                print("\n - DESCRIÇÃO EDITADA - \n")

            elif opcao == "2":
                novo_email_solicitacao = input(f" Digite o novo email da solicitação {id_solicitacao}: ")
                while novo_email_solicitacao == '':
                    print("\n - INFORME UM EMAIL - \n")
                    novo_email_solicitacao = input(f" Digite o novo email da solicitação {id_solicitacao}: ")
                cursor.execute(" UPDATE solicitacoes SET email_solicitacao = ? WHERE id_solicitacao = ? ", (novo_email_solicitacao,id_solicitacao,))
                conexao_DB.commit()
                print("\n - EMAIL EDITADO - \n")

            elif opcao == "3":
                novo_nome_solicitacao = input(f" Digite o novo nome da solicitação {id_solicitacao}: ").upper()
                while novo_nome_solicitacao == '':
                    print("\n - INFORME UM NOME - \n")
                    novo_nome_solicitacao = input(f" Digite o novo nome da solicitação {id_solicitacao}: ").upper()
                cursor.execute(" UPDATE solicitacoes SET nome_solicitacao = ? WHERE id_solicitacao = ? ", (novo_nome_solicitacao,id_solicitacao,))
                conexao_DB.commit()
                print("\n - NOME EDITADO - \n")

            elif opcao == "4":
                novo_telefone_solicitacao = input(f" Digite o novo telefone da solicitação {id_solicitacao}: ")
                while novo_telefone_solicitacao == '':
                    print("\n - INFORME UM TELEFONE - \n")
                    novo_telefone_solicitacao = input(f" Digite o novo telefone da solicitação {id_solicitacao}: ")
                cursor.execute(" UPDATE solicitacoes SET telefone_solicitacao = ? WHERE id_solicitacao = ? ", (novo_telefone_solicitacao,id_solicitacao,))
                conexao_DB.commit()
                print("\n - TELEFONE EDITADO - \n")

            else:
                print("\n - OPÇÃO INVÁLIDA - \n")
            
            menu_solicitacoes()

def insere_solicitacao():
    while True:
        opcao = input(f"""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
|____________ INSERIR solicitação _____________|
|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|
|                                              |
|   [0] ............................. VOLTAR   |
|   [1] ................ Inserir solicitação   |
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

>>> Escolha a opção: """)
        if opcao  == "0":
            print("\n - VOLTANDO - \n")
            break
        elif opcao == "1":
            nome_solicitacao = input(" Digite o nome da solicitação: ").upper()
            while nome_solicitacao == '':
                print("\n - INFORME UM NOME - \n")
                nome_solicitacao = input(" Digite o nome da solicitação: ").upper()

            descricao_solicitacao = input(" Digite a descrição da solicitação: ").upper()
            while descricao_solicitacao == '':
                print("\n - INFORME UMA DESCRIÇÃO - \n")
                descricao_solicitacao = input(" Digite a descrição da solicitação: ").upper()

            email_solicitacao = input(" Digite o email da solicitação: ")
            while email_solicitacao == '':
                print("\n - INFORME UM EMAIL - \n")
                email_solicitacao = input(" Digite o email da solicitação: ")

            telefone_solicitacao = input(" Digite o telefone da solicitação ")
            while telefone_solicitacao == '':
                print("\n - INFORME UM TELEFONE - \n")
                telefone_solicitacao = input(" Digite o telefone da solicitação: ")

            cursor.execute(" INSERT INTO solicitacoes (descricao_solicitacao, email_solicitacao, nome_solicitacao, telefone_solicitacao) VALUES (?,?,?,?) ", (descricao_solicitacao, email_solicitacao, nome_solicitacao, telefone_solicitacao,))
            conexao_DB.commit()

            print("\n - solicitação ADICIONADA - \n")

def busca_solicitacao():
    while True:
        opcao = input(f"""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
|___________ BUSCAR solicitação ___________|
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
            busca_id = input(" Busca pelo ID da solicitação: ")
            while busca_id == '':
                print("\n - INFORME UM VALOR - \n")
                busca_id = input(" Busca pelo ID da solicitação: ")

            cursor.execute(" SELECT * FROM solicitacoes WHERE id_solicitacao = ? ", (busca_id,))
            verifica_id = cursor.fetchall()

            if not verifica_id: # Verifica se a variável 'verifica_id' está vazia
                print("\n - A BUSCA PELO ID INFORMADO NÃO FOI ENCONTRADA - \n")
                busca_solicitacao()
            else:
                print("\n - RESULTADO(S): - \n")
                print(" >>> Considere a sequência: ID, Descrição, Email, Nome e Telefone separados por vírgula: \n")
                print(verifica_id) # Exibe a variável 'verifica_id' pois existe apenas um ID solicitação

        elif opcao == "2":
            busca_descricao = input(" Buscar pela descrição da solicitação: ").upper()
            while busca_descricao == '':
                print("\n - INFORME UM VALOR - \n")
                busca_descricao = input(" Buscar pela descrição da solicitação: ").upper()

            cursor.execute(" SELECT * FROM solicitacoes WHERE descricao_solicitacao LIKE ? ", ('%' + busca_descricao + '%',))
            verifica_descricao = cursor.fetchall()

            if not verifica_descricao: # Verifica se a variável 'verifica_descricao' está vazia
                print("\n - A BUSCA PELA DESCRIÇÃO INFORMADA NÃO FOI ENCONTRADA - \n")
                busca_solicitacao()
            else:
                print("\n - RESULTADO(S): - \n")
                print(" >>> Considere a sequência: ID, Descrição, Email, Nome e Telefone separados por vírgula: \n")
                for solicitacao in verifica_descricao:
                    print(solicitacao) # Exibe a variável 'solicitacao' pois pode existir mais de um resultado, ou seja, exibe todos os resultados

        elif opcao == "3":
            busca_email = input(" Buscar pelo email da solicitação: ")
            while busca_email == '':
                print("\n - INFORME UM VALOR - \n")
                busca_email = input(" Buscar pelo email da solicitação: ")

            cursor.execute(f" SELECT * FROM solicitacoes WHERE email_solicitacao LIKE ? ", ('%' + busca_email + '%',))
            verifica_email = cursor.fetchall()

            if not verifica_email: # Verifica se a variável 'verifica_email' está vazia
                print("\n - A BUSCA PELO EMAIL INFORMADO NÃO FOI ENCONTRADA - \n")
                busca_solicitacao()
            else:
                print("\n - RESULTADO(S): - \n")
                print(" >>> Considere a sequência: ID, Descrição, Email, Nome e Telefone separados por vírgula: \n")
                for solicitacao in verifica_email:
                    print(solicitacao) # Exibe a variável 'solicitacao' pois pode existir mais de um resultado, ou seja, exibe todos os resultados

        elif opcao == "4":
            busca_nome = input(" Buscar pelo nome da solicitação: ").upper()
            while busca_nome == '':
                print("\n - INFORME UM VALOR - \n")
                busca_nome = input(" Buscar pelo nome da solicitação: ").upper()

            cursor.execute(f" SELECT * FROM solicitacoes WHERE nome_solicitacao LIKE ? ", ('%' + busca_nome + '%',))
            verifica_nome = cursor.fetchall()

            if not verifica_nome: # Verifica se a variável 'verifica_nome' está vazia
                print("\n - A BUSCA PELO NOME INFORMADO NÃO FOI ENCONTRADA - \n")
                busca_solicitacao()
            else:
                print("\n - RESULTADO(S): - \n")
                print(" >>> Considere a sequência: ID, Descrição, Email, Nome e Telefone separados por vírgula: \n")
                for solicitacao in verifica_nome:
                    print(solicitacao) # Exibe a variável 'solicitacao' pois pode existir mais de um resultado, ou seja, exibe todos os resultados

        elif opcao == "5":
            busca_telefone = input(" Buscar pelo telefone da solicitação: ")
            while busca_telefone == '':
                print("\n - INFORME UM VALOR - \n")
                busca_telefone = input(" Buscar pelo telefone da solicitação: ")
            
            cursor.execute(f" SELECT * FROM solicitacoes WHERE telefone_solicitacao LIKE ? ", ('%' + busca_telefone + '%',))
            verifica_telefone = cursor.fetchall()

            if not verifica_telefone: # Verifica se a variável 'verifica_telefone' está vazia
                print("\n - A BUSCA PELO NOME INFORMADO NÃO FOI ENCONTRADA - \n")
                busca_solicitacao()
            else:
                print("\n - RESULTADO(S): - \n")
                print(" >>> Considere a sequência: ID, Descrição, Email, Nome e Telefone separados por vírgula: \n")
                for solicitacao in verifica_telefone:
                    print(solicitacao) # Exibe a variável 'solicitacao' pois pode existir mais de um resultado, ou seja, exibe todos os resultados
        
        else:
            print("\n - OPÇÃO INVÁLIDA - \n")

def exclui_solicitacao():
    while True:
        opcao = input(f"""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
|____________ EXCLUIR solicitação _____________|
|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|
|                                              |
|   [0] ............................. VOLTAR   |
|   [1] .......... Excluir solicitação por ID  |
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

>>> Escolha a opção: """)
        if opcao  == "0":
            print("\n - VOLTANDO - \n")
            break
        elif opcao == "1":
            id_solicitacao = input(" Digite o ID da solicitação que deseja excluir: ")
            while id_solicitacao == '':
                print("\n - INFORME UM ID - \n")
                id_solicitacao = input(" Digite o ID da solicitação que deseja excluir: ")

            cursor.execute(" SELECT id_solicitacao FROM solicitacoes WHERE id_solicitacao = ? ", (id_solicitacao,))
            verifica_id = cursor.fetchall()

            if verifica_id == None:
                print(f"\n - solicitação > {id_solicitacao} < INEXISTENTE - \n")
                exclui_solicitacao()
            else:
                visualiza_solicitacao_selecionada(id_solicitacao)
                confirma_exclusao = input(f" Tem certeza que deseja excluir a solicitação {id_solicitacao}? (s/n): ").upper()
                if confirma_exclusao == "S":
                    cursor.execute(" DELETE FROM solicitacoes WHERE id_solicitacao = ? ", (id_solicitacao,))
                    conexao_DB.commit()
                    print("\n - solicitação DELETADA - \n")
                elif confirma_exclusao == "N":
                    print("\n - EXCLUSÃO NÃO CONFIRMADA - \n")
                    exclui_solicitacao()
                else:
                    print("\n - OPÇÃO INVÁLIDA - \n")        
        else:
            print("\n - OPÇÃO INVÁLIDA - \n")

if __name__ == "__main__":
    menu_solicitacoes()
