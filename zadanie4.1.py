file = open('liczby.txt', 'r')

s1 = file.readline()
s2 = file.readline()
l11 = s1.split(' ')
l22 = s2.split(' ')
l1 = list(map(int, l11))
l2 = list(map(int, l22))

count = 0

for num1 in l1:
    for num2 in l2:
        if num2 % num1 == 0:
            count += 1
            break

print(count)
