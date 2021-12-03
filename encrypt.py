import sys
fisier_text = sys.argv[2]
f = open(fisier_text, 'r')
continut = f.read()
f.close()
cheie = sys.argv[1]
continut_baza_10 = [ord(x) for x in continut]
cheie_baza_10 = [ord(x) for x in cheie]

cheie_repeat =[cheie_baza_10[x % len(cheie_baza_10)] for x in range(len(continut_baza_10))]
text_criptat =[(int(continut_baza_10[i]) ^ int(cheie_repeat[i])) for i in range(len(continut_baza_10))]
for i in range(len(text_criptat)):
    text_criptat[i] = bin(text_criptat[i])[2:].zfill(8)
text_criptat_final = "".join(text_criptat)
g = open(sys.argv[3], 'w')
g.write(text_criptat_final)
g.close()