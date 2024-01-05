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
            print("\n - SERVIÇO SELECIONADO -")
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

                cursor.execute(" SELECT * FROM instituicoes WHERE id_instituicao = ? ", novo_id_instuicao)
                verifica_id_instituicao = cursor.fetchall()

                if verifica_id_instituicao == None:
                    print(" - ID INSTITUIÇÃO INEXISTENTE - ")
                else:
                    cursor.execute(" UPDATE servicos SET fk_id_instituicao = ? WHERE id_servico = ? ", (novo_id_instuicao,id_servico,))
                    conexao_DB.commit()
                    print("\n - ID INSTITUIÇÃO EDITADO - \n")
                    visualiza_servico_selecionado(id_servico)

            elif opcao == "2":
                novo_nome_servico = input(f" Digite o novo nome do serviço {id_servico}: ").upper()
                while novo_nome_servico == '':
                    print("\n - INFORME UM NOME - \n")
                    novo_nome_servico = input(f" Digite o novo nome do serviço {id_servico}: ").upper()
                cursor.execute(" UPDATE servicos SET nome_servico = ? WHERE id_servico = ? ", (novo_nome_servico,id_servico,))
                conexao_DB.commit()
                print("\n - NOME EDITADO - \n")
                visualiza_servico_selecionado(id_servico)

            elif opcao == "3":
                novo_tipo_servico = input(f" Digite o novo tipo do serviço {id_servico}: ").upper()
                while novo_tipo_servico == '':
                    print("\n - INFORME UM TIPO - \n")
                    novo_tipo_servico = input(f" Digite o novo tipo do serviço {id_servico}: ").upper()
                cursor.execute(" UPDATE servicos SET tipo_servico = ? WHERE id_servico = ? ", (novo_tipo_servico,id_servico,))
                conexao_DB.commit()
                print("\n - TIPO EDITADO - \n")
                visualiza_servico_selecionado(id_servico)

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
                nome_servico = input(" Digite o nome do serviço: ").upper()

            instituicoes.instituicoes_disponiveis()
            id_instituicao = input(" Digite o ID instituição do serviço: ")
            while id_instituicao == '':
                print("\n - INFORME UM ID INSTITUIÇÃO - \n")
                id_instituicao = input(" Digite o ID instituição do serviço: ")

            # Verifica se o ID instituição informado é existente na tabela de intituições
            cursor.execute(" SELECT * FROM instituicoes WHERE id_instituicao = ? ", novo_id_instuicao)
            verifica_id_instituicao = cursor.fetchall()

            if verifica_id_instituicao == None:
                print(" - ID INSTITUIÇÃO INEXISTENTE - ")
                break
                
            tipo_servico = input(" Digite o tipo do serviço: ").upper()
            while tipo_servico == '':
                print("\n - INFORME UMA DESCRIÇÃO - \n")
                tipo_servico = input(" Digite o tipo do serviço: ").upper()

            cursor.execute(" INSERT INTO servicos (fk_id_instituicao, nome_servico, tipo_servico) VALUES (?,?,?) ", (id_instituicao, nome_servico, tipo_servico,))
            conexao_DB.commit()

            print("\n - SERVIÇO ADICIONADO - \n")
            menu_servicos()

