# <!--Hulknurk
# * Koosta klass, milles on üks massiiv kolmnurga x-koordinaatide hoidmiseks ning teine massiiv y-koordinaatide hoidmiseks. 
# Koosta klassist kaks eksemplari, määra algväärtused ning trüki andmed välja.

# * Lisa klassile käsklus punkti koordinaadipaari lisamiseks. Käsklusena väljasta tekkiva hulknurga ümbermõõt. 
# Kuva tekkinud kujund ekraanile.

# * Lisa klassile käsklused kogu kujundi nihutamiseks ning suurendamiseks/vähendamiseks. 
# Võimalda küsida punktide uued asukohad ning külgede pikkused, näita kujundit ekraanil. -->

from PIL import Image, ImageDraw
import math
class Hulknurk:
    xid=[]
    yid=[]
    def __init__(self,x1,y1,x2,y2,x3,y3):
        self.xid=[x1,x2,x3]
        self.yid=[y1,y2,y3]
    def lisa(self,x,y):
        self.xid.append(x)
        self.yid.append(y)
    def ymbermoot(self):
        # p1 = (self.xid[0],self.yid[0])
        # p2 = (self.xid[1],self.yid[1])
        # p3 = (self.xid[2],self.yid[2])
        # perim = (
        #     math.dist(p1,p2) +
        #     math.dist(p2,p3) +
        #     math.dist(p3,p1)
        # )
        # return perim
        v = 0 
        for nr in range(len(self.xid)):
            dx=self.xid[(nr+1) % len(self.xid)] - self.xid[nr]
            dy=self.yid[(nr+1) % len(self.yid)] - self.yid[nr]
            v+= math.sqrt(dx*dx+dy*dy)
        return v
    # def paremale(self):
    #     for nr in range(len(self.xid)):
    #         self.xid[nr]+=1
    def nihuta(self, dx,dy):
        for nr in range(len(self.xid)):
            self.xid[nr]+= dx
            self.yid[nr]+= dy
    # def p2(self):
    #     self.xid=[x+1 for x in self.xid]
    def suurenda(self, dx,dy):
        for i in range(len(self.xid)):
            self.xid[i] *= dx
            self.yid[i] *= dy
    def vahenda(self, dx,dy):
        for i in range(len(self.xid)):
            self.xid[i] /= dx
            self.yid[i] /= dy
    def __str__(self):
        return ", ".join([f"({paar[0]}, {paar[1]})" for paar in zip(self.xid, self.yid)])
    def tekstiks(self):
        vastus = ""
        for nr in range(3):
            vastus += "("+str(self.xid[nr])+", "+str(self.yid[nr])+")"
            return vastus
    def joonista(self):
        pilt1 = Image.new("RGB", (200,200))
        g=ImageDraw.ImageDraw(pilt1)
        for nr in range(len(self.xid)):
            g.line((self.xid[nr], self.yid[nr],
                self.xid[(nr+1) % len(self.xid)],
                self.yid[(nr+1) % len(self.yid)])),
        pilt1.save("pilt1.gif","GIF")

k1= Hulknurk(1,3,2,4,3,5)
print(k1.xid, k1.yid)
k2 = Hulknurk(20,30,25,14,21,20)
print(k2)
print(k2.xid,k2.yid)
print(list(zip(k2.xid, k2.yid)))
print(k2.tekstiks())
print(k2.ymbermoot())
k2.lisa(2,8)
print(k2.ymbermoot())
k2.nihuta(1,1)
print(k2.ymbermoot())
print(k2.tekstiks())
k2.suurenda(2,2)
print(k2.ymbermoot())
print(k2.tekstiks())
k2.vahenda(2,2)
print(k2.ymbermoot())
print(k2.tekstiks())
k2.joonista()
