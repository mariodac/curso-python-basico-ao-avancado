# Exercício: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
# python permite utilizar _ em numeros inteiros para separar centana, milhar, milhão, etc
value_loan = 1_000_000
years_payment = 5
qtd_parcels = years_payment * 12
parcel_payment = value_loan / qtd_parcels
init_date = datetime.strptime('20/12/2020', '%d/%m/%Y')
finish_date = init_date + relativedelta(years=years_payment)
print(init_date)
print(finish_date)
current_date = init_date + relativedelta(months=1)
index = 1
print(f"Data de pagamento da Parcela {index} = {current_date.strftime('%d/%m/%Y')}")
while current_date < finish_date:
    # if current_date == finish_date:
    #     break
    current_date += relativedelta(months=1)
    index += 1
    print(f"Data de pagamento da Parcela {index} = {current_date.strftime('%d/%m/%Y')} com o valor de R$ {parcel_payment:,.2f}")
print()
print(f"Você pegou R$ {value_loan:,} para pagar em {years_payment} anos ({qtd_parcels} meses) em parcelas de R$ {parcel_payment:,.2f}")