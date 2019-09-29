arr=[3,5,6,8,9,0, -3]
Y=3

def testersFunction():
    print ("Holy crap, this is a function and stuff.")

#testersFunction()

def loopTest():
    for x in range(0, 20):
        print("Hello World!")

#loopTest()

def b13one():
    arr = []
    for x in range (1,256):
        arr.append(x)
    print(arr)
    return(arr)

#b13one()

def b13two():
    x = 0
    for i in range(2,1002, 2):
       x += i
    print(x)
    return(x) 

#b13two()

def b13three():
    sum = 0
    for i in range (1,5001, 2):
        sum += i
        print(i)
        print(sum)
    return(sum)

#b13three()

def b13four(arr):
    sum = 0
    for i in arr:
       sum += i
    print(arr)
    print(sum)
    return(sum)

#b13four(arr=[3,5,6,8,9])

def b13five(arr):
    high = arr[0]
    for i in arr:
        if high < i:
            high = i
    print(high)
    return(high)

#b13five(arr=[3,5,6,8,9,0])

def b13six(arr):
    avg = 0.0
    sum = 0
    for i in arr:
        sum += i
    avg = sum / len(arr)
    print(avg)
    return(avg)

#b13six(arr=[3,5,6,8,9,0])

def b13seven():
    arr = []
    for i in range(1,51,2):
        arr.append(i)
    print(arr)
    return(arr)

#b13seven()

def b13eight(arr, Y):
    count = 0
    for i in arr:
        if Y < i:
            count += 1
    print(count)
    return(count)

#b13eight(arr, Y)

def b13nine(arr):
    counter = 0
    for i in arr:
        arr[counter] = i * i
        counter += 1
    print(arr)
    return(arr)

#b13nine(arr)

def b13ten(arr):
    counter = 0
    for i in arr:
        if i < 0:
            arr[counter] = 0
        counter += 1
        print(counter)
    print(arr)
    return(arr)

#b13ten(arr)

def b13eleven(arr):
    newNums = [arr[0], arr[0], 0]
    for i in arr:
        if i > newNums[0]:
            newNums[0] = i
        if i < newNums[1]:
            newNums[1] = i
    for i in arr:
        newNums[2] += i
    newNums[2] = newNums[2] / len(arr)
    print(newNums)
    return(newNums)
    
#b13eleven(arr)

def b13twelve(arr):
    temp = arr[0]
    arr[0] = arr[len(arr)-1]
    arr[len(arr)-1] = temp
    print(arr)
    return(arr)

#b13twelve(arr)

def b13thirteen(arr):
    counter = 0
    for i in arr:
        if i < 0:
            arr[counter] = "Dojo"
        counter += 1
    print(arr)
    return(arr)

#b13thirteen(arr)

