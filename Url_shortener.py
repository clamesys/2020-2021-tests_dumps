import pyshorteners
url = input("Paste URL Here ----->>")
print ("URL----->>",
	pyshorteners.Shortener().tinyurl.short(url))
