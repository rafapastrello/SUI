import tela_cidadao
import tela_administrador

def menu_principal():
    """
    - Função responsável por exibir o menu principal do sistema, dando liberdade ao usuário escolher entre CIDADÃO, ADMINISTRADOR, ou encerrar o sistema;
    - Caso o usuário escolha a opção 1, ele é redirecionado ao arquivo 'tela_cidadao.py', caso ele escolha a opção 2, ele é redirecionado ao arquivo 'tela_administrador.py'. 
    """
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

    >>> Escolha sua opção: """)

        if opcao == "0":
            print("\n - SISTEMA ENCERRADO - \n")
            break
        elif opcao == "1":
            print("\n - TELA DO CIDADÃO - \n")

        elif opcao == "2":
            print("\n - TELA DO ADMINISTRADOR - \n")

        else:
            print("\n - OPÇÃO INVÁLIDA - \n")

if __name__ ==  '__main__':
    menu_principal()
