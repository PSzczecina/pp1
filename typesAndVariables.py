"""
################################################
zad 6

a.	50  -- int
b.	149.17 -- float
c.	4 * 7 -- int
d.	4.0 * 7 -- float
e.	"Krakow University of Economics" -- str
f.	True -- bool
g.	2 > 5 -- bool

"""
'''
################################################
zad 7 

a.	3 - 2 + 1       -- 2 operatory, 3 zmienne, wynik 2, int             + +
b.	5 + 10 * 5      -- 2 operatory, 3 zmienne, wynik 55, int            + +
c.	4 + 4 / 2 ** 2  -- 3 operatory, 4 zmienne, wynik 5, int             +-  5.0 - float
d.	4 % 3 % 2 % 1   -- 3 operatory, 4 zmienne, wynik 1  int             - +
e.	1 + 2 % 3 ** 4 * 5  -- 4 operatory, 5 zmiennych, wynik ***, int     -
f.	True != False   -- 1 operator, 2 zmienne, wynik True/1, bool        +
'''

def task7():
    print(3-2+1)
    print(5+10*5)
    print(4+4/2**2)
    print(4%3%2%1)
    print(1+2%3**4*5)
    print(True!=False)


def task8():
    numer1 = 71
    numer2 = 14
    result = numer1 + numer2
    print('numer 1: ',numer1)
    print('numer 2: ',numer2)
    print('result: ',result)

def task9():
    n1, n2, n3, n4, n5 = 5, 1, 8, 6, 3
    sum = n1+n2+n3+n4+n5
    print(sum)
    squareSum=n1*n1+n2*n2+n3*n3+n4*n4+n5*n5
    print(squareSum)
    quotient = n3/n5
    print(quotient)
    print(n3==n4)

def task10():
    print(f"My name is {'Paweł'}, I am {19} years old, and my height is {178} cm. In 6 years I will be {25} years old")


def task11():
    fatherMoney=int(input("enter father's income: "))
    motherMoney=int(input("enter mother's income: "))
    houseNumber=int(input("enter number of people in the family: "))
    print("total income: ",fatherMoney+motherMoney)
    print("income per capita: ",(fatherMoney+motherMoney)/houseNumber)

def task12():
    first_name=input("enter your first name: ")
    last_name=input("enter your last name: ")
    full_name = first_name+' '+last_name
    print(f'your filename is {full_name}')

def task13():
    cubeSide=int(input("enter the side of the cube: "))
    print(f'The surface of the cube is {cubeSide**3}')

def task14():
    radius=5
    pi=3.14
    area=4/3*pi*radius**3
    circumference = 2*pi*radius
    print(f"area is {area}\ncircumference is {circumference}")

def task15():
    celcius=int(input("provide me some celcius: "))
    fahrenheit = celcius*9/5+32
    print(f"fahrenheit is {fahrenheit}")

task15()