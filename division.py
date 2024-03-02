import random

def division(lowestnum,highestnum):
    a = random.randrange(lowestnum,highestnum)
    b = random.randrange(1,10)
    return str(a*b) + " / " + str(b) + " = ______"