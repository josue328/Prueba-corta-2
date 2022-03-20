
N = int(input("Ingrese ")) #Ingresa el numero 
I = 0 #numero invertido
D = 0 #digito 

while N > 0:
    N = int(input("Ingrese ")) #Ingresa el numero 
    D = N%10
    I = (I*10)+D
    N = (N-D)//10
    
print(I)
