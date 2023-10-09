import random
import word_list

print("Wilkommen zu Hangmen Spiel")
print(''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/ ''')

print("Verusche das Wort zu eratten")

words = word_list.word_list
word = random.choice(words)
#print(word)

guesses = ""
Versuche = 10

while Versuche > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=""),
        else:
            print("_", end=""),
            failed += 1

    if failed == 0:
        print("Du hast gewonne")
        break
    gues = input("Rate Buchstabe\n")
    guesses += gues

    if gues not in word:
        Versuche -= 1
        print("Falsch")
        print("Du hast", +Versuche, "Versuhe übrig")

    if Versuche == 0:
     print("Du hast verloren")
     print("Das richtige Wort war", word)

