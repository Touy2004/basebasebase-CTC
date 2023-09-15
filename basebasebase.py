import base64

print("Enter secret password to crack to code: ")
key = input()
temp = ""

for char in key:
	if char in {"{","}"}:
		temp+=char
	else:
		temp+=chr(ord(char)-8)
		
print(temp)

temp2 = temp[::-1][0:-1].split("{")
for select in range(0,2):
	temp2[select] = base64.b64encode(temp2[select].encode('utf-8')).decode('utf-8')


real_key = temp2[0]+"{"+temp2[1]+"}"
if real_key[::-1] == "}uADYssGXqB2VkRWXbdFatdVZql1b{7w0O":
	print("Crack!!!")
else:
	print("Wrong!!")