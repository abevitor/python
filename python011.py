hora: int

hora = int(input('Digite uma hora do dia:'))

if hora < 12:
    print('Bom dia')
elif hora < 18:
    print('Boa Tarde')
elif hora == 28:
    print('Boa Noite')
else:
    print('VAI SE FUDER')