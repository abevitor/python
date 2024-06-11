salario1: float; salario2: float
nome: str; nome2: str
idade: int
idade2: int
sexo: str
sexo2: str
salariototal: float

nome = str(input('Nome da primeira pessoa: '))
nome2 = str(input('Nome da segunda pessoa: '))
idade = int(input('idade da primeira pessoa: '))
idade2 = int(input('idade da segunda pessoa: '))
sexo = str(input('sexo da primeira pessoa: '))
sexo2 = str(input('sexo da segunda pessoa: '))
salario1 = float(input('salario da primeira pessoa: '))
salario2 = float(input('salario da segunda pessoa:'))
salariototal = salario1 + salario2
idadetotal = idade + idade2

print(f' o nome da primeira pessoa é {nome} e da segunda pessoa é {nome2}. ')
print(f'A idade da primeira pessoa é {idade} e da segunda pessoa é {idade2}')
print(f' o sexo da primeira pessoa é {sexo} e da segunda pessoa é {sexo2}')
print(f' o salário da primeira pessoa é {salario1:.2f} e da segunda pessoa é {salario2:.2f}')
print(f' o total do salário dos dois é de: {salariototal}')
print(f'a idade somada dos dois da: {idadetotal} ')