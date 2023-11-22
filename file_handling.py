def task8():
    file = open('countries.txt','r')
    file_content = file.read()
    print(file_content)
    file.close()

def task9():
    file = open('countries.txt','r')
    counter = 0
    for line in file:
        counter+=1
        print(f"{counter}. {line}",end="")
    file.close()

def task10():
    file = open("speech.txt",'r')
    for line in file:
        print(line,end="")
    file.close()

def task11():
    file = open("numbers.txt","r")
    sum = 0
    print("numbers: ",end="")
    for line in file:
        print(line.strip('\n'),end=" ")
        sum+=int(line)
    print(f"\n{sum}")
    file.close()

def task12():
    name = "Nae Nae Baby"
    university = "Krakow University of Economics"
    field = "applied informatics"
    file = open("student.txt","w")
    file.write(name+"\n")
    file.write(university+"\n")
    file.write(field+"\n")
    file.close()

def task13():
    movie_titles = ["Star Wars","Terminator","Cowboy Bebop","Oppenheimer","Barbie"]
    file = open("movies.txt","w")
    for element in movie_titles:
        file.write(element+"\n")
    file.close()

def task14():
    file = open("shopping.txt","w")
    read_product = True
    counter = 0
    while read_product:
        product = input("enter product name: ")
        if product!="":
            counter+=1
            file.write(product+"\n")
        else:
            read_product = False
    file.close()

def task15():
    with open("speech.txt","r") as f:
        for line in f:
            print(line,end="")
        f.close()

def task16():
    with open("speech.txt","r") as file:
        lines=0
        for line in file:
            lines+=1
        print("file name: speech.txt")
        print(f"number of lines: {lines}")
    file.close()

def task17():
    with open("navy.txt","r") as file:
        showLines = True
        currentLine=0
        decicion = "yes"
        for line in file:
            print(line,end="")
            currentLine+=1
            if (currentLine+1)%5==0:
                decicion = input("wanna see other lines? type anything for yes: ")
            if decicion =="":
                showLines=False
            if showLines == False:
                break
    file.close()

#jeżeli ma zapisywać po prostu na raz - to nwm jak to zrobić
def task18():
    mainfile = open("speech.txt","r")
    copyfile = open("copy.txt","w+")
    #copyfile.write(mainfile)
    mainfile.close()
    copyfile.close()

def task19():
    mainfile = open("speech.txt","r")
    copyfile = open("copy.txt","w+")
    for line in mainfile:
        copyfile.write(line)
    mainfile.close()
    copyfile.close()

def task20():
    meatFile = open("MeatAndFish.txt","r")
    breadFile = open("GrainsAndBread.txt","r")
    allProducts = open("allproducts.txt","w+")
    for line in meatFile:
        allProducts.write(line)
    for line in breadFile:
        allProducts.write(line)
    meatFile.close()
    breadFile.close()


##########################
#do zrobienia - 21>29 + 18
##########################



task20()