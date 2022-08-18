# contador_letras = lambda lista: [len(x) for x in lista]

# lista_animais = ['cachorro', 'gato', 'elefante']
# print(contador_letras(lista_animais))

# soma = lambda a, b: a + b     #Uma opção de trabalhar com lambda
# subtracao = lambda a, b: a-b

a = int(input('Qual o primeiro valor?'))
b = int(input('Qual o segundo valor?'))

calculadora = {
    'soma': lambda a, b: a+b,
    'subtracao': lambda a, b: a-b,
    'multiplicacao': lambda a, b: a*b,
    'divisao': lambda a, b: a/b,
}
soma = calculadora['soma']
subtracao = calculadora['subtracao']
multiplicacao = calculadora['multiplicacao']
divisao = calculadora ['divisao']

print('A soma é:', soma(a,b), 'A substração é: ', subtracao(a,b),'A multiplicação é:', multiplicacao(a,b),
      'A divisão é:', divisao(a,b))
