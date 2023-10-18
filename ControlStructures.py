import os

def kulko_krzyzyk():
    turn=1
    board = [
            [" "," "," "],
            [" "," "," "],
            [" "," "," "]
        ]
    while True:
        #reset ekranu terminala
        os.system('cls' if os.name == 'nt' else 'clear')

        col=1
        print("    A   B   C")
        print("  ┏---+---+---┓")
        for x in board:
            print(f"{col} ",end="")
            for r in x:
                print(f"| {r} ",end="")
            print("|")
            print("  |---+---+---|")
            col=col+1

        print("now is the turn of player",turn)
        playerOption=input("Type the square to Cross. The pattern is 'Letter''Number' : ")
        while len(playerOption)!=2:
            playerOption=input("Incorrect pattern. Try again. The pattern is 'Letter''Number' : ")
        row, collumn="X","X"
        if playerOption[1]=="a":
            row=0
        elif playerOption[1]=="b":
            row = 1
        elif playerOption[1]=="c":
            row = 2

        if playerOption[0]=="1":
            collumn=0
        elif playerOption[0]=="2":
            collumn=1
        elif playerOption[0]=="3":
            collumn=2


        if turn==1:
            board[row][collumn]="O"
            turn==2
        elif turn==2:
            board[row][collumn]="X"
            turn==1




def task9():
    taskNumber=20
    taskCorrect=13
    if taskNumber/2 < taskCorrect:
        print("Test passed")

def task10():
    number = int(input("enter number: "))
    numOutput=number
    if number<0:
        numOutput=number*-1
    print(f"|{number}| = {numOutput}")

def task11():
    number=int(input("enter number: "))
    if number%2==0:
        print("number is even")
    else:
        print("number is odd")

def task12():
    person1Name=input("enter first person name: ")
    person1Age=int(input("enter first person age: "))
    person2Name=input("enter second person name: ")
    person2Age=int(input("enter second person age: "))
    if person1Age>=18 and person2Age>=18:
        print(f"both {person1Name} and {person2Name} are adults")
    elif person1Age<18 and person2Age<18:
        print(f"both {person1Name} and {person2Name} are not adults")
    elif person1Age<18 and person2Age>-18:
        print(f"{person1Name} is not an adult")
    else:
        print(f"{person2Name} is not an adult")

def task13():
    num1=int(input("enter number 1: "))
    num2=int(input("enter number 2: "))
    if num1 >=0 or num2 >= 0:
        print(f"at least one of entered numbers {num1} and {num2} is not negative")
    else:
        print(f"both numbers {num1} and {num2} are negative")

def task17():
    x=1
    result=0
    while x<=5:
        result=result+x
        x=x+1
    print(result)

def task18():
    x=1
    result=0
    while x<=10:
        print(f"1/{x} = {1/x}")
        x=x+1

def task19():
    x=2
    result=0
    while x<=10:
        result=result+x
        x=x+2
    print(result)


task19()


# kulko_krzyzyk()