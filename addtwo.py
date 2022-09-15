a = [2,4,3]
b = [5,6,4]

def addTwoNumbers(l1,l2):
    l1.reverse()
    l2.reverse()
    # Making the lists into strings
    for i in range(len(l1)):
        l1[i] = str(l1[i])
    for i in range(len(l2)):
        l2[i] = str(l2[i])
    num1 = int(''.join(l1))
    num2 = int(''.join(l2))
    total = str(num1+num2)
    
    
    totalList = list(total)
    totalList.reverse()

    return totalList
    
    

c = addTwoNumbers(a,b)

print(c)