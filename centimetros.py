centimetros = str(input('Qual a unidade de tamanho que vc quer utilizar?: '))

cm = ['centimetros', 'Centimetros','CENTIMETROS','cm','Cm','CM']
m = ['metros','Metros', 'METROS','m','M']
km = ['km','Km','KM','kilometros','Kilometros','KILOMETROS']

if centimetros in cm:
    valor = float(input('Digite o valor: '))
    x = valor / 100000
    x1 = valor / 100
    print(f'O valor em metros é de {x1} e o valor em km é de {x}')

elif centimetros in m:
    valor = float(input('Digite o valor: '))

    y = valor * 10
    y1 = valor / 1000

    print(f'O valor em centimetros é de {y:.2f} e em km é de {y1:.2f}')

elif centimetros in km:
    valor = float(input('Digite o valor: '))

    z = valor * 10000
    z1 = valor * 1000

    print(f'O valor em metros é de {z1:.2f} e em centimetros é {z:.2f}')
else:
    print('error')






