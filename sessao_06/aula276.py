# datetime.timedelta e dateutil.relativetimedelta (calculando datas)
# Docs:
# https://dateutil.readthedocs.io/en/stable/relativedelta.html
# https://docs.python.org/3/library/datetime.html#timedelta-objects

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
fmt ='%d/%m/%Y %H:%M:%S'
init_date = datetime.strptime('20/04/1987 09:30:30', fmt)
finish_date = datetime.strptime('29/05/2024 08:20:20', fmt)
# print(finish_date > init_date)
# print(finish_date < finish_date)
# print(finish_date == init_date)
# print(finish_date - init_date)
# delta = finish_date - init_date
delta = timedelta(days=10, hours=2)
print(datetime.now() + delta)
print(relativedelta(finish_date, init_date))
print(datetime.now() + relativedelta(days=10, hours=2, seconds=10))
# print(delta.days, delta.seconds, delta.microseconds)
# print(delta.total_seconds())
