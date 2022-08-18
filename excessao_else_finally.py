lista = [10, 1]
try:
    divisao = 10 / 0
    numero = lista[1]
except ZeroDivisionError:
    print('Não é possível dividir por 0')
except IndexError:
    print('Erro ao acessar um índice inexistente')
except BaseException as ex:
    print ('Erro no programa:', ex)
else:                                    #Executa alguma situação se não tiver erro nenhum
    print('Não houve nenhum erro')
finally:                                 #executa independente se tiver algum erro ou não
    print('Sempre executa')