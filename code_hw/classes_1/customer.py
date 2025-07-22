# 
"""класс customer представляет клиента с атрибутами name (имя) и orders (список заказов клиента)
метод __init__ инициализирует объект с этими атрибутами
метод __str__ возвращает строковое представление объекта для удобного вывода"""
class Customer:
    def __init__(self, name: str, orders: str):
        self.name = name
        self.orders= orders
#
    def __str__(self):
        return f"клиент (Имя={self.name}, Список заказов={self.orders})"