from tela_cidadao import menu_cidadao
import tela_administrador

def menu_principal():
    while True:
        opcao = input("""
    -----------------------------------------
    |   SUI - Soluções Urbanas Integradas   |
    |_______________________________________|
    |____________ MENU PRINCIPAL ___________|
    |-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|
    |                                       |
    |   [0] ........... ENCERRAR PROGRAMA   |
    |   [1] ..................... CIDADÃO   |
    |   [2] ............... ADMINISTRADOR   |
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    >>> Escolha a opção: """)

        if opcao == "0":
            print("\n - SISTEMA ENCERRADO - \n")
            break
        elif opcao == "1":
            print("\n - TELA DO CIDADÃO - \n")
            menu_cidadao()
        elif opcao == "2":
            print("\n - TELA DO ADMINISTRADOR - \n")

        else:
            print("\n - OPÇÃO INVÁLIDA - \n")

if __name__ ==  '__main__':
    menu_principal()
