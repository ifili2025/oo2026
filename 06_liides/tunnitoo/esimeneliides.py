from abc import ABC, abstractmethod
from datetime import datetime
class Adder(ABC):
    @abstractmethod
    def add(self, nr: float) -> None:
        pass
    @abstractmethod
    def getSum(self) -> float:
        pass
    def greet(self)-> None:
        print("hello")
class CharCounter:
    def __init__ (self, a: Adder):
        self.adder = a
        self.wordadder = None
    def setWordAdder(self, a2: Adder):
        self.wordadder = a2
    def addWordCharacters(self, word):
        self.adder.add(len(word))
        if self.wordadder: self.wordadder.add(1)
    def getCharacterCount(self):
        return self.adder.getSum()
    def getWordCount(self):
        return self.wordadder.getSum() if self.wordadder else -1
class SimpleAdder(Adder):
    def __init__(self):
        self.sum = 0
    def add(self , nr: float) -> None:
        self.sum += nr

    def getSum(self) -> float:
        return self.sum
    
sa = SimpleAdder()


lause = str(input("Sisesta lause:"))
sa2 = SimpleAdder()
lugeja1 = CharCounter(sa)
lugeja1.setWordAdder(sa2)
lugeja1.addWordCharacters(lause)
print(lugeja1.getCharacterCount())
print(lugeja1.getWordCount())
print(datetime.now())
#sa.add(3)
#sa.add(2)
#print(sa.getSum())
#lugeja1.addWordCharacters("Juku")
#lugeja1.addWordCharacters("Mikku")
#print(lugeja1.getCharacterCount())
#print(lugeja1.getWordCount())
