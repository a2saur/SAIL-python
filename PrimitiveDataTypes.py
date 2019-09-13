import sys

myInt = 21
myFloat = 85.1
myString = "Made by Alexa"
myBoolean = True

byte = sys.getsizeof(myInt)
intFact = "Integers take up about 2 bytes (16 bits). This one takes up "
intFact += str(byte)

num = sys.getsizeof(myBoolean)
boo = "Boolean variables can either take up 24 or 28 bytes. 24 if the value is false, and 28 if it\'s true. This one takes up "
boo += str(num)

byte = sys.getsizeof(myString)
strFact = "Strings take up 49 bytes plus an extra byte for every character. This one takes up "
strFact += str(byte)

byte = sys.getsizeof(myFloat)
fltFact = "Floats take up 24 bytes. This one takes up "
fltFact += str(byte)


types = ['integer:', 'float:', 'string:', 'boolean:']
items = [myInt, myFloat, myString, myBoolean]

intFacts = [intFact]
fltFacts = [fltFact, "The word float is short for \"Floating Point Number\" because the decimal/binary point can float around (it can be placed anywhere in the number)"]
strFacts = [strFact, "In python, the computer knows that this is a string because it starts and ends with either \"quotation marks\" or \'single quotation marks\'"]
booFacts = [boo]

facts = [intFacts, fltFacts, strFacts, booFacts]

for x in range(4):
    print("This is an example of a(n)", types[x], "\n", items[x])
    for n in facts[x]:
        print(n)
    print('\n')