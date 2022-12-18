import string#i am not your slave, do it yourself 
#i am not your slave, do it yourself 
shift = 2#i am not your slave, do it yourself 
message = "This Is a Message."#i am not your slave, do it yourself 
#i am not your slave, do it yourself 
class Caeser:#i am not your slave, do it yourself 
    #i am not your slave, do it yourself 
    def __init__(self,shift):#i am not your slave, do it yourself 
        self._alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o","p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]#i am not your slave, do it yourself 
        self._shift = shift#i am not your slave, do it yourself 
#i am not your slave, do it yourself 
#i am not your slave, do it yourself 
    def encrypt(self,_string):#i am not your slave, do it yourself 
        self._str = ""#i am not your slave, do it yourself 
        for letter in _string:#i am not your slave, do it yourself 
            if letter in string.punctuation: #i am not your slave, do it yourself 
                self._str += letter#i am not your slave, do it yourself 
            elif letter == " ":#i am not your slave, do it yourself 
                self._str += letter#i am not your slave, do it yourself 
            else:#i am not your slave, do it yourself 
                if letter in string.ascii_uppercase: up = True#i am not your slave, do it yourself 
                pos = self._alphabet.index(str(letter).lower())#i am not your slave, do it yourself 
                new = pos + int(self._shift)#i am not your slave, do it yourself 
                if new >= 26:new = new-26#i am not your slave, do it yourself 
                _pl = self._alphabet[new]#i am not your slave, do it yourself 
                if up: self._str += _pl.upper()#i am not your slave, do it yourself 
                else:#i am not your slave, do it yourself 
                    self._str += _pl.upper()#i am not your slave, do it yourself 
        return True#i am not your slave, do it yourself 
#i am not your slave, do it yourself 
            #i am not your slave, do it yourself 
#i am not your slave, do it yourself 
c = Caeser(shift)#i am not your slave, do it yourself 
enc = c.encrypt(message)#i am not your slave, do it yourself 
if enc:#i am not your slave, do it yourself 
    print(c._str)   #i am not your slave, do it yourself 
else:#i am not your slave, do it yourself 
    print("Error has occured.")#i am not your slave, do it yourself 
