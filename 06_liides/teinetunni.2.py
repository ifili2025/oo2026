#koosta uus adderi alamklass, mis toimib, nõnda, et eksemplari loomisel antakse sinna faili nimi andmete hoidmiseks 
#Igal lisamisel kirjutatakse faili kogus ning lisamise kellaeg
#Summa küsimisel arvutatakse andmed failist kokku
#kasutatakse sama faili andmed ka korduval käivitamisel
import contextlib
from abc import ABC, abstractmethod
import datetime
class Adder(ABC):
    @abstractmethod
    def add(self, nr: float) -> None:
        pass
    @abstractmethod
    def getSum(self) -> float:
        pass
    def greet(self)-> None:
        print("hello")
class FileStoringadder(Adder):
    def __init__ (self, failinimi):
        self.failinimi = failinimi
    def add(self,nr: float) -> None:
        with open(self.failinimi, "a") as f2:
            print(nr, datetime.datetime.now().strftime("%X"), sep=",", file=f2)
    def getSum(self) -> float:
        total = 0
        with open(self.failinimi, "r") as f2:
            for line in f2:
                parts = line.strip().split(",")
                total += float(parts[0])
        return total
class CharCounter:
    def __init__ (self, a: Adder):
        self.adder = a
    def addWordCharacters(self, word):
        self.adder.add(len(word))
    def getCharacterCount(self):
        return self.adder.getSum()

a:Adder= FileStoringadder("sonapikkused.txt")
c:CharCounter = CharCounter(a)
while sisend := input("Palun lause, katkestuseks enter: "):
    for sona in sisend.split(): c.addWordCharacters(sona)
print(a.getSum())