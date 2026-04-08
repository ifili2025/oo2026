#Loo programmiga kolm takistit. Esimese takistus 110 oomi, teise takistus 220 oomi, kolmanda takistus 4700 oomi (ehk 4,7 kilooomi). Arvuta iga takisti puhul vool 5-voldise pinge korral.
#Paiguta need kolm takistit massiivi. Rakenda igaühele pinge 5 volti, liida kokku tekkivad voolud nagu juhtub rööpühenduse korral
totals = []
class Resistor:
    def __init__(self, r):
        self.r = r
    def get_current(self, u):
        return u / self.r
class ResistorRun1:
    @staticmethod
    def main():
        r1=Resistor(110)
        r2=Resistor(220)
        r3=Resistor(4700)
        totals.append(r1.get_current(5))
        totals.append(r2.get_current(5))
        totals.append(r3.get_current(5))
if __name__ == "__main__":
    ResistorRun1.main()


print (totals)
summa = sum(totals)
print(summa)

