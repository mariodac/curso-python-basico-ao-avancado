# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datatime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datatime.fromtimestamp(Unix Timestamp) 
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz

from datetime import datetime
from pytz import timezone

data_str = '2024-05-29  00:48:52'
date_str_fmt = '%Y-%m-%d %H:%M:%S'


# date = datetime.strptime(data_str, date_str_fmt)
# date = datetime(2024, 5, 26, 6, 59, 13, tzinfo=timezone('Asia/Tokyo'))
date = datetime.now(timezone('America/Sao_Paulo'))
# print(date.timestamp())
print(datetime.fromtimestamp(1716673213.0))
print(date)

