# argparse.ArgumentParser para argumentos mais complexos
# https://docs.python.org/pt-br/3/howto/argparse.html
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    '-b', '--basic',
    help='Mostra "Olá mundo" na tela', 
    type=str, # tipo de argumentp
    metavar='STRING',
    # default='Olá mundo', #Valor padrão
    required=False, 
    # nargs='+' #Recebe mais de um valor
    action='append', # Recebe o argumento mais de um vez
)
parser.add_argument(
    '-v', '--verbose',
    help="Mostra logs",
    action='store_true',
)
args = parser.parse_args()

if args.basic is None:
    print('Nenhum argumento foi fornecido.')
    print(args.basic)
else:
    print(f"O valor é: {args.basic}")

print(args.verbose)