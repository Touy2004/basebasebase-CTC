import base64

temp2 = ["O0w7", "b1lqZVdtaFdbXWRkV2BqXGssYDAu"]
decode = []

for select in range(0, 2):
    temp2[select] = base64.b64decode(temp2[select].encode('utf-8')).decode('utf-8')
    # print(temp2[select])
    decode.append(temp2[select])

print(decode[0] + "{" + decode[1] + "}")

#output
#;L;{oYjeWmhW[]ddW`j\k,`0.}