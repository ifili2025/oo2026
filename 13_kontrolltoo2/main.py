class Toiduaine:
    def __init__(self, nimetus, valk, rasv, süsivesikud):
        self.nimetus = nimetus
        self.valk = valk
        self.rasv = rasv
        self.süsivesikud = süsivesikud
        
    def kontrolli_protsent(self):
        if self.valk + self.rasv + self.süsivesikud > 100:
            raise ValueError("Protsent ei tohi ületada 100")
        if self.valk < 0 or self.rasv < 0 or self.süsivesikud < 0:
            raise ValueError("Protsent ei tohi olla negatiivne")
        return True

class Toidukomponent:
    def __init__(self, toiduaine, kogus):
        self.toiduaine = toiduaine
        self.kogus = kogus
    def rasva_kogus(self):
        return self.kogus * self.toiduaine.rasv / 100
    def valkude_kogus(self):
        return self.kogus * self.toiduaine.valk / 100
    def süsivesikute_kogus(self):
        return self.kogus * self.toiduaine.süsivesikud / 100

class Toit:
    def __init__(self, nimetus, toidukomponendid,kogus_g):
        self.nimetus = nimetus
        self.toidukomponendid = toidukomponendid
        self.kogus_g = kogus_g
    def valkude_kogus(self):
        kokku = 0
        kogukaal = sum(i.kogus for i in self.toidukomponendid)
        for i in self.toidukomponendid:
            kokku += i.valkude_kogus()
        return kokku * self.kogus_g / kogukaal 
    def rasvade_kogus(self):
        kokku = 0
        kogukaal = sum(i.kogus for i in self.toidukomponendid)
        for i in self.toidukomponendid:
            kokku += i.rasva_kogus()
        return kokku * self.kogus_g / kogukaal       
    def süsivesikute_kogus(self):
        kokku = 0
        kogukaal = sum(i.kogus for i in self.toidukomponendid)
        for i in self.toidukomponendid:
            kokku += i.süsivesikute_kogus()
        return kokku * self.kogus_g / kogukaal
    def toiduained_kogused(self, kogus):
        kogukaal = sum(i.kogus for i in self.toidukomponendid)
        for i in self.toidukomponendid:
            print(f"{i.toiduaine.nimetus}: {round(i.kogus * kogus / kogukaal, 2)}g")




t1 = Toiduaine("kartul", 40, 10, 50) #nimetus, valk, rasv, süsivesikud
t2 = Toiduaine("hapukoor", 20, 20, 60) 
t3 = Toiduaine("vorst", 20, 20, 60)

# print(t1.kontrolli_protsent())
# print(t2.kontrolli_protsent())
# print(t3.kontrolli_protsent())

tk1 = Toidukomponent(t1, 100)
tk2 = Toidukomponent(t2, 30)
tk3 = Toidukomponent(t3, 50)

# print(tk1.rasva_kogus())
# print(tk2.rasva_kogus())
# print(tk3.rasva_kogus())

tr1 = Toit("kartulisalat", (tk1, tk2, tk3), 1000)

print("vajalikud toiduained 5kg kartulisalati jaoks:")
tr1.toiduained_kogused(5000)
print("sellest saame kätte:")
print("valku: ", round(tr1.valkude_kogus(), 2), "g")
print("rasva: ", round(tr1.rasvade_kogus(), 2), "g")
print("susivsikuid: ", round(tr1.süsivesikute_kogus(), 2), "g")





