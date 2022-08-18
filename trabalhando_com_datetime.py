from datetime import date, time, datetime, timedelta

def trabalhando_com_datetime ():
    data_e_hora = datetime.now()
    print(data_e_hora.strftime('%d/%m/%Y, %H:%M:%S'))
    tupla = ('segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado', 'domingo')
    print ('Hoje é', tupla[data_e_hora.weekday()])
    data_criada = datetime(2018, 6, 20, 15, 30, 20)
    print(data_criada.strftime('%c, %d/%m/%Y, às %H:%M:%S'))
    data_string = '01/01/2019'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y')
    print(data_convertida)

def trabalhando_com_date():
    data_atual = date.today()
    print(data_atual.strftime('%d/%m/%Y'))
    data_atual_str = data_atual.strftime('%A, %B, %Y')
    print (data_atual_str)

def trabalhando_com_time ():
    horário = time(minute=18)
    print(horário)

if __name__ == '__main__':
    # trabalhando_com_date()
    # trabalhando_com_time()
    # trabalhando_com_datetime()
