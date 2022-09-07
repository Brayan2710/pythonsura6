#Ciclo Mientras 

#Declarar una variable centinela  o variable de control  para evaluar el ciclo 
from cgi import print_form
from nis import match


i=0
numero1=int(input("Diite el numero 1 "))
numero2=int(input("Diite el numero 2 "))


# Menu de opciones 
print("*Menu*")
print("1.sumar dos numeros ")
print("2.Restar dos numeros ")
print("3.Encontrar la raiz cuadrada de un numero ")
print("4. Multiplicar 2 numeros ")
print("5.salir ")
# programar la estructura del ciclo mientras 

while (i!=5):
    i=int(input("Digite una  Opcion del menu "))
    numero1=int(input("Diite el numero 1 "))
    numero2=int(input("Diite el numero 2 "))
    if(i==1):
        suma=numero1+numero2
    elif(i==2):
        resta=numero1-numero2
    elif(i==3):
        raiz= match.pow(suma)
    elif(i==4):
        multiplicar=numero1*numero2
    elif(i==5):
        break    
    else:
        print("Digita una opcion valida")
    
print("Salimos del while ")
