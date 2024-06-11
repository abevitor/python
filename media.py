aluno = str(input('Digite seu nome: '))
notas = int(input('Quantas notas serão digitadas?: '))
soma = 0
for i in range(0,notas):
    x = int(input('Digite as notas de 0 a 10: '))

    soma = soma + x
    media = soma / 2

    print(f'a media de {aluno} [e {media} ')