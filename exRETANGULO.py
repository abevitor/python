
r1 = float(input('Qual o tamanho da base do retangulo?: '))
r2 = float(input('Qual o tamanho da Altura do retangulo?: '))


area = r1 * r2
perimetro = 2 * (r1 + r2)
pitagoras = r1 ** 2 + r2 ** 2
diagonal = pow(pitagoras, 0.5)

print(f'A base do retangulo é de: {r1}')
print(f'A altura do retangulo é de: {r2}')
print((f'A area do retangulo é de: {area:.4f}'))
print(f'O perimetro do retangulo é de: {perimetro}')
print(f'A diagonal do retangulo é de: {diagonal:.4f}')






