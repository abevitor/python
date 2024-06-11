horaganha = float(input('Digite quanto voce ganhar por hora: '))
numerohora = float(input('Digite quantas horas voce trabalhou esse mes: '))

salariobruto = horaganha * numerohora
IR = salariobruto * 0.11
INSS = salariobruto * 0.08
sindicato = salariobruto * 0.05

salarioliquido = salariobruto - (IR + INSS + sindicato)

print(f'o Salário líquido é de: {salarioliquido} ')