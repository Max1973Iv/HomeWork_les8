# 
"""класс customer представляет клиента с атрибутами name (имя) и orders (список заказов клиента)
метод __init__ инициализирует объект с этими атрибутами
метод __str__ возвращает строковое представление объекта для удобного вывода"""
class Customer:
    def __init__(self, name: str, orders: list):
        self.name = name
        self.orders= []#инициализ как пустой список
    def add_order(self, order):
        """
        Метод add_order для добавления нового заказа в список заказов.
        """
        self.orders.append(order)
    #
    def __str__(self):
        orders_str = ', '.join(str(order) for order in self.orders)
        return f"клиент (Имя: {self.name}, Список заказов: {orders_str})"
#
#    def __str__(self):
#       return f"клиент (Имя: {self.name}, Список заказов: {self.orders})"