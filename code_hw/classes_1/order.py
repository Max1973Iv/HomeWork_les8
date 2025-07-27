"""класс order представляет заказ с атрибутами products (список товаров в заказе) и nomber (номер заказа, который автоматически увеличивается при каждом новом заказе)
метод __init__ инициализирует объект с этими атрибутами
метод __str__ возвращает строковое представление объекта для удобного вывода
метод класса sum_total_orders возвращает общее количество заказов
метод класса cash_total_orders возвращает общую стоимость всех заказов"""
class Order:
    def __init__(self, products: list, nomber: int = 0):
        """
        Инициализация заказа списком товаров.
        """
        self.products = products
        self.nomber = nomber
        self.nomber += 1  # увеличиваем номер заказа при каждом новом заказе
#
    def __str__(self):
        return f"Список {len(self.products)} товаров в заказе номер {(self.nomber)}: {', '.join(str(product) for product in self.products)}"
#
    @classmethod
    def sum_total_orders(cls, orders):
        """
        Метод класса для подсчета общего количества заказов
        """
        return len(orders)
#
    @classmethod
    def cash_total_orders(cls, orders):
        """
        Метод класса для подсчета общей стоимости всех заказов
        """
        total = 0
        for order in orders:
            total += sum(product.price for product in order.products)
        return total