def busca_servico():
    while True:
        opcao = input(f"""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
|_____________ BUSCAR SERVIÇO _____________|
|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|
|                                          |
|   [0] ......................... VOLTAR   |
|   [1] ................. Buscar pelo ID   |
|   [2] ..... Buscar pelo ID instituição   |
|   [3] ............... Buscar pelo nome   |
|   [4] ............... Buscar pelo tipo   |
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

>>> Escolha a opção: """)
        if opcao  == "0":
            print("\n - VOLTANDO - \n")
            break

        elif opcao == "1":
            busca_id = input(" Busca pelo ID do serviço: ")
            while busca_id == '':
                print("\n - INFORME UM VALOR - \n")
                busca_id = input(" Busca pelo ID do serviço: ")

            cursor.execute(f" SELECT * FROM servicos WHERE id_servico = ? ", (busca_id,))
            verifica_id = cursor.fetchall()

            if not verifica_id: # Verifica se a variável 'verifica_id' está vazia
                print("\n - A BUSCA PELO ID INFORMADO NÃO FOI ENCONTRADA - \n")
                busca_servico()
            else:
                print("\n - RESULTADO(S): - \n")
                print(" >>> Considere a sequência: ID, ID instituição, Nome e Tipo separados por vírgula: \n")
                print(verifica_id) # Exibe a variável 'verifica_id' pois existe apenas um ID instituição

        elif opcao == "2":
            busca_id_instituicao = input(" Buscar pelo ID da instituição: ")
            while busca_id_instituicao == '':
                print("\n - INFORME UM VALOR - \n")
                busca_id_instituicao = input(" Buscar pelo ID da instituição: ")

            cursor.execute(f" SELECT * FROM servicos WHERE fk_id_instituicao = ? ", (busca_id,))
            verifica_id_instituicao = cursor.fetchall()

            if not verifica_id_instituicao: # Verifica se a variável 'verifica_id_instituicao' está vazia
                print("\n - A BUSCA PELO ID INSTITUIÇÃO INFORMADO NÃO FOI ENCONTRADA - \n")
                busca_servico()
            else:
                print("\n - RESULTADO(S): - \n")
                print(" >>> Considere a sequência: ID, ID instituição, Nome e Tipo separados por vírgula: \n")
                for servico in verifica_id_instituicao:
                    print(servico) # Exibe a variável 'servico' pois pode existir mais de um resultado, ou seja, exibe todos os resultados

        elif opcao == "3":
            busca_nome = input(" Buscar pelo nome do serviço: ")
            while busca_nome == '':
                print("\n - INFORME UM VALOR - \n")
                busca_nome = input(" Buscar pelo nome do serviço: ")

            cursor.execute(f" SELECT * FROM servicos WHERE nome_servico LIKE '%{busca_nome}%' ")
            verifica_nome = cursor.fetchall()

            if not verifica_nome: # Verifica se a variável 'verifica_nome' está vazia
                print("\n - A BUSCA PELO NOME INFORMADO NÃO FOI ENCONTRADA - \n")
                busca_servico()
            else:
                print("\n - RESULTADO(S): - \n")
                print(" >>> Considere a sequência: ID, ID instituição, Nome e Tipo separados por vírgula: \n")
                for servico in verifica_nome:
                    print(servico) # Exibe a variável 'servico' pois pode existir mais de um resultado, ou seja, exibe todos os resultados

        elif opcao == "4":
            busca_tipo = input(" Buscar pelo tipo do serviço: ").upper()
            while busca_tipo == '':
                print("\n - INFORME UM VALOR - \n")
                busca_tipo = input(" Buscar pelo tipo do serviço: ").upper()

            cursor.execute(f" SELECT * FROM servicos WHERE tipo_servico LIKE '%{busca_tipo}%' ")
            verifica_tipo = cursor.fetchall()

            if not verifica_tipo: # Verifica se a variável 'verifica_tipo' está vazia
                print("\n - A BUSCA PELO TIPO INFORMADO NÃO FOI ENCONTRADA - \n")
                busca_servico()
            else:
                print("\n - RESULTADO(S): - \n")
                print(" >>> Considere a sequência: ID, Descrição, Email, Nome e Telefone separados por vírgula: \n")
                for servico in verifica_tipo:
                    print(servico) # Exibe a variável 'servico' pois pode existir mais de um resultado, ou seja, exibe todos os resultados
        
        else:
            print("\n - OPÇÃO INVÁLIDA - \n")

def exclui_servico():
    while True:
        opcao = input(f"""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
|____________ EXCLUIR SERVIÇO ____________|
|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|
|                                         |
|   [0] ........................ VOLTAR   |
|   [1] ......... Excluir serviço por ID  |
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

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
