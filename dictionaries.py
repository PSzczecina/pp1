import json

def task7():





    person = {
    "name":"Marek",
    "surname":"Banach",
    "age":25,
    "hobby":["swimming","excursions"],
    "married":True,
    "phone":{"landline":"123444321","mobile":"777888999"}
    }

    print(person)
    print(person["name"])
    print(person["hobby"])
    person["surname"]="Nowak"
    print(person["surname"])
    person["married"]=not person["married"]
    print(person["married"])
    person.update({"gender":"male"})
    print(person)
    person["hobby"].append("bicycle")
    person["phone"].update({"work":"313131444"})

    print(person)

def task8():
    mobile = {
        "OS":"Android",
        "name":"Redmi 10C",
        "OS version":11,
        "broken screen":True,
        "contact numbers":{"home":367729394, "parent":213769420},
        "Ram":"much"
    }
    for key,value in mobile.items():
        x = type(value)
        if type(value)==type(mobile): #głupie to, ale
            print(f"{key}::")
            for k,v in value.items():
                print(f"    {k}:{v}")
        print(f"{key}:{value}")

def task9():
    countries=[
        {"name":"Poland","pop":38000000},
        {"name":"Germany","pop":83000000},
        {"name":"Turkey","pop":80000000},
        {"name":"France","pop":67000000},
        {"name":"Romania","pop":20000000},
        {"name":"Slovakia","pop":5500000}
    ]

    i=0
    print("COUNTRY     POPULATION")
    while i<len(countries):
        for key,value in countries[i].items():
            if key=="name":
                print(f"{value}    ",end="")
            elif key=="pop":
                print(f"{value}")
        i+=1

def task10():
    with open("data.json") as file:
         data = json.load(file)
    for element in data:
        for key,value in element.items():
            if type(value)==type([]):
                print(f("    "))
            print(f"{key}:{value}")

    #def checkElement():
        #if type(value)==type([]):



task10()