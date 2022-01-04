def incr (a):
    return (a+1)
def decr (a):
    while (a!=0):
        return (a-1)
    return (a)
def clr (a):
    while (a!=0):
        a=decr(a)
    return (a)
def assi (x1,x2):
    aux=1
    aux=clr(aux)
    x1=clr(x1)
    while (x2!=0):
        aux=incr(aux)
        x2=decr(x2)
    while (aux!=0):
        x1=incr(x1)
        x2=incr(x2)
        aux=decr(aux)
    return(x1)
def cero():
    z=2
    return (clr (z))
def suce(a):
    aux=3
    aux=incr(assi(aux,a))
    return aux


def G(a):
    z1=2
    return (assi(z1,a))
def H(a):
    z1=2
    return (incr(assi(z1,a)))
def suma (x1,x2):
    x3=1
    z1=2
    aux=3
    z1=G(x1)
    aux=assi(aux,x2)
    x2=clr(x2)
    while(aux!=0):
        x3=assi(x3,z1)
        z1=H(x3)
        x2=incr(x2)
        aux=decr(aux)
    return(z1)
def mult(x1,x2):
    aux=2
    z1=2
    z1=clr(z1)
    aux=assi(aux,x2)
    while (aux!=0):
        z1=assi(z1,suma(z1,x1))
        aux=decr(aux)
    return z1
def expo (x1,x2):
    aux1=2
    aux2=3
    z1=2
    
    z1=clr(z1)
    aux1=assi(aux1,x2)
    aux2=assi(aux2,x2)
    aux2=decr(aux2)
    while (aux1!=0):
        z1=assi(z1,mult(x1,suce(cero())))
        while(aux2!=0):
            z1=assi(z1,mult(z1,x1))
            aux1=decr(aux1)
            aux2=decr(aux2)
        return z1
    return (suce(cero()))
def pred (x1):
    z1=1
    z1=clr(z1)
    z1=assi(z1,x1)
    return (decr(z1))
def monus(x1,x2):
    aux=1
    aux=assi(aux,x2)
    z1=1
    z1=assi(z1,x1)
    while(aux!=0):
        z1=decr(z1)
        aux=decr(aux)
    return z1
def equ(x1,x2):
    a=3
    b=3
    aux=4
    z1=4
    a=assi(a,x1)
    b=assi(b,x2)
    aux=clr(aux)
    z1=clr(z1)
    
    z1=monus(a,b)
    aux=monus(b,a)
    z1=suma(z1,aux)
    z1=monus((suce(cero())),z1)
    return z1
def coci(x1,x2):
    z1=3
    z1=clr(z1)
    aux1=5
    aux1=assi(aux1,x1)
    
    aux2=5
    aux2=assi(aux2,x2)
    
    while(aux1!=0):
        while(aux2!=0):
            z1=suma(coci(pred(aux1),aux2),equ(aux1,suma(aux2,mult(coci(pred(aux1),aux2),aux2))))
            aux2=clr(aux2)
        aux1=clr(aux1)
    return z1
def fib(x1):
    z1=3
    z1=clr(z1)

    aux1=5
    aux1=assi(aux1,x1)

    aux1=decr(aux1)
    while(aux1!=0):
        aux1=decr(aux1)
        while(aux1!=0):
            aux1=decr(aux1)
            while(aux1!=0):
                
                aux1=assi(aux1,x1)
                z1=suma(fib(decr(aux1)),fib(decr(decr(aux1))))
                return z1

            return suce(z1)
        return suce(z1)
    return z1
def impa(x1):
    z1=3
    z1=clr(z1)

    aux1=5
    aux1=assi(aux1,x1)

    while(aux1!=0):
        return monus(x1,mult(2,coci(x1,2)))
    return z1
def fact(x1):
    z1=5
    z1=clr(z1)

    aux1=5
    aux1=assi(aux1,x1)

    aux2=4
    aux2=clr(aux2)
    aux2=incr(aux2)

    z1=incr(z1)
    while(aux1!=0):
        z1=mult(z1,aux2)
        aux2=incr(aux2)
        aux1=decr(aux1)
    return z1

def GF (x1,x2,t):
    return monus((suma (x1,1)),(suma((mult(t,x2)),x2)))
def div(x,y):
    z1=3
    z1=clr(z1)

    aux1=5
    aux1=assi(aux1,x)
    
    aux2=5
    aux2=assi(aux2,y)

    ite=6
    ite=clr(ite)

    z1=GF(aux1,aux2,ite)
    while(z1!=0):
        ite=incr(ite)
        z1=GF(aux1,aux2,ite)
    z1=assi(z1,ite)
    return z1
div(17,3)



