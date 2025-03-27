file = open('liczby.txt', 'r')

s1 = file.readline()
s2 = file.readline()
l1 = list(map(int, s1.split()))
l2 = list(map(int, s2.split()))

def rozdziel(liczba):
    czynniki = []
    m = 2
    while m <= liczba:
        while liczba % m == 0:
            czynniki.append(m)
            liczba = liczba // m
        m += 1
    return czynniki

def sprawdz(liczba, l1):
    czynniki = rozdziel(liczba)
    czynniki_w_l1 = [x for x in czynniki if x in l1]
    from collections import Counter
    czynniki_count = Counter(czynniki)
    l1_count = Counter(l1)

    for factor, count in czynniki_count.items():
        if l1_count.get(factor, 0) < count:
            return False
    return True


for liczba in l2:
    if sprawdz(liczba, l1):
        czynniki = rozdziel(liczba)
        print(f"Liczba {liczba} czynniki: {czynniki}")
