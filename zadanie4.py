file = open('liczby_przyklad.txt', 'r')

s1 = file.readline()
s2 = file.readline()

l11 = s1.split(' ')
l22 = s2.split(' ')

l1 = list(map(int, l11))
l2 = list(map(int, l22))

counter = 0

print(s1)
print(s2)
for n1 in l1:
    is_div = False;
    j = 0;
    while (not is_div) and (j < len(l2)):
        n2 = l2[j]
        if n2 % n1 == 0:
            is_div = True;
        if is_div:
            counter += 1
