file = open('liczby.txt', 'r')

s1 = file.readline()
s2 = file.readline()
l11 = s1.split()
l22 = s2.split()
l1 = list(map(int, l11))
l2 = list(map(int, l22))


def rozklad(n):
    czynniki = []
    dzielnik = 2
    while dzielnik * dzielnik <= n:
        while (n % dzielnik) == 0:
            czynniki.append(dzielnik)
            n //= dzielnik
        dzielnik += 1
    if n > 1:
        czynniki.append(n)
    return czynniki


from collections import Counter

counter_l1 = Counter(l1)
for liczba in l2:
    czynniki = rozklad(liczba)
    policzczyn = Counter(czynniki)

    sprawdz = True
    for czynnik, ile in policzczyn.items():
        if counter_l1[czynnik] < ile:
            sprawdz = False
            break

    if sprawdz:
        print(f"Liczba {liczba}")
