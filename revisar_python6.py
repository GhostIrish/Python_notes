from datetime import datetime, date, timedelta

data_atual = date.today()

# mostra o dia do sistema
print(date.today())

# formatado para o brasil
date_em_texto = f'{data_atual.day}/{data_atual.month}/{data_atual.year}'
print(date_em_texto)

hora = datetime.now()

hora_str = hora.strftime('%A %d %B %y  %I:%M')
print(hora_str)

daq_dois_dias = data_atual + timedelta(2)
print(daq_dois_dias)
