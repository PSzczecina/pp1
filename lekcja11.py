#task8
def task8():
    def ms_to_kmh(ms):
        result = ms*3600/1000
        return result
    print(ms_to_kmh(10))

#task9
def task9():
    result = lambda ms: ms*3600/1000
    speed = 35
    print(f"{speed} m/s = {result(speed)} km/h")

#task10
def task10():
    length = int(input("enter distance: "))
    hour = int(input("enter traveled hours: "))
    minute = int(input("enter traveled minutes: "))
    def avg_speed(distance, hours, minutes):
        result = distance/(hours+(minutes/60))
        return result
    print(avg_speed(length, hour, minute))

#task11
def task11():
    length = int(input("enter distance: "))
    hour = int(input("enter traveled hours: "))
    minute = int(input("enter traveled minutes: "))
    avg_speed = lambda distance, hours, minutes: distance/(hours+(minutes/60))
    print(avg_speed(length, hour, minute))

def taskQ():
    arr = [2,5,4,7]
    y = list(map(lambda x:x**2 , arr))
    print(sum(y))


def task15():
    text = 'I completely agree with you'
    words = text.split()
    letters = list(map(lambda x: len(x),words))
    #for i in range(len(words)):
    #    words[i] = len(words[i])
    print(letters)

def task16():
    stock = [(20,5.50),(15,8.30),(37,3.85),(4,11.60)]

    total_value = sum(map(lambda x: x[0]*x[1],stock))
    #for el in range(len(stock)):
    #    stock[el]=stock[el][0]*stock[el][1]
    print(total_value)

def taskX():
    arr = [2,5,4,7]
    y = filter(lambda x: x>4,arr)
    print(list(y))

def taskABC():
    arr = [2,5,8,3,5,10,42]
    result = list(filter(lambda x: x%2==0, arr))
    print(result)


taskABC()