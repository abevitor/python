nome = str(input('Digite seu nome: '))
dias = int(input('Digite quantos dias por mes vc trabalha: '))
horas = float(input('Digite quantas horas por dia vc trabalha:'))
money = float(input('Digite quanto que vc ganha por hora: '))

salario = (dias * horas) * money

print(f'O salário atual de {nome} é {salario}')
