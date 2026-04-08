# Pane näide käima, muuda andmeid.
# Koosta jadaühenduse klassist kaks eksemplari, katseta tulemusi mitmesuguse pinge korral. Võrdle käsitsi arvutatud tulemusi programmi pakutuga.
# Lisa jadaühenduse klassile käsklus kogu eralduva võimsuse leidmiseks.
# Väljasta jadaühenduse takistitest suurim takistus
# Väljasta jadaühendusest suurim ühele takistile langev pinge 5-voldise kogupinge juures
# Väljasta jadaühendusest suurim ühelt takistilt eralduv võimsus 5-voldise kogupinge juures
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


class SeriesCircuit:
    def __init__(self):
        self.resistors = []
    def addResistor(self, r):
        self.resistors.append(r)
    def getTotalResistance(self):
        total = 0
        for t in self.resistors:
            total += t.r
        return total
    def getTotalPower(self, u):
        total = 0
        current = u / self.getTotalResistance()
        for t in self.resistors:
            voltage = current * t.r
            total += t.getPower(voltage)
        return total
    def getMaxResistance(self):
        maxRes = 0
        for t in self.resistors:
            if t.r > maxRes:
                maxRes = t.r
        return maxRes
    def getMaxVoltage(self, u):
        current = u / self.getTotalResistance()
        maxVoltage = 0
        for t in self.resistors:
            voltage = current * t.r
            if voltage > maxVoltage:
                maxVoltage = voltage
        return maxVoltage
    def getMaxPower(self, u):
        current = u / self.getTotalResistance()
        maxPower = 0
        for t in self.resistors:
            voltage = current * t.r
            power = t.getPower(voltage)
            if power > maxPower:
                maxPower = power
        return maxPower
    def getMinVoltage(self, u):
        current = u / self.getTotalResistance()
        minVoltage = current
        for t in self.resistors:
            voltage = current * t.r
            if voltage < minVoltage:
                minVoltage = voltage
        return minVoltage
    def getMinPower(self, u):
        current = u / self.getTotalResistance()
        minPower = current
        for t in self.resistors:
            voltage = current * t.r
            power = t.getPower(voltage)
            if power < minPower:
                minPower = power
        return minPower

r1=SeriesCircuit()
r1.addResistor(Resistor(100, 0.25))
r1.addResistor(Resistor(200, 0.25))
r1.addResistor(Resistor(1000, 100))

print("Kokku resistance: ", r1.getTotalResistance())
print("Kokku power: ",r1.getTotalPower(5))
print("Maksimaalne resistance: ",r1.getMaxResistance())
print("Maksimalane voltage: ",r1.getMaxVoltage(5))
print("Maksimaalne power: ",r1.getMaxPower(5))
print("Minimaalne voltage: ", r1.getMinVoltage(5))
print("Minimaalne power: ", r1.getMinPower(5))

# def leiaSobivad(takistid, u):
#     return [t for t in takistid if t.isVoltageAllowed(u)]
# for t in leiaSobivad(m,12):
#     print(t.r, t.maxN)