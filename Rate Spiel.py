import random

ratezahl = random.randint(0, 100)
Versuch = 0
aktiv = True

while aktiv:
    Versuch = Versuch + 1
    print()
    print(Versuch)
    benutzereingabe = int(input("Bitte Zahl eingeben: "))

    if benutzereingabe == ratezahl:
        print("Gewonnen! Die geheime Zahl ist nicht mehr geheim")
        aktiv = False
        break
    elif benutzereingabe > ratezahl:
        print("deine geratene Zahl ist zu groß")
    else:
        print("deine geratene Zahl ist zu klein")

    if (Versuch == 7):
        print("Du hast verloren")
        print("Es war die Zahl " + str(ratezahl))
        aktiv = False
print("Ende des Spiels")

