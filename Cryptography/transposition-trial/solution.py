transposed_msg = open("message.txt", "r").read()

n=3
mugi = [transposed_msg[i:i+n] for i in range(0, len(transposed_msg), n)]
decode_lst = []

for i in range(len(mugi)):
    decode_lst.append(mugi[i][2]+mugi[i][0]+mugi[i][1])

print(''.join(decode_lst))
