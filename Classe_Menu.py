from Classe_Agenda import *

class Menu:
    def __init__(self):
        agenda_felipe = Agenda()

        ## iniciar menu
        while True:
            entrada = input('Informe a operação desejada' 
                            '\n1 - Novo contato' 
                            '\n2 - Listar contatos'
                            '\n3 - Alterar telefone'
                            '\n0 - Sair\n')

            if entrada == '1':
                agenda_felipe.salvar_contatos()
            elif entrada == '2':
                agenda_felipe.listar_todos_contatos()
            elif entrada == '3':
                agenda_felipe.alterar_telefone()
            elif entrada == '0':
                break
            else:
                print('opção errada!')