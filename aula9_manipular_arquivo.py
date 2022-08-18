import shutil

def escrever_arquivo (texto):
    arquivo = open('teste.txt', 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo (nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas (nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    # print(aluno_nota)
    soma = 0
    c=0
    aluno_nota = aluno_nota.split('\n')
    for x in aluno_nota:
        lista_notas = x.split(':')
        aluno = lista_notas[0]
        print(aluno)
        nota = float(lista_notas[1])
        print('nota:', nota)
        soma+=nota
        c+=1
    media_turma = soma/c
    print ('A média da turma é:', media_turma)

def copia_arquivo (nome_arquivo):
    shutil.copy(nome_arquivo, "E:/DOC'S/Desktop/")

def move_arquivo (nome_arquivo):
    shutil.move(nome_arquivo, "E:/DOC'S/Desktop")

if __name__ == '__main__':
    # media_notas('notas.txt')
    # move_arquivo('notas.txt')
    # copia_arquivo('notas.txt')
    #escrever_arquivo('Primeira linha\n')
    # aluno = 'Santino: 8\n'
    # atualizar_arquivo('notas.txt', aluno)
    # ler_arquivo('teste.txt')
