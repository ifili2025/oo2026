class Resistor:
    def __init__(self,r,maxN):
        self.r=r
        self.maxN=maxN
    def getCurrent(self,u):
        return u/self.r
    def getPower(self, u):
        return u*self.getCurrent(u)
    def isVoltageAllowed(self,u):
        return self.getPower(u) <= self.maxN
r1=Resistor(220,0.25)
print(r1.getCurrent(5), r1.getPower(5), r1.isVoltageAllowed(5))
print(r1.getCurrent(12), r1.getPower(12), r1.isVoltageAllowed(12))

m=[r1,Resistor(220,1),Resistor(110,1), Resistor(4700, 0.25)]

def leiaSobivad(takistid, u):
    return [t for t in takistid if t.isVoltageAllowed(u)]
for t in leiaSobivad(m,12):
    print(t.r, t.maxN)