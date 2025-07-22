"""класс order представляет заказ с атрибутами products (список товаров в заказе)
метод __init__ инициализирует объект с этими атрибутами
метод __str__ возвращает строковое представление объекта для удобного вывода
метод класса sum_total_orders возвращает общее количество заказов
метод класса cash_total_orders возвращает общую стоимость всех заказов"""
class Order:
    def __init__(self, products):
        self.products = products
#
    def __str__(self):
        return f"Список {len(self.products)} товаров в заказе: {', '.join(str(product) for product in self.products)}"
    
#
    @classmethod
    def sum_total_orders(cls, orders):
        """Метод класса для подсчета общего количества заказов"""
        return len(orders)
    @classmethod
    def cash_total_orders(cls, orders):
        """Метод класса для подсчета общей стоимости всех заказов"""
        total = 0
        for order in orders:
            total += sum(product.price for product in order.products)
        return total  