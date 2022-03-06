max=int(input("please enter the maximum value: "))
evenSum=0
oddSum=0
num=1
while (num<=max):
    if (num%2==0):
        evenSum=evenSum+num
    else:
        oddSum=oddSum+num
    num+=1
print("The sum of Even numbers 1 to ", max, evenSum)
print("The sum of Even numbers 1 to ",max, oddSum)
