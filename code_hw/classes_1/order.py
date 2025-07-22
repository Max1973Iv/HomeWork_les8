"""класс order представляет заказ с атрибутами products (список товаров в заказе)
""""
class Order:
    def __init__(self, products):
        self.products = products
#
    def __str__(self):
        return f"Список {len(self.products)} товаров в заказе: {', '.join(str(product) for product in self.products)}"
    
    