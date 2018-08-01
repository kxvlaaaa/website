#imports the ability to generate a random number
from random import *


#create the list of words you want to choose
aList = ["kelsey", "kat", "kayla", "kimani", "karen", "kauley"]

#generates a random number
aRandomIndex = randint(0, len(aList)-1)
print(aRandomIndex)
aRandomIndex2 = randint(0,len(aList)-1)
print(aRandomIndex2)


print(aList[aRandomIndex])
print(aList[aRandomIndex2])
