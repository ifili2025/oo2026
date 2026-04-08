# Takistile mõjub pinge 5 volti ning seda läbib vool 2 amprit. Mitu vatti soojust eraldub takistist?
# Takistile mõjub pinge 4 volti ning sealt eraldub võimsus 6 vatti. Mitu amprit voolu läbib takistit? P= U/I
# Mitu oomi on eelneva takisti takistus? R = U/I  takistus (R) on võrdne pingega (U), mis on jagatud voolutugevusega (I)
# Veekeedukannu võimsuseks on 1 kilovatt, seal sees on vett 1 liiter. Mitme kraadi peale tõuseb vee temperatuur 20 kraadi
# Celsiuse pealt ühe minutiga, kui kogu sisselülitatud kannu võimsus läheb vee soojendamiseks?
# Mitu amprit voolu läbib eelnimetatud veekeedukannu, kui võrgupinge on 220 volti?
# Mitu oomi on selle veekeedukannu takistus?
# Koosta takistitest massiiv. Koosta funktsioon, mis loob uue massiivi takistitest, mille lubatud võimsus jääb etteantud pinge korral lubatud piiresse.
class Resistor:
    def __init__(self, r, max_power):
        self.r = r
        self.max_power = max_power
    def get_Current(self, u):
        return u / self.r
    def get_Power(self,u):
        return u*self.r
    def check_Power(self, u):
        return self.max_power - self.get_Power(u)
        
class ResistorRun1:
    @staticmethod
    def main():
        r1=Resistor(220,50)
        r2=Resistor(200,130000)
        r3=Resistor(1500,30)
        r4=Resistor(2000,20)
        print(r1.check_Power(24))
        print(r2.check_Power(24))
        print(r3.check_Power(24))
        print(r4.check_Power(24))
if __name__ == "__main__":
    ResistorRun1.main()




