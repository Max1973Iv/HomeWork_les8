# класс customer представляет клиента с атрибутами name (имя) и orders (список заказов клиента)
class Customer:
    def __init__(self, name: str, orders: str):
        self.name = name
        self.orders= orders
#
    def __str__(self):
        return f"клиент (Имя={self.name}, Список заказов={self.orders})"