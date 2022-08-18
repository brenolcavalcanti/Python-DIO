from aula7_televisao import Televisao
from Calculadora1 import Calculadora
from aula8_contador_letras import contador_letras

if __name__ == '__main__':
    lista = ['cachorro', 'gato', 'elefante']
    print(contador_letras(lista))

    calculadora = Calculadora(15,2)
    print(calculadora.soma())
    
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
