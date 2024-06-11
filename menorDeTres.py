#minha resolução
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))

if n1 < n2 < n3:
    print(f'MENOR = {n1}')
elif n2 < n1 < n3:
    print(f'MENOR = {n2}')

elif n3 < n2 < n1:
    print(f'MENOR = {n3}')



#outra forma de fazer

#n1 = int(input('Digite o primeiro valor: '))
#n2 = int(input('Digite o segundo valor: '))
#n3 = int(input('Digite o terceiro valor: '))

#if a < b and a < c:
                   #menor = a
    #elif b < c:
               #menor = b
  #else:
       #menor = c

     #print(f'MENOR ={menor}')

