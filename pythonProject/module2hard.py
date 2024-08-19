n = int(input("Ведите число от 3 до 20 что бы получить пароль: "))

pairs = []
for i in range(1, n):
    for j in range(i + 1, n):
        if (i + j) % n == 0:
            pairs.append(str(i) + str(j))

result = ''.join(pairs)

print(f'{n} - {result}')
