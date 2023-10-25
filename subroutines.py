import math

def task12():
    #task a
    max_digit = max(7,5,6,3,8,2)
    print(f"max number of (7,5,6,3,8,2) is {max_digit}")
    #task b
    binary_digit = bin(304)
    print(f"a binary version of decimal 304 is {binary_digit}")
    #task c
    hex_digit = hex(304)
    print(f"a hexadecimal version of decimal 304 is {hex_digit}")
    #task d
    unicode_character = ord('€')
    print(f"a unicode version of € is {unicode_character}")
    #task e
    absolute_value = abs(-17)
    print(f"the absolute value of -17 is {absolute_value}")

def task13():
    #A
    log = math.log10(5)
    print("a natural logarithm of 5 is",log)
    #B  co to jest to e?
    funny_letter = math.e**3
    print("e^3 is",funny_letter)
    #C
    square_root=math.sqrt(7)
    print("the square root of 7 is",square_root)
    #D
    sinus = math.sin(math.pi/2)
    print("sine of 90 degrees is",sinus)

def task14():
    def display_program_name():
        print("applied informatics")
    for i in range(4):
        display_program_name()

def task15():
    def phone_keyboard(number):
        if number%3 ==0:
            print(number)    
        else:
            print(number,end=" ")

    for i in range (9):
        phone_keyboard(i+1)

def task16():
    def product(x,y):
        return x*y
    a=3
    b=4
    print(f"the product of {a} and {b} is {product(a,b)}")

def task17():
    def different(n1, n2, n3):
        if n1 == n2 or n1 == n3 or n2 == n3:
            return False
        else:
            return True


    texta=input("Enter first number: ")
    textb=input("Enter first number: ")
    textc=input("Enter first number: ")

    if different(texta,textb,textc) == True:
        print(f"Numbers {texta}, {textb} and {textc} are different")
    else:
        print(f"Numbers {texta}, {textb} and {textc} are not all different")

def task18():
    def numbers(n):
        liczby=""
        for i in range(n):
            liczby+=str(i+1)+" "
        return liczby

    print(f"Numbers <1,15>: {numbers(15)}")
    print(f"Numbers <1,7>: {numbers(7)}")

# task 19

# task 20




#######task18()