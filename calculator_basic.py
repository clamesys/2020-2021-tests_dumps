print ("Welcome to my Calculator")
print (' ')
opperand = input('Press'+'\n'+
'A for Addition'+'\n'+
'S for Substraction'+'\n'+
'M for Multiplication'+'\n'+
'D for Division'+'\n'+
' '+'\n'+
':::::-----')
print (' ')
if  opperand == ('A') or opperand == ('a'):
	a = int(input('1st Number::---'))
	b = int(input('2nd Number::---'))
	print (a+b)
elif  opperand == ('S') or opperand == ('s'):
	a = int(input('1st Number::---'))
	b = int(input('2nd Number::---'))
	print (a-b)
elif  opperand == ('M') or opperand == ('m'):
	a = int(input('1st Number::---'))
	b = int(input('2nd Number::---'))
	print (a*b)
elif  opperand == ('D') or opperand == ('d'):
	a = int(input('1st Number::---'))
	b = int(input('2nd Number::---'))
	print (a/b)
else:
	print ("SORRY TRY AGAIN");
print (" ")
print ("THANK YOU")
print ("VISIT AGAIN");
