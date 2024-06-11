sexo = str(input('M/F: '))
peso = str(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em centimetros: '))
masculino = ['m', 'M']
feminino = ['f', 'F']

if sexo in masculino:
    x = (72.7 * altura) - 58
    print(f'o peso ideal para a sua altura é de {x:.2f}, voce pesa no momento {peso}')

elif sexo in feminino:
    y = (62.1 * altura) - 44.7
    print(f'o peso ideal para a sua altura é de {y:;2f}, voce pesa no momento {peso}')

else:
    print('Essa opção é inexistente!')