file = open('liczby_przyklad.txt', 'r')

s1 = file.readline()
l11 = s1.split(' ')
l1 = list(map(int, l11))

print(s1)
l1.sort(reverse=True)

if len(l1) >= 101:
    print(l1[100])