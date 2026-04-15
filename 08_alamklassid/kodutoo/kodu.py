class Toiduaine:
    def __init__(self, nimetus, valk, rasv, suhkur):
        self.nimetus = nimetus
        self.valk = valk
        self.rasv = rasv
        self.suhkur = suhkur
        
    def kontrolli_protsent(self):
        if self.valk + self.rasv + self.suhkur > 100:
            raise ValueError("Protsent ei tohi ületada 100")
        if self.valk < 0 or self.rasv < 0 or self.suhkur < 0:
            raise ValueError("Protsent ei tohi olla negatiivne")
        return True
        
class Toidukomponendid:
    def __init__(self, toiduaine, kogus):
        self.toiduaine = toiduaine
        self.kogus = kogus
    def rasvakogus(self):
        return self.toiduaine.rasv * self.kogus / 100
    def valkukogus(self):
        return self.toiduaine.valk * self.kogus / 100
    def suhkrukogus(self):
        return self.toiduaine.suhkur * self.kogus / 100
    def __str__(self):
        return f"{self.toiduaine.nimetus} {self.kogus}g {self.valkukogus()}g valku, {self.rasvakogus()}g rasva, {self.suhkrukogus()}g süsivesikuid"
        
class Toit:
    def __init__(self, nimetus, toidukomponendid):
        self.nimetus = nimetus
        self.toidukomponendid = toidukomponendid

    def valkukogus(self):
        kokku = 0
        for i in self.toidukomponendid:
            kokku += i.valkukogus()
        return kokku

    def rasvakogus(self):
        kokku = 0
        for i in self.toidukomponendid:
            kokku += i.rasvakogus()
        return kokku

    def suhkrukogus(self):
        kokku = 0
        for i in self.toidukomponendid:
            kokku += i.suhkrukogus()
        return kokku

    def toiduained_kogused(self, kogus):
        kogukaal = sum(i.kogus for i in self.toidukomponendid)
        for i in self.toidukomponendid:
            print(f"{i.toiduaine.nimetus}: {round(i.kogus * kogus / kogukaal, 2)}g")

    def kirjutamine_faili(self):
        faili_nimi = self.nimetus + ".txt"
        with open(faili_nimi, "w") as f:
            f.write(self.nimetus + "\n")
            for i in self.toidukomponendid:
                f.write(i.toiduaine.nimetus + " " + str(i.kogus) + "\n")

    def lugemine_failist(self, faili_nimi):
        with open(faili_nimi, "r") as f:
            self.nimetus = f.readline().strip()
            self.toidukomponendid = []
            for line in f:
                toiduaine, kogus = line.strip().split(" ")
                self.toidukomponendid.append(Toidukomponendid(Toiduaine(toiduaine, 0, 0, 0), int(kogus)))

t1 = Toiduaine("kartul", 40, 10, 50)
t2 = Toiduaine("hapukoor", 20, 20, 60)
t3 = Toiduaine("vorst", 20, 20, 60)
# print(t1.kontrolli_protsent())
# print(t2.kontrolli_protsent())
# print(t3.kontrolli_protsent())

k1 = Toidukomponendid(t1, 100)
k2 = Toidukomponendid(t2, 30)
k3 = Toidukomponendid(t3, 60)
# print(k1)
# print(k2)
# print(k3)

# toiduained = [k1, k2, k3]
# toiduained = Toit("Kartuli salat", toiduained)
# toiduained.toiduained_kogused(2000)

# toiduained.kirjutamine_faili()

to = Toit("", [])
to.lugemine_failist("Kartuli salat.txt")
to.toiduained_kogused(2500)