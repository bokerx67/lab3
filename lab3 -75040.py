#zad1
print("\fzad1: ")
paliwo = 100
paliwo_zuzyte_na_s = 10
czas = 0

while paliwo > 0:
    print(f"Stan paliwa: {paliwo}L, czas: {czas}s")
    paliwo -= paliwo_zuzyte_na_s
    czas += 1
    if paliwo == 0:
        print("Koniec lotu! ")
#zad2
print("\fzad2: ")

licznik = 0
liczba_p = 2
lista_l_p = []
while licznik < 10:
    for i in range(2,liczba_p):
        if liczba_p % i == 0:
            break
    else:
        lista_l_p.append(str(liczba_p))
        licznik += 1
    liczba_p += 1

print(','.join(lista_l_p))

#zad3
print("\fzad3: ")

Ulice = ["Jagodowa", "Lipowa", "Kwiatowa", "Kasztanowa", "Polna"]
Numery = [1, 2, 3, 4, 5]
Mieszkania = ["/1", "/2", "/3", "/4","/5", "/6", "/7", "/8", "/9", "/10"]
for Ulica in Ulice:
    for Numer in Numery:
           for Mieszkanie in Mieszkania:
                print("Ulica",Ulica, "Numer", Numer, Mieszkanie)

#zad5
print("\fzad5: ")

liczby = []

for i in range(80,-1,-4):
    liczby.append(i)

print(f"{liczby}")

#zad6
print("\fzad6: ")

while True:
    if int(input("Podaj liczbę")) < 0:
        break

#zad8
print("\fzad8: ")

tekst = "Python jest super"

print(f"Oryginaln tekst: {tekst}")
print(f"Znak o indeksie 0: {tekst[0]}")
print(f"Znak o indeksie ostatnim: {tekst[-1]}")
print(f"Co drugi znak, zaczynając od 0: {tekst[0::2]}")
print(f"Co trzeci znak, zaczynając od 1: {tekst[1::3]}")
print(f"Od dziesiątego do ostatniego: {tekst[10:]}")
print(f"Od końca do początku: {tekst[::-1]}")

#zad9
print("\fzad9: ")

imie = input("Podaj imie: ")
nazwisko = input("Podaj nazwisko: ")
wiek = int(input("Podaj wiek: "))
print(f"Witaj {imie}")
print(f"Twój wiek to {wiek}")
print(f"Twoje inicjały to: {imie[0]}.{nazwisko[0]}.")

tekst = input("Podaj tekst: ")
for i in range(5):
    print(tekst)

l1 = input("Podaj pierwszy tekst: ")
l2 = input("Podaj drugi tekst: ")
l3 = l1+l2
print(f"Połączone teksty: {l3}")

l3 = input("Podaj pierwszy tekst: ")
l4 = input("Podaj drugi tekst: ")
l5 = l3[:len(l3)//2]+l4[len(l4)//2:]
print(f"Połączone połówki tekstów: {l5}")
#Wykonał Konrad Greszta 75040
