
for zahl in range(1, 101):
 if zahl % 3 == 0 and int(zahl) % 5 == 0:
    print("fizzbuzz")
 elif zahl % 3 == 0:
    print("fizz")
 elif zahl % 5 == 0:
    print("buzz")
 else:
     print(zahl)
