a_binary_string = input("Message to be Decoded--->>>")
binary_values = a_binary_string.split()
ascii_string = ""
for binary_value in binary_values:
	an_integer = int(binary_value, 2)
	ascii_character = chr(an_integer)
	ascii_string += ascii_character
print ("")
print ("Decoded Message----->>>>>"+" "+ascii_string)

