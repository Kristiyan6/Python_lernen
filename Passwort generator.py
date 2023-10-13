import random

small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
'u', 'v', 'w', 'x', 'y', 'z']

capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
'U', 'V', 'W', 'X', 'Y', 'Z']

letters = small_letters + capital_letters

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']




Buchstaben= int(input("Eingabe der Anzahl an Buchstasben \n"))

Sonderzeichen= int(input("Eingabe der Anzahl der Sonderzeichen \n"))

Zahlen= int(input("Eingabe der Anzahl an Zahlen \n"))

#Passwort =random.choice(letters,numbers,symbols)

Passwort = []


for _ in range(0, Buchstaben):
    Buchstaben = random.choice(letters)
    Passwort.append(Buchstaben)


for _ in range(0, Sonderzeichen):
    Sonderzeichen = random.choice(symbols)
    Passwort.append(Sonderzeichen)

for _ in range(0, Zahlen):
    Zahlen = random.choice(numbers)
    Passwort.append(Zahlen)

random.shuffle(Passwort)

string_passwort = ""
for char in Passwort:
    string_passwort += char

print("Passwort:\t" + string_passwort)