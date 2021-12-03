import sys
f_input = open(sys.argv[1], 'r')
text = f_input.read()
f_input.close()

cheie_text = sys.argv[2]
cheie_b10 = [ord(char) for char in cheie_text]
text_sep = [text[8*i:8*i+8] for i in range(len(text)//8)]
text_b10 = [int(nr_binar, 2) for nr_binar in text_sep]
l_cheie = len(cheie_b10)
l_text = len(text_b10)

text_decriptat = []
for i in range(l_text):
    text_decriptat.append(chr(text_b10[i] ^ cheie_b10[i % l_cheie]))
output = ''.join(text_decriptat)

f_output = open(sys.argv[3], 'w')
f_output.write(output)
f_output.close()