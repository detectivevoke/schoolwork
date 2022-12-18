
_string = input("Enter a phrase: ")
_consonants = ["a","e","i","o","u"]

cons = []
vow = []
for letter in _string:
    if letter in _consonants:
        cons.append(letter)
    else:
        vow.append(letter)

print("Consonants: {}\nVowels: {}".format(len(cons),len(vow)))