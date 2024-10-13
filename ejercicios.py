
for i in range(11):
 list = []
 if i%2 == 0: 
   list.append(i)
   print (list)    

result=0
for i in range (0,101):
  result +=i
print (result)

numero = int (input ("intriduce un numero para multiplicar"))
for i in range (0 , 11):
  res= numero * i
  print (res)

  def suma(a,b):
   return a + b
print (suma(5,5))

nueva = suma (9,9)
print (nueva)

tupla = tuple (range(1,101))
lista = []
for i in tupla:
  primo=True
  if(i==1 or i==2):
    lista.append(i)
    primo = False
  for j in range (2,i):
    if i%j==0:
      primo =False
  if primo:
    lista.append(i)

print (lista)


num = int (input("Introduce un numero que empiece el rango "))
num2 = int (input("Introduce un numero que termine el rango 9"))

lis=[]
fin=0
for i in range (num, num2):
    if i%2!=0:
        
        lis.append(i)
        for j in lis:
         fin += j
print (lis)
print (fin)



import random
numero_adivinar= random.randint(1, 100)
print ("intenta adivinar un numero del 1 al 100")

print(numero_adivinar)

while True:
 num = int(input("intriduce un numero "))
 if numero_adivinar > num:
    print ("El numero es mayor")
    num = int(input("intriduce un numero "))
 elif numero_adivinar < num:
    print("el numero es menor")
 else:
    print ("has acertado")   
    break 