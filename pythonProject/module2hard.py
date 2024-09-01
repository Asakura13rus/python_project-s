for n in range(3, 21):
    result = ""
    used_pairs = set() 

    for i in range(1, n):
        for j in range(1, n):
            if i != j and (i + j) % n == 0:
                if (j, i) not in used_pairs:
                    result += f"{i}{j}"
                    used_pairs.add((i, j))

    print(f"{n} - {result}")
