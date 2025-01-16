def nwd(a, b):
    while b:
        a, b = b,a % b
    return a


def skrotLiczba(liczba):
    potega = 1
    wynik = 0
    while liczba > 0:
        cyfra = liczba % 10
        if cyfra % 2 == 1:  # 
            wynik = potega * cyfra + wynik
            potega = potega * 10
        liczba = liczba // 10
    return wynik


with open("skrot2.txt") as plik:
    linie = plik.readlines()
    linie = [int(line.strip()) for line in linie]


with open("wyniki3_3.txt", "w") as wynik_file:
    for liczba in linie:
        
        if nwd(liczba, skrotLiczba(liczba)) == 7:
            wynik_file.write(f"{liczba}\n")