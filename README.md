# Proiect1ASC
Numele echipei: Team, Assembly!
Numele echipei adverse: Echipa Registri
Cheia echipei adverse: ediEUnRegistru

Algoritm find_key_with_input:
1. pentru primele 30 de caractere din text, se aplică xor caracter cu caracter între input.txt și output.txt. Astfel, rezultă cheia de criptare, repetată până la o lungime de 30
de caractere.
2. pentru fiecare lungime x de la 10 la 15, se verifica dacă primele x caractere din string-ul obținut sunt egale cu următoarele x (bazându-ne pe faptul ca se tot repeta).
Dacă sunt, înseamnă că aceea este cheia de criptare.

Algoritm find_key_without_input:
Intâi se află lungimea cheii de criptare astfel:
1. Folosindu-ne de faptul că cheia de criptare se tot repetă, dacă cheia are o lungime x, inseamna că fiecare al x-ulea caracter va fi criptat cu acelasi caracter din cheie.
Astfel, pentru fiecare lungime posibilă (10-15 a cheii), trunchiem textul astfel încât sa rămână doar text criptat cu acelasi caracter din cheie (de exemplu, din 10 în 10 caractere).
2. Ne dăm seama care este lungimea corectă a cheii (si deci cand textul este criptat cu exact acelasi caracter) în momentul in care distributia caracterelor din textul criptat este
similară cu distribuția literelor din limba română. În programul nostru, aproximăm că primele cele mai uzuale 4 litere (a, e, i, t) ar trebui să reprezinte cam 40% din conținutul
textului. Dacă lungimea cheii e diferită de cea dupa care am trunchiat textul, distributia literelor o să fie aleatoare, nu o să predomine unele caractere.

După ce am aflat lungimea cheii, aflăm, pe rând, fiecare caracter din cheie astfel:
1. trunchiem textul, luând doar fiecare al x-ulea caracter, unde x e lungimea cheii de criptare, astfel încât fiecare element din textul obținut să fi fost criptat cu acelasi
caracter din cheie.
2. facem xor pe text cu toate valorile posibile ale unui caracter din cheie (A-z, 0-9). Ne dăm seama că am gasit caracterul corect atunci când, în textul decriptat, cele mai uzual
întâlnite caractere sunt cele întâlnite des in limba romana (în programul nostru, aproximam că literele e + a + i + t ocupă o proporție de 30-45%).
3. repetăm pentru fiecare caracter din cheie
