import sqlite3
import instituicoes

# Cria uma conexão com o banco de dados
conexao_DB = sqlite3.connect('DB_SUI.db')

# Cria um cursor para executar comandos SQL
cursor = conexao_DB.cursor()

def menu_servicos():
    while True:
        opcao = input("""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
|_______________________ SERVIÇOS _______________________|
|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|
|                                                        |
|   [0] ....................................... VOLTAR   |
|                                                        |
|   [1] ........... Visualizar os serviços disponíveis   |
|   [2] ............................... Editar serviço   |
|   [3] .............................. Inserir serviço   |
|   [4] ............................... Buscar serviço   |
|   [5] .............................. Excluir serviço   |
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

>>> Escolha a opção: """)
        if opcao  == "0":
            print("\n - VOLTANDO - \n")
            break
        elif opcao == "1":
            servicos_disponiveis()
        elif opcao == "2":
            edita_servico()
        elif opcao == "3":
            insere_servico()
        elif opcao == "4":
            busca_servico()
        elif opcao == "5":
            exclui_servico()
        else:
            print("\n - OPÇÃO INVÁLIDA - \n")

def obtem_servicos(): # Obtem os servicos em lista
    servicos = []

    # Obtem os valores da tabela servicos
    cursor.execute(""" SELECT * FROM servicos """)
    valores = cursor.fetchall() # Lista de tuplas

    for valor in valores:
        servico = list(valor) # Transforma cada tupla em lista
        servicos.append(servico) # Agrupa as listas em uma única lista

    return servicos

def servicos_disponiveis(): # Visualiza os serviços disponíveis
    lista_servicos = obtem_servicos()
    
    # Exibe a tabela estilizada
    print("\n - SERVIÇOS DISPONÍVEIS -")
    print(f"{'=-'*75}")
    print(f"| {'ID':<2} || {'ID INSTITUIÇÃO':<14} | {'NOME':<40} | {'TIPO':<80} |")
    print(f"|{'='*4}||{'='*16}|{'='*42}|{'='*82}|")
    
    for servico in lista_servicos:
        print(f"| {servico[0]:<2} || {servico[1]:<14} | {servico[2]:<40} | {servico[3]:<80} |")
        print(f"|{'-'*4}||{'-'*16}|{'-'*42}|{'-'*82}|")
    print(f"{'=-'*75}\n")

def visualiza_servico_selecionado(id_servico):
    servicos = [] # Obtem os servicos em lista
    cursor.execute(" SELECT * FROM servicos WHERE id_servico = ? ", (id_servico,)) # Obtem os valores da tabela servicos
    valores = cursor.fetchall() # Lista de tuplas
    for valor in valores:
        servico = list(valor) # Transforma cada tupla em lista
        servicos.append(servico) # Agrupa as listas em uma única lista

    # Exibe a tabela estilizada
    print("\n - SERVIÇO SELECIONADO -")
    print(f"{'=-'*76}")
    print(f"| {'ID':<3} || {'ID INSTITUIÇÃO':<14} | {'NOME':<40} | {'TIPO':<81} |")
    print(f"|{'='*5}||{'='*16}|{'='*42}|{'='*83}|")
    
    for servico in servicos:
        print(f"| {servico[0]:<3} || {servico[1]:<14} | {servico[2]:<40} | {servico[3]:<81} |")
        print(f"|{'-'*5}||{'-'*16}|{'-'*42}|{'-'*83}|")
    print(f"{'=-'*76}\n")

