#--------------------- 1.1) 99 Bottles of Beer
def beerBottles(n):
    for i in range(n):
        print(n, "bottles of beer on the wall, ", n, "bottles of beer" " Take one down, pass it around, ")
        n = n-1
        print( "Take one down, pass it around,",  n, "bottles of beer on the wall")
    
hellos = int(input("How many bottles of beer should we start at?"))
beerBottles(hellos)

#----------------------- 1.2) Multiplication table
def multTable(h):
       for row in range(h):
        for col  in range(1,h+1):
            print(row*col,end="\t")
        print()
        
multiple = int(input("multiple number for tabel: "))
multTable(multiple)
#----------------------- 1.3) Summation of squares

def squareSum(n) :
    sm = 0
    for i in range(1, n+1) :
        sm = sm + (i * i)
    return sm

n = int(input("multiple number for tabel: "))
print(squareSum(n))
