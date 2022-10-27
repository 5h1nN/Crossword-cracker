

f = open("8-letters.txt", "r")
#print(f.read())

for x in f:
	if x[0] == "s" and x[4] == "l" and x[6] == "s":
		print(x,end="")