def whatsMyNum(a = 1, b = 1000):
    SEVEN = 7
    ONE = 1
    numList = []
    for num in range(a,b+1):
        if len(str(num)) >=2:
            numList.append(num)

    numSet = set()

    for num in numList:
        a = True
        i = 2
        while i < num and a == True:
            if num % i == 0:
                numSet.add(num)
                a = False
            else:
                i += 1

    for num in numList:
        if str(SEVEN) in str(num) or str(ONE) in str(num):
            numSet.add(num)

    for num in numList:
        sum = 0
        for digit in str(num):
            sum += int(digit)
        if sum > 10:
            numSet.add(num)

    for num in numList:
        sum = int(str(num)[0]) + int(str(num)[1])
        if sum % 2 == 0:
            numSet.add(num)

    for num in numList:
        if int(str(num)[-2]) % 2 != 0:
            numSet.add(num)

    for num in numList:
        if int(str(num)[-1]) != len(str(num)):
            numSet.add(num)

    for num in numSet:
        numList.remove(num)

    print(numList)

def main():
    whatsMyNum()


main()










