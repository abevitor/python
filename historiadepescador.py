peso = float(input('Digite o peso do peixe: '))
nome = str(input('Digite o nome do peixe: '))
kgg = str(input('kilos ou gramas?: '))
kg = ['kg', 'KG', 'Kg', 'kG', 'KILOS', 'Kilos', 'kilos']
gramas = ['gramas', 'g', 'G', 'Gramas', 'GRAMAS']

if peso > 50 and kgg in kg:
    x = (peso - 50) * 4
    y = peso - 50
    print(f'O peso foi ultrapassado por {y} kilos e o valor da multa será {x}R$.')

elif peso > 50 and kgg in gramas:
    z = (peso / 100) * 4
    q = z - 50
    print(f'O peso foi ultrapassado por {q}kilos e o valor da multa será {z}R$')

else:
    print('o peso nao foi ultrapassado e voce nao pagará multa.')