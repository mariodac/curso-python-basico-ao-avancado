import os
import json

def read_tasks_list(filename):
    json_tasks_list = []
    if os.path.isfile(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            json_tasks_list = json.load(file)
    return json_tasks_list

def write_tasks_list(filename, tasks_list):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(tasks_list, file, ensure_ascii=False, indent=2)

def print_tasks_list(tasks_list):
    if tasks_list:
        print('\nTAREFAS')
        for index,item in enumerate(tasks_list):
            print(f"\t{index+1} - {item}")
        print('')
    else:
        print('\nNenhuma tarefa adicionada\n')

def read_int():
    while True:
        answer = input('Digite o número da tarefa a ser excluída: ').strip()
        if answer.isdigit():
            int_answer = int(answer)
            return int_answer
        else:
            print('Digite um número de tarefa válido')

undo_list = []
redo_list = []
path_file = 'lista_tarefas.json'
tasks_list = read_tasks_list(path_file)
command = ''
try:
    while command != 'sair':
        print('Comandos: listar, desfazer, refazer, excluir, sair')
        command = input('Digite uma tarefa ou comando: ').strip()
        if command.lower() == 'listar' or command.lower() == 'refazer' or command.lower() == 'desfazer' or command.lower() == 'excluir':
            if command.lower() == 'listar':
                print_tasks_list(tasks_list)
            elif command.lower() == 'refazer':
                if redo_list:
                    item = redo_list.pop()
                    tasks_list.append(item)
                    undo_list.append(item)
                    print_tasks_list(tasks_list)
                    write_tasks_list(path_file, tasks_list)
                else:
                    print('\nNada a refazer\n')
            elif command.lower() == 'desfazer':
                if undo_list:
                    redo_list.append(undo_list.pop())
                    tasks_list.pop()
                    print_tasks_list(tasks_list)
                    write_tasks_list(path_file, tasks_list)
                else:
                    print('\nNada a desfazer\n')
            elif command.lower() == 'excluir':
                if tasks_list:
                    print_tasks_list(tasks_list)
                    task_choiced = read_int()
                    print(f"Tarefa \"{tasks_list.pop(task_choiced-1)}\" removida com sucesso")
                    print_tasks_list(tasks_list)
                    write_tasks_list(path_file, tasks_list)
                else:
                    print('\nNenhuma tarefa adicionada\n')
        elif command.lower() == 'clear':
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')
        elif command.lower() == 'sair':
            write_tasks_list(path_file, tasks_list)
        else:
            tasks_list.append(command)
            undo_list.append(command)
            write_tasks_list(path_file, tasks_list)

except KeyboardInterrupt:
    write_tasks_list(path_file, tasks_list)
    print('\nPrograma interrompido pelo usuário.\n')