def edita_servico():
    while True:
        print("\n - EDITAR SERVIÇO - \n")
        id_servico = input(" Digite o ID do serviço que deseja editar: ")
        while id_servico == "":
            print("\n - INFORME UM ID - \n")
            id_servico = input(" Digite o ID do serviço que deseja editar: ")
        
        # Verifica se o ID informado é existente no DB
        cursor.execute(" SELECT id_servico FROM servicos WHERE id_servico = ? ", (id_servico,))
        verifica_servico = cursor.fetchall()
        
        if verifica_servico == None:
            print("\n - SERVIÇO INEXISTENTE - \n")
            menu_servicos()
        else:
            visualiza_servico_selecionado(id_servico)
            opcao = input(f"""
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    |__________ EDITAR SERVIÇO {id_servico:<3} __________|
    |-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|
    |                                        |
    |   [0] ....................... VOLTAR   |
    |                                        |
    |   [1] ........ Editar ID instituição   |
    |   [2] .................. Editar nome   |
    |   [3] .................. Editar tipo   |
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

    >>> Escolha a opção: """)
            if opcao  == "0":
                print("\n - VOLTANDO - \n")
                break

            elif opcao == "1":
                instituicoes.instituicoes_disponiveis()
                novo_id_instuicao = input(f" Digite o novo ID instituição do serviço {id_servico}: ").upper()
                while novo_id_instuicao == '':
                    print("\n - INFORME UM ID INSTITUIÇÃO - \n")
                    novo_id_instuicao = input(f" Digite o novo ID instituição do serviço {id_servico}: ").upper()

                cursor.execute(" SELECT * FROM servicos WHERE fk_id_instituicao = ? ", novo_id_instuicao)
                verifica_id_instituicao = cursor.fetchall()

                if verifica_id_instituicao == None:
                    print(" - ID INSTITUIÇÃO INEXISTENTE - ")
                else:
                    cursor.execute(" UPDATE servicos SET fk_id_instituicao = ? WHERE id_servico = ? ", (novo_id_instuicao,id_servico,))
                    conexao_DB.commit()
                    print("\n - ID INSTITUIÇÃO EDITADO - \n")

            elif opcao == "2":
                novo_nome_servico = input(f" Digite o novo nome do serviço {id_servico}: ").upper()
                while novo_nome_servico == '':
                    print("\n - INFORME UM NOME - \n")
                    novo_nome_servico = input(f" Digite o novo nome do serviço {id_servico}: ").upper()
                cursor.execute(" UPDATE servicos SET nome_servico = ? WHERE id_servico = ? ", (novo_nome_servico,id_servico,))
                conexao_DB.commit()
                print("\n - NOME EDITADO - \n")

            elif opcao == "3":
                novo_tipo_servico = input(f" Digite o novo tipo do serviço {id_servico}: ")
                while novo_tipo_servico == '':
                    print("\n - INFORME UM TIPO - \n")
                    novo_tipo_servico = input(f" Digite o novo tipo do serviço {id_servico}: ")
                cursor.execute(" UPDATE servicos SET tipo_servico = ? WHERE id_servico = ? ", (novo_tipo_servico,id_servico,))
                conexao_DB.commit()
                print("\n - TIPO EDITADO - \n")

            else:
                print("\n - OPÇÃO INVÁLIDA - \n")
            
            menu_servicos()

def insere_servico():
    while True:
        opcao = input(f"""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
|____________ INSERIR SERVIÇO ____________|
|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|
|                                         |
|   [0] ........................ VOLTAR   |
|   [1] ............... Inserir serviço   |
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

>>> Escolha a opção: """)
        if opcao  == "0":
            print("\n - VOLTANDO - \n")
            break
        elif opcao == "1":
            nome_servico = input(" Digite o nome do serviço: ").upper()
            while nome_servico == '':
                print("\n - INFORME UM NOME - \n")
                nome_servico = input(" Digite o nome da serviço: ").upper()

            tipo_servico = input(" Digite a descrição da serviço: ").upper()
            while tipo_servico == '':
                print("\n - INFORME UMA DESCRIÇÃO - \n")
                tipo_servico = input(" Digite a descrição da serviço: ").upper()

            cursor.execute(" INSERT INTO servicos (tipo_servico, email_servico, nome_servico, telefone_servico) VALUES (?,?) ", (tipo_servico, email_servico, nome_servico, telefone_servico,))
            conexao_DB.commit()

            print("\n - serviço ADICIONADA - \n")

