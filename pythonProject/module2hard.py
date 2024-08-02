n = int(input("Введите число от 3 до 20: "))

pairs = []

for i in range(1, 21):
    for j in range(i + 1, 21):
        if (i + j) % n == 0:
            pairs.append(f"{i}{j}")

result = ''.join(pairs)

print(f"{n} - {result}")