print("decode +8 ASCII: ")
key = input()
temp = ""

for char in key:
	if char in {"{","}"}:
		temp+=char
	else:
		temp += chr(ord(char) + 8)
		
print(temp)