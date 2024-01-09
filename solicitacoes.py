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
        print("\n - EDITAR SOLICITAÇÃO - \n")
        id_solicitacao = input(" Digite o ID da solicitação que deseja editar: ")
        while id_solicitacao == "":
            print("\n - INFORME UM ID - \n")
            id_solicitacao = input(" Digite o ID da solicitação que deseja editar: ")
        
        # Verifica se o ID informado é existente no DB
        cursor.execute(" SELECT id_solicitacao FROM solicitacoes WHERE id_solicitacao = ? ", (id_solicitacao,))
        verifica_solicitacao = cursor.fetchall()
        
        if not verifica_solicitacao:
            print("\n - SOLICITAÇÃO INEXISTENTE - \n")
            menu_solicitacoes()
        else:
            visualiza_solicitacao_selecionada(id_solicitacao)
            opcao = input(f"""
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    |___________ EDITAR SOLICITAÇÃO {id_solicitacao:<3} ___________|
    |-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|
    |                                              |
    |   [0] ............................. VOLTAR   |
    |                                              |
    |   [1] .................. Editar ID serviço   |
    |   [2] .................. Editar ID usuário   |
    |   [3] ................... Editar descrição   |
    |   [4] .................... Editar endereço   |
    |   [5] ...................... Editar status   |
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

    >>> Escolha a opção: """)
            if opcao  == "0":
                print("\n - VOLTANDO - \n")
                break
            elif opcao == "1":
                novo_id_servico = input(f" Digite o novo ID serviço da solicitação {id_solicitacao}: ")
                while novo_id_servico == '':
                    print("\n - INFORME UM ID SERVIÇO - \n")
                    novo_id_servico = input(f" Digite o novo ID serviço da solicitação {id_solicitacao}: ")
                cursor.execute(" UPDATE solicitacoes SET fk_id_servico = ? WHERE id_solicitacao = ? ", (novo_id_servico,id_solicitacao,))
                conexao_DB.commit()
                print("\n - ID SERVIÇO EDITADO - \n")

            elif opcao == "2":
                novo_id_usuario = input(f" Digite o novo ID usuário da solicitação {id_solicitacao}: ")
                while novo_id_usuario == '':
                    print("\n - INFORME UM ID USUÁRIO - \n")
                    novo_id_usuario = input(f" Digite o novo ID usuário da solicitação {id_solicitacao}: ")
                cursor.execute(" UPDATE solicitacoes SET fk_id_usuario = ? WHERE id_solicitacao = ? ", (novo_id_usuario,id_solicitacao,))
                conexao_DB.commit()
                print("\n - ID USUÁRIO EDITADO - \n")

            elif opcao == "3":
                nova_descricao_solicitacao = input(f" Digite a nova descrição da solicitação {id_solicitacao}: ").upper()
                while nova_descricao_solicitacao == '':
                    print("\n - INFORME UMA DESCRIÇÃO - \n")
                    nova_descricao_solicitacao = input(f" Digite a nova descrição da solicitação {id_solicitacao}: ").upper()
                cursor.execute(" UPDATE solicitacoes SET descricao_solicitacao = ? WHERE id_solicitacao = ? ", (nova_descricao_solicitacao,id_solicitacao,))
                conexao_DB.commit()
                print("\n - DESCRIÇÃO EDITADA - \n")

            elif opcao == "4":
                novo_endereco_solicitacao = input(f" Digite o novo endereço da solicitação {id_solicitacao}: ")
                while novo_endereco_solicitacao == '':
                    print("\n - INFORME UM ENDEREÇO - \n")
                    novo_endereco_solicitacao = input(f" Digite o novo endereço da solicitação {id_solicitacao}: ")
                cursor.execute(" UPDATE solicitacoes SET endereco_solicitacao = ? WHERE id_solicitacao = ? ", (novo_endereco_solicitacao,id_solicitacao,))
                conexao_DB.commit()
                print("\n - ENDEREÇO EDITADO - \n")

            elif opcao == "5":
                while True:
                    opcao = input(f"""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
|_______ EDITAR STATUS SOLICITAÇÃO _______|
|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|
|   [0] ........................ VOLTAR   |
|                                         |
|   [1] ...................... Recebida   |
|   [2] .................... Em análise   |
|   [3] .................. Em andamento   |
|   [4] ..................... Concluída   |
|   [5] ..................... Cancelada   |
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

>>> Digite o novo status da solicitação {id_solicitacao}: """)
                    if opcao  == "0":
                        print("\n - VOLTANDO - \n")
                        break
                    elif opcao == "1":
                        novo_status_solicitacao = "Recebida"
                    elif opcao == "2":
                        novo_status_solicitacao = "Em análise"
                    elif opcao == "3":
                        novo_status_solicitacao = "Em andamento"
                    elif opcao == "4":
                        novo_status_solicitacao = "Concluída"
                    elif opcao == "5":
                        novo_status_solicitacao = "Cancelada"
                    else:
                        print("\n - OPÇÃO INVÁLIDA - \n")

                    cursor.execute(" UPDATE solicitacoes SET status_solicitacao = ? WHERE id_solicitacao = ? ", (novo_status_solicitacao,id_solicitacao,))
                    conexao_DB.commit()
                    print("\n - STATUS EDITADO - \n")

            else:
                print("\n - OPÇÃO INVÁLIDA - \n")
            
            menu_solicitacoes()

def insere_solicitacao():
    while True:
        opcao = input(f"""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
|____________ INSERIR SOLICITAÇÃO _____________|
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
|___________ BUSCAR SOLICITAÇÃO ___________|
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
|____________ EXCLUIR SOLICITAÇÃO _____________|
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
