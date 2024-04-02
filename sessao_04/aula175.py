from itertools import groupby
# groupby - agrupando valores (itertools)
# para realizar o agrupamento corretamente, a lista deve estar ordenada
students = [
    {'nome': 'Mario', 'nota': 'A'},
    {'nome': 'Victor', 'nota': 'B'},
    {'nome': 'Mikaele', 'nota': 'D'},
    {'nome': 'Guilherme', 'nota': 'A'},
    {'nome': 'João', 'nota': 'C'},
    {'nome': 'Dave', 'nota': 'B'},
    {'nome': 'Leonardo', 'nota': 'F'}
]

def students_sorted(student):
    return student['nota']

grades = ['a', 'a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'a']
groups = groupby(sorted(grades))

for chave, group in groups:
    print(chave)
    print(list(group))


sorted_students = sorted(students, key=students_sorted)

groups_students = groupby(sorted_students, key=students_sorted)
print('ALUNOS')
for chave, group in groups_students:
    print(chave)
    for student in group:
        print(student)
