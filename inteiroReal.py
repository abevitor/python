inteiro = int(input('Quantos números inteiros voce deseja digitar?: '))
real = int(input('Quantos números reais voce deseja digitar: '))
tipoop = str(input('Qual o tipo da operação?: '))
produto = ['vezes', 'VEZES', 'Vezes']
soma = ['soma', 'Soma', 'SOMA']
potencia = ['potencia', 'Potencia', 'POTENCIA']

vet: [float] = [0 for x in range(inteiro)]

vet2: [float] = [0 for z in range(real)]

for i in range(0, inteiro):
    vet[i] = int(input('Digite os números inteiros: '))
    for i in range(0, inteiro):
        print(f'{ vet[i]}:  INTEIRO')

for k in range(0, real):
    vet[k] = input('Digite os números reais: ')
    for k in range(0, real):
        (print(f'{vet[k]}:  REAL'))

