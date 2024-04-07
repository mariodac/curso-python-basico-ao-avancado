import os
import json
tasks_list = []
undo_list = []
redo_list = []
command = ''
while command != 'sair':
    print('Comandos: listar, desfazer, refazer, sair')
    command = input('Digite uma tarefa ou comando: ').strip()
    if command.lower() == 'listar' or command.lower() == 'refazer' or command.lower() == 'desfazer':
        if command.lower() == 'listar':
            if tasks_list:
                print('\nTAREFAS')
                for index,item in enumerate(tasks_list):
                    print(f"{index+1} - {item}")
                print('')
            else:
                print('\nNenhuma tarefa adicionada\n')
        elif command.lower() == 'refazer':
            if redo_list:
                item = redo_list.pop()
                tasks_list.append(item)
                undo_list.append(item)
            else:
                print('\nNada a refazer\n')
        elif command.lower() == 'desfazer':
            if undo_list:
                redo_list.append(undo_list.pop())
                tasks_list.pop()
            else:
                print('\nNada a desfazer\n')
    elif command.lower() == 'clear':
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    else:
        tasks_list.append(command)
        undo_list.append(command)
