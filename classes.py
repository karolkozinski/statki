from abc import ABC, abstractmethod

class Statek(ABC):
    def __init__(self, maxZaloga, maxDziala, maxLadunek, predkosc, curZaloga, curDziala, curLadunek):
        self.maxZaloga = maxZaloga
        self.maxDziala = maxDziala
        self.maxLadunek = maxLadunek
        self.predkosc = predkosc
        self.zaloga = curZaloga
        self.dziala = curDziala
        self.ladunek = curLadunek

    @abstractmethod
    def zmien_zaloge(self, oIle):
        self.zaloga = self.zaloga + oIle
        if self.zaloga > self.maxZaloga:
            self.zaloga = self.maxZaloga
        if self.zaloga < 0:
            self.zaloga  = 0



            
    def pokaz_info(self):
        return f"Typ statku: {self.__class__.__name__}\n" \
               f"Maksymalna załoga: {self.maxZaloga}, Obecna załoga: {self.zaloga}\n" \
               f"Maksymalne działa: {self.maxDziala}, Obecne działa: {self.dziala}\n" \
               f"Maksymalny ładunek: {self.maxLadunek}, Obecny ładunek: {self.ladunek}\n" \
               f"Prędkość: {self.predkosc} węzłów"

class Fregata(Statek):  
    def __init__(self, curZaloga, curDziala, curLadunek):
        super().__init__(200, 24, 120, 9, curZaloga, curDziala, curLadunek)

    def zmien_zaloge(self, oIle):
        super().zmien_zaloge(oIle)

    def pokaz_info(self):
        return super().pokaz_info()

# Tworzenie obiektu klasy Fregata
fregata = Fregata(150, 20, 100)

# Wywołanie metody pokaz_info()
print(fregata.pokaz_info())

fregata.zmien_zaloge(-15)
print(fregata.pokaz_info())