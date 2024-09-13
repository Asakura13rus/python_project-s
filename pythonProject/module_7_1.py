class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                return file.read().strip()
        except FileNotFoundError:
            return ''

    def add(self, *products):
        current_products = self.get_products().splitlines()
        current_names = [line.split(', ')[0] for line in current_products]

        with open(self.__file_name, 'a') as file:
            for product in products:
                if product.name not in current_names:
                    file.write(str(product) + '\n')
                    current_names.append(product.name)
                else:
                    print(f'Продукт {product} уже есть в магазине')


# Пример работы программы
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # Проверка метода __str__
s1.add(p1, p2, p3)
print(s1.get_products())