def A(m,n):
    z1=3
    z1=clr(z1)

    aux1=5
    aux1=assi(aux1,m)
    
    aux2=5
    aux2=assi(aux2,n)
    
    while(aux1!=0):
        while(aux2!=0):
            z1=A((decr(aux1)),(A (aux1,(decr(aux2)))))
            return z1
        z1=A((decr(aux1)),(suce(cero())))
        return z1
    z1=incr(aux2)
    return z1

#A(3,6)
#impa(5)
#fact(6)


def menu():
    os.system('cls')
    print('Este es un interprete de recursividad empleando un lenguaje de programación esencial\n')
    print('accede a las operaciones con los numeros del 1 a 12, cada función requiere ciertos parametros\nde entrada y las operaciones disponibles son:\n')
    print(' 1.- suma(x,y)')
    print(' 2.- multiplicación(x,y)')
    print(' 3.- exponenciación(x,y)')
    print(' 4.- predecesor(x)')
    print(' 5.- resta(x,y)')
    print(' 6.- igualdad(x,y)')
    print(' 7.- cociente(x,y), parte entera')
    print(' 8.- Elemento x de la seriue de fibonacci')
    print(' 9.- identificación si un numero es impar')
    print('10.- factorial(x)')
    print('11.- división (x,y)')
    print('12.- función de ackermann (x,y)')



import os
while True:
    menu()
    sop=input('selecciona alguna operación o q para salir\n')
    if(sop.isdigit() and int(sop) in range(1,13)):
        if(int(sop)==1):
            x,y=input('\n\n¿que valores seran sumados? e.g 5,4\n').split(',')
            print('el resultado de la suma de',x,'y',y,'es',suma(int(x),int(y)))
            input('pulsa una tecla para continuar')
        elif(int(sop)==2):
            x,y=input('\n\n¿que valores seran multiplicados? e.g 5,4\n').split(',')
            print('el resultado de la multiplicación de',x,'y',y,'es',mult(int(x),int(y)))
            input('pulsa una tecla para continuar')
        elif(int(sop)==3):
            x,y=input('\n\n¿que numero sera exponenciado? e.g 5,4 = 5^4\n').split(',')
            print('el resultado de la exponenciación de',x,'a la',y,'es',expo(int(x),int(y)))
            input('pulsa una tecla para continuar')
        elif(int(sop)==4):
            x=input('\n\n¿A que numero se le busca un predecesor?\n')
            print('el predecesor de',x,'es',pred(int(x)))
            input('pulsa una tecla para continuar')
        elif(int(sop)==5):
            x,y=input('\n\n¿que valores seran restados? e.g 5,4=5-4\n').split(',')
            print('el menor numero que se puede obtener es cero, no existen los negativos')
            print('el resultado de la resta de',x,'y',y,'es',monus(int(x),int(y)))
            input('pulsa una tecla para continuar')
        elif(int(sop)==6):
            x,y=input('\n\n¿que valores buscan ser comparados? e.g 5,4 ¿es 5 igual a 4 ?\n').split(',')
            if(equ(int(x),int(y))):
                print(x,'y',y,'son iguales')
            else:
                print(x,'y',y,'no son iguales')
            input('pulsa una tecla para continuar')
        elif(int(sop)==7):
            x,y=input('\n\n¿cual es el cociente entre 2 numeros? e.g 5,4=5/4\n').split(',')
            print('la parte entera del cociente de',x,'y',y,'es',coci(int(x),int(y)))
            input('pulsa una tecla para continuar')
        elif(int(sop)==8):
            x=input('\n\n¿que valor se busca saber si es impar? e.g 5 ¿es 5 impar?\n')
            if(impa(int(x))):
                print(x,'es impar')
            else:
                print(x,'es par')
            input('pulsa una tecla para continuar')
        elif(int(sop)==9):
            x=input('\n\n¿Que numero de la serie de Fibonacci se quiere conocer?\n')
            print('el elemento',x,'de la serie de fibonacci es',fib(int(x)))
            input('pulsa una tecla para continuar')
        elif(int(sop)==10):
            x=input('\n\n¿el factorial de que numero se desea conocer? e.g !4=24\n')
            print('el factorial de',x,'es',fact(int(x)))
            input('pulsa una tecla para continuar')


        elif(int(sop)==11):
            x,y=input('\n\n¿que valores buscan ser divididos? e.g 5,4 ¿cuanto es 5/4 ?\n').split(',')
            print('la parte entera de la división de',x,'y',y,'es',div(int(x),int(y)))
            input('pulsa una tecla para continuar')
        elif(int(sop)==12):
            x,y=input('\n\nIngrese dos numeros para calular la función de Ackermann e.g 5,4\n').split(',')
            print('el resultado de la función de Ackermann de',x,'y',y,'es',A(int(x),int(y)))
            input('pulsa una tecla para continuar')

    elif(sop=='q'):
        os.system('cls')
        print('adios vaquero')
        break  
    else:
        os.system('cls')
        input('opción no listada, oprime alguna tecla para continuar')
        os.system('cls')