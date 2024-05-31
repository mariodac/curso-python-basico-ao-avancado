# Usando calendar para calendários e datas
# https://docs.python.org/3/library/calendar.html
# calendar é usado para coisas genéricas de calendários e datas
# Com calendar, você pode saber coisas como:
# - Qual o nome e número do dia de determinada data (ex.: weekday)
# - Criar um calendário em si (ex.: monthcalendar)
# - Trabalhar com coisas específicas de calendários (ex.: calendar, month)
# Por padrão dia da semana começa em 0 até 6
# 0 = segunda-feira | 6 = domingo

import calendar

# imprimir o calendario do ano
# print(calendar.calendar(2022))
# imprimir o calendario do mês
# print(calendar.month(2022, 12))
# print(calendar.monthrange(2022, 12))
# print(list(calendar.day_name))
# obtem o primeiro dia da semana do mês informa e ultimo numero do dia do mês
# first_day, last_day = calendar.monthrange(2022, 12)
# print(calendar.day_name[first_day])
# print(calendar.weekday(2022, 12, last_day))
# print(calendar.monthcalendar(2022, 12))
for week in calendar.monthcalendar(2022, 12):
    for day in week:
        if day == 0: continue
        week_day = calendar.weekday(2022, 12, day)
        print(calendar.day_name[week_day])
