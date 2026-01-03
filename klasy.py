#Klasa
class Czlowiek:
    gatunek = "Homo Sapiens"
    def __init__(self, imie):
        # Konstruktor
        #Akt Istnienia
        print(f"Niech powstanie czowiek o imieniu {imie}")
        self.imie =imie
        #ada.imie = "Adam"
#Powstawanie obiektu
# Gotowanie z przepisu
adam = Czlowiek("Adam")
ewa = Czlowiek("Ewa")

print(adam.gatunek)
print(ewa.gatunek)
print(ewa.imie)
print(adam.imie)