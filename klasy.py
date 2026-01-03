#Klasa = Szablon, Przepis
class Czlowiek:
    gatunek = "Homo Sapiens"
    def __init__(self, imie, plec):
        # Konstruktor
        #Akt Istnienia
        print(f"Niech powstanie czlowiek o imieniu {imie}")
        self.imie =imie
        self.plec= plec
        #adam.imie = "Adam"

        #Metoda
    def przedstaw_sie(self):
        print(f"dzien dobry mam na imie {self.imie} i jestem", end =" ")
        if self.plec=="M":
            print("mezczyzna")
        else:
            print("kobieta")

    def przedstaw(self, osoba):
        print(f"Oto {osoba.imie}")
# Gotowanie z przepisu
adam = Czlowiek("Adam", "M")
ewa = Czlowiek("Ewa", "K")

class Dziecko(Czlowiek):
    def baw_sie(self):
        print("Ale zabawa!!!!")

    def przedstaw_sie(self):
        print(f"Czesc mam na imie {self.imie} i jestem", end =" ")
        if self.plec=="M":
            print("chlopcem")
        else:
            print("dziwczynka")

print(adam.gatunek)
print(ewa.gatunek)
print(ewa.imie)
print(adam.imie)
adam.przedstaw_sie()
ewa.przedstaw(adam)

dziecko = Dziecko("Kain", "M")
dziecko.baw_sie()
dziecko.przedstaw_sie()