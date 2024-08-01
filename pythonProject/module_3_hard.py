def calculate_structure_sum(data_structure):
    def recursive_sum(data):
        total_sum = 0

        if isinstance(data, (list, tuple, set)):
            for item in data:
                total_sum += recursive_sum(item)
        elif isinstance(data, dict):
            for key, value in data.items():
                total_sum += recursive_sum(key)
                total_sum += recursive_sum(value)
        elif isinstance(data, int):
            total_sum += data
        elif isinstance(data, str):
            total_sum += len(data)

        return total_sum

    return recursive_sum(data_structure)


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)