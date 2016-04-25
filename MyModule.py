import random

def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction:
    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return  str(self.num)+"/"+str(self.den)

    def show(self):
        print (self.num,"/",self.den)

    def __add__(self, otherfraction):
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum

if __name__ == '__main__':
    x = Fraction(1,2)
    rand1 = random.randint(1,10)
    rand2 = random.randint(1,10)
    y = Fraction(rand1,rand2)
    print (x+y)
    print (x==y)