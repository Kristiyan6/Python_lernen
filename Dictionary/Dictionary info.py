# Dicitionaries -> Wörtebücher

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again",
    "Loop": "The action of doing something over and over again."
}

#dictionary = dict(a=1,b=2,c=3)
#print(dictionary)

print(programming_dictionary)

print(programming_dictionary["Function"])
print(programming_dictionary.get("Function"))

print(len(programming_dictionary))

# prüfen ob key in dict vorhanden ist
if "Function" in programming_dictionary:
    print("programming dictionary contains the key function")

if programming_dictionary.get("Function") is not None:
    print("programming dictionary contains the key function")

print(programming_dictionary.keys())

print(programming_dictionary.values())

# different types of loops
# for key in programming_dictionary.keys():
#     print(key)
#     print(programming_dictionary[key])

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# neues key value ipar einfügen
programming_dictionary["Variable"] = "Placeholder for a certain data piece"
print(programming_dictionary)

# ändern eines values
programming_dictionary["Variable"] = "Changed"
print(programming_dictionary)

# löschen eines elements aus dem dict
programming_dictionary.pop("Bug")
print(programming_dictionary)

# leeren eines dict
programming_dictionary.clear()
print(programming_dictionary)
