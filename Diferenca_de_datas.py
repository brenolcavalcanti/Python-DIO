from datetime import date, datetime

def contador_de_dias ():
    print ('--------------------')
    print ('  CONTADOR DE DIAS')
    print ('--------------------')
    d1 = int(input('Digite o dia da primeira data:'))
    m1 = int(input('Digite o mês da primeira data:'))
    a1 = int(input('Digite o ano da primeira data:'))
    d2 = int(input('Digite o dia da segunda data:'))
    m2 = int(input('Digite o mês da segunda data:'))
    a2 = int(input('Digite o ano da segunda data:'))
    data1 = date(a1,m1,d1)
    data2 = date(a2,m2,d2)
    dif = data1 - data2
    print(dif)

contador_de_dias()
