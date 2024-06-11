inteiro = int(input('Digite um número inteiro: '))
inteiro2 = int(input('Digite um número inteiro: '))
real = float(input('Digite um número real: '))
operacao = str(input('potencia/soma/produto: '))
potencia = ['Potencia', 'potencia', 'POTENCIA']
produto = ['Produto', 'produto', 'PRODUTO']
soma = ['Soma', 'soma', 'SOMA']

if operacao in soma:
   x = (inteiro * 3) + real
   print(f'{x} soma selecionada')

elif operacao in produto:
    y = (inteiro * 2) * real
    print(f'{y} produto selecionado')

elif operacao in potencia:
    z = real * real * real
    print(f'{z} potencia selecionada')

else:
    print('essa opção não está disponivel, tente novamente!')
