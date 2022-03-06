import base64
message = input("Message to be Encoded--->>>")
message_bytes = message.encode('ascii')
base64_bytes = base64.b32encode(message_bytes)
base32_message = base64_bytes.decode('ascii')
print ("")
print ("Encoded Message--->>", base32_message)
