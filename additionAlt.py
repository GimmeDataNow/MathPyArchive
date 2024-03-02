import random

def additionAlt(lowestnum,highestnum):
    a = random.randrange(lowestnum,highestnum)
    b = random.randrange(lowestnum,highestnum)
    return str(a) + "  + ______ = " + str(a+b) 