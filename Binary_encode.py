test = input("Message to be Encoded--->>>")
res = ' '.join(format(ord(x), 'b') for x in test)
print (" ")
print("Encoded Message--->>" + " " + str(res))

