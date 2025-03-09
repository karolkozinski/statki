from abc import ABC, abstractmethod


class Statek(ABC):  # Klasa abstrakcyjna
    def __init__(self, maksymalnaZaloga, maksymalneDziala, ladownosc, predkosc, curZaloga, curDziala, curLadunek):
        self.maksymalnaZaloga = maksymalnaZaloga
        self.maksymalneDziala = maksymalneDziala
        self.ladownosc = ladownosc
        self.predkosc = predkosc
        self.curZaloga = curZaloga
        self.curDziala = curDziala
        self.curLadunek = curLadunek
    
    @abstractmethod
    def zmien_zaloge(self, oIle):
        self.curZaloga = self.curZaloga + oIle
        if self.curZaloga > self.maksymalnaZaloga:
            self.curZaloga = self.maksymalnaZaloga
        if self.curZaloga < 0:
            self.curZaloga  = 0

        
    @abstractmethod
    def pokaz_info(self):
        print ('Załoga: ' + str(self.curZaloga) + '/' + str(self.maksymalnaZaloga))
        print ('Działa: ' + str(self.curDziala) + '/' + str(self.maksymalneDziala))
        print ('Ładowność: ' + str(self.curLadunek) + '/' + str(self.ladownosc))
        print ('Nazwa klasy statku: ' + __name__)
                



class Fregata(Statek):  # Klasa dziedzicząca po abstrakcyjnej klasie Statek
    def __init__(self, curZaloga, curDziala, curLadunek):
        super().__init__(200, 24, 120, 9, curZaloga, curDziala, curLadunek)
        self.zaloga = curZaloga
        self.dziala = curDziala
        self.ladunek = curLadunek
    def zmien_zaloge(self, oIle):
        super().zmien_zaloge()
    def pokaz_info(self):
        super().pokaz_info()


SantaMaria = Fregata(50,20,10)
SantaMaria.pokaz_info()