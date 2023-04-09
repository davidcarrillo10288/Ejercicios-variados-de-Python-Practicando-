
def triangle(number):
    print('La primera forma de resolver, con str:',sep='/n')
    for i in range(1,number):
        new = (str(i)*i).ljust(0)
        print(new, sep="/n")

def triangle2(number):
    print('La segunda forma de resolver, sin str y con 2 for y operaciones matemáticas:',sep='/n')
    for i in range(1,number):
        new=0
        for j in range(i):
            new += i*10**j
        print(new, sep="/n")    

def triangle3(number):
    print('La tercera forma de resolver, en 2 lineas de codigo:',sep='/n')
    for i in range(1,number):
        print((i)*(10**(i))//9, sep="/n")

if __name__ == '__main__':
    number = int(input('Ingresa el numero a analizar: '))
    triangle(number)
    triangle2(number)
    triangle3(number)