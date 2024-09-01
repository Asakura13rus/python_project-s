for n in range(3, 21):
    result = ""
    used_pairs = set()  # Для хранения использованных пар

    for i in range(1, n):
        for j in range(i + 1, n):
            if (i + j) % n == 0:
                result += f"{i}{j}"

    print(f"{n} - {result}")
