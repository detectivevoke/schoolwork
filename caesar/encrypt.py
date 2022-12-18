import string

shift = 2
message = "This Is a Message."

class Caeser:
    
    def __init__(self,shift):
        self._alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o","p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        self._shift = shift
    def encrypt(self,_string):
        self._str = ""
        for letter in _string:
            if letter in string.punctuation: 
                self._str += letter
            elif letter == " ":
                self._str += letter
            else:
                if letter in string.ascii_uppercase: up = True
                pos = self._alphabet.index(str(letter).lower())
                new = pos + int(self._shift)
                if new >= 26:new = new-26
                _pl = self._alphabet[new]
                if up: self._str += _pl.upper()
                else:
                    self._str += _pl.upper()
        return True
c = Caeser(shift)
enc = c.encrypt(message)
if enc:
    print(c._str)   
else:
    print("Error has occured.")