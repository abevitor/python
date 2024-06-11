numero = int(input('Quantos numeros serão mostrados na tela?: '))

vet: [float] = [0 for x in range(numero)]

for i in range(0,numero):
    vet[i] = int(input('Digite os numeros: '))

    print()
    print('numeros digitados: ')
    for i in range(0,numero):
        print(f'numeros escolhidos: {vet[i]:.1f}')
