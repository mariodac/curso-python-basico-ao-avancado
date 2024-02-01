# Exercício - sistema de perguntas e respostas


questions = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': 2,
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': 0,
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': 1,
    },
    {
        'Pergunta': r'Quanto é 10% de 100?',
        'Opções': ['10', '20', '30', '40'],
        'Resposta': 0,
    },
    {
        'Pergunta': 'Quem descobriu o Brasil',
        'Opções': ['Cristovão Colombo', 'Pedro Alvares Cabral', 'Bill Clinton', 'Abraham Lincoln'],
        'Resposta': 1,
    },
    {
        'Pergunta': 'Qual é a capital de São Paulo?',
        'Opções': ['Goiania', 'Rio de Janeiro', 'Ipanema', 'São Paulo'],
        'Resposta': 3,
    }
]

correct = 0

for id_question, question in enumerate(questions):
    print(f'{id_question+1}º Pergunta: {question['Pergunta']}')
    print('Opções:')

    for index, option in enumerate(question['Opções']):
        print(f'{index+1}) {option}')

    answer = input('Escolha uma opção => ')
    
    if answer.isdigit():
        int_answer = int(answer)
        if (int_answer - 1) == question['Resposta']:
            correct += 1
            print('Acertô mizeravi 👍')
        
        else:
            print('Não foi dessa vez 👎')

    else:
        print('Resposta inválida. 🤷‍♂️')

    print()

print(f'Você acertou {correct} de {len(questions)} perguntas')
if correct == len(questions):
    print('Parabéns você é um gênio.🤴')
elif correct >= 3:
    print('Parabéns você é um quase gênio. 👨‍🎓')
else:
    print('Que pena você não é um gênio.🤦‍♀️')