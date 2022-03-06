n=int(input('Check if ur no. is prime or not'))
i=2
flag=0
while i<n:
    if n%i==0:
        flag=1
        break
    i=i+1
if flag==1:
    print('Not Prime')
else:
    print('Prime')