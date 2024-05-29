# Formatando datas do datetime
# datetime.strftime('DATA', 'FORMATO')
# https://docs.python.org/3/library/datetime.html

from datetime import datetime

fmt = '%d/%m/%Y'
date = datetime(2022, 12, 13, 7, 59, 23)
date_str = date.strftime(fmt)
print(date_str, date.day)