fortnite = float(input('Digite uma temperatura em Fahrenheit: '))

if fortnite >= 32:
 fahrenheit = 5 * ((fortnite - 32) / 9)


 print(f'A temperatura em graus celcius é de {fahrenheit}')

else:

 print('Digite um valor que seja pelo menos 32 graus Fahrenheit')