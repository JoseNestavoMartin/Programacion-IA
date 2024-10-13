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
    
