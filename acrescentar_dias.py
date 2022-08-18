from datetime import date, timedelta

def contador_de_dias ():
    print ('--------------------')
    print ('  CONTADOR DE DIAS')
    print ('--------------------')
    d1 = int(input('Digite o dia da primeira data:'))
    m1 = int(input('Digite o mês da primeira data:'))
    a1 = int(input('Digite o ano da primeira data:'))
    delta = int(input('Quantos dias você quer acrescentar?'))
    data1 = date(a1,m1,d1)
    data2 = data1 + timedelta(delta)
    print(data2)

contador_de_dias()