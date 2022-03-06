import time
a = time.strftime("%A", time.localtime())
if a == "Friday":
	print ("today ok")
elif a == "Sunday":
	print ("time was changed manually")