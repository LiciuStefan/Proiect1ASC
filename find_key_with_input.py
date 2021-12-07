f = open("output.txt", "rb")
text_output = f.read(30)
g = open("input.txt", "rb")
text_input = g.read(30)

text_xor = []
for char1, char2 in zip(text_input, text_output):
    text_xor.append(chr(char1 ^ char2))
cheie = ""

for i in range(6):
    if text_xor[:10+i] == text_xor[10+i:2*(10+i)]:
        cheie = "".join(text_xor[:10+i])
        break
print(cheie)
