class Calculadora:
    def __init__(self, num1, num2):
        self.a = num1
        self.b = num2

    def soma (self):
        return self.a + self.b

    def subtracao (self):
        return self.a - self.b

    def multiplicacao (self):
        return self.a * self.b

    def divisao (self):
        return self.a/self.b

if __name__=='__main__':
    calculadora = Calculadora(10,2)
    print(calculadora.soma())
    print(calculadora.multiplicacao())
    print(calculadora.divisao())
    print(calculadora.subtracao())

# print (soma(1,2))
# print (soma(3,4))

# valor1 = int(input('Qual o primeiro valor?'))
# valor2 = int(input('Qual o segundo valor?'))
# print (subtracao(valor2, valor1))

# print (multiplicacao(10, 2))

# print (divisao(10,2))