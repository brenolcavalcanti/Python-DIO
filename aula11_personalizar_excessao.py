class Error (Exception):
    pass

class InputError (Error):
    def __init__(self, message):
        self.message = message


while True:              #Enquanto digitar um valor inválido o programa vai ficar repetindo
    try:
        x = int(input('Entre com uma nota de 0 a 10: '))
        print (x)
        if x>10 or x<0:
            raise InputError('Valor inválido! Apenas entre 0 ou 10!')
        break                #Quando digitar um valor válido, o break vai tirar do loop
    except ValueError:
        print('Valor inválido. Deve-se digitar apenas números')
    except InputError as ex:
        print (ex)