def busca_servico():
    while True:
        opcao = input(f"""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
|___________ BUSCAR serviço ___________|
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
            busca_id = input(" Busca pelo ID da serviço: ").upper()
            while busca_id == '':
                print("\n - INFORME UM VALOR - \n")
                busca_id = input(" Busca pelo ID da serviço: ").upper()

            cursor.execute(f" SELECT * FROM servicos WHERE id_servico = ? ", (busca_id))
            verifica_id = cursor.fetchall()

            if not verifica_id: # Verifica se a variável 'verifica_id' está vazia
                print("\n - A BUSCA PELO ID INFORMADO NÃO FOI ENCONTRADA - \n")
                busca_servico()
            else:
                print("\n - RESULTADO(S): - \n")
                print(" >>> Considere a sequência: ID, Descrição, Email, Nome e Telefone separados por vírgula: \n")
                print(verifica_id)

        elif opcao == "2":
            busca_descricao = input(" Buscar pela descrição da serviço: ").upper()
            while busca_descricao == '':
                print("\n - INFORME UM VALOR - \n")
                busca_descricao = input(" Buscar pela descrição da serviço: ").upper()

            cursor.execute(f" SELECT * FROM servicos WHERE descricao_servico LIKE '%{busca_descricao}%' ")
            verifica_descricao = cursor.fetchall()

            if not verifica_descricao: # Verifica se a variável 'verifica_descricao' está vazia
                print("\n - A BUSCA PELA DESCRIÇÃO INFORMADA NÃO FOI ENCONTRADA - \n")
                busca_servico()
            else:
                print("\n - RESULTADO(S): - \n")
                print(" >>> Considere a sequência: ID, Descrição, Email, Nome e Telefone separados por vírgula: \n")
                for servico in verifica_descricao:
                    print(servico)

        elif opcao == "3":
            busca_email = input(" Buscar pelo email da serviço: ")
            while busca_email == '':
                print("\n - INFORME UM VALOR - \n")
                busca_email = input(" Buscar pelo email da serviço: ")

            cursor.execute(f" SELECT * FROM servicos WHERE email_servico LIKE '%{busca_email}%' ")
            verifica_email = cursor.fetchall()

            if not verifica_email: # Verifica se a variável 'verifica_email' está vazia
                print("\n - A BUSCA PELO EMAIL INFORMADO NÃO FOI ENCONTRADA - \n")
                busca_servico()
            else:
                print("\n - RESULTADO(S): - \n")
                print(" >>> Considere a sequência: ID, Descrição, Email, Nome e Telefone separados por vírgula: \n")
                for servico in verifica_email:
                    print(servico)

        elif opcao == "4":
            busca_nome = input(" Buscar pelo nome da serviço: ").upper()
            while busca_nome == '':
                print("\n - INFORME UM VALOR - \n")
                busca_nome = input(" Buscar pelo nome da serviço: ").upper()

            cursor.execute(f" SELECT * FROM servicos WHERE nome_servico LIKE '%{busca_nome}%' ")
            verifica_nome = cursor.fetchall()

            if not verifica_nome: # Verifica se a variável 'verifica_nome' está vazia
                print("\n - A BUSCA PELO NOME INFORMADO NÃO FOI ENCONTRADA - \n")
                busca_servico()
            else:
                print("\n - RESULTADO(S): - \n")
                print(" >>> Considere a sequência: ID, Descrição, Email, Nome e Telefone separados por vírgula: \n")
                for servico in verifica_nome:
                    print(servico)

        elif opcao == "5":
            busca_telefone = input(" Buscar pelo telefone da serviço: ")
            while busca_telefone == '':
                print("\n - INFORME UM VALOR - \n")
                busca_telefone = input(" Buscar pelo telefone da serviço: ")
            
            cursor.execute(f" SELECT * FROM servicos WHERE telefone_servico LIKE '%{busca_telefone}%' ")
            verifica_telefone = cursor.fetchall()

            if not verifica_telefone: # Verifica se a variável 'verifica_telefone' está vazia
                print("\n - A BUSCA PELO NOME INFORMADO NÃO FOI ENCONTRADA - \n")
                busca_servico()
            else:
                print("\n - RESULTADO(S): - \n")
                print(" >>> Considere a sequência: ID, Descrição, Email, Nome e Telefone separados por vírgula: \n")
                for servico in verifica_telefone:
                    print(servico)
        
        else:
            print("\n - OPÇÃO INVÁLIDA - \n")

def exclui_servico():
    while True:
        opcao = input(f"""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
|____________ EXCLUIR serviço _____________|
|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|
|                                              |
|   [0] ............................. VOLTAR   |
|   [1] .......... Excluir serviço por ID  |
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

>>> Escolha a opção: """)
        if opcao  == "0":
            print("\n - VOLTANDO - \n")
            break
        elif opcao == "1":
            id_servico = input(" Digite o ID da serviço que deseja excluir: ")
            while id_servico == '':
                print("\n - INFORME UM ID - \n")
                id_servico = input(" Digite o ID da serviço que deseja excluir: ")

            cursor.execute(" SELECT id_servico FROM servicos WHERE id_servico = ? ", (id_servico,))
            verifica_id = cursor.fetchall()

            if verifica_id == None:
                print(f"\n - serviço > {id_servico} < INEXISTENTE - \n")
                exclui_servico()
            else:
                visualiza_servico_selecionado(id_servico)
                confirma_exclusao = input(f" Tem certeza que deseja excluir a serviço {id_servico}? (s/n): ").upper()
                if confirma_exclusao == "S":
                    cursor.execute(" DELETE FROM servicos WHERE id_servico = ? ", (id_servico,))
                    conexao_DB.commit()
                    print("\n - serviço DELETADA - \n")
                elif confirma_exclusao == "N":
                    print("\n - EXCLUSÃO NÃO CONFIRMADA - \n")
                    exclui_servico()
                else:
                    print("\n - OPÇÃO INVÁLIDA - \n")        
        else:
            print("\n - OPÇÃO INVÁLIDA - \n")

if __name__ == "__main__":
    menu_servicos()
