

def main(_string):
    _list = list(_string)
    _list.reverse()
    reversed_word = "".join(_list)
    

    if reversed_word.lower() == str(_string).lower():
        return True
    else:
        return False


_string = input("Enter a word to check if its a palindrome: ")
if main(_string):
    print(_string + " is a palindrome.")
else:
    print(_string + " is not a palindrome.")