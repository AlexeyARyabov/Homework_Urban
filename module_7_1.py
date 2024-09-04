from pprint import pprint


class Product:

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(Shop.__file_name, 'r')
        pprint(file.read())
        file.close()

    def add(self, *products):
        file = open(Shop.__file_name, 't+r')
        content = file.read()
        for p in products:
            if str(p) in content:
                print('Продукт ', p, ' уже есть в магазине')
            else:
                file.write(Product.__str__(p)+'\n')
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
