# Write a Python program that prints the character at index i in the string s.

# If the index is out of range, the program should print "i is out of range"

# If the string is empty, the program should print "Empty String"


print("Please enter a string")
s = input()


def printCharacterAtIndex(s):
    print("Please enter a character index")
    index = int(input())
    if len(s) == 0:
            print("Empty String")
    elif index > len(s) - 1:
        print("Index out of range")
    else:
        print(s[index])
        
        
        
printCharacterAtIndex(s)
