# класс Product
class Product:
    """
    Класс Product
    Этот класс представляет товар в интернет-магазине с атрибутами name (название товара) и price (цена товара).
    Метод __init__:
        Конструктор инициализирует объект Product с двумя атрибутами: name (название товара) и price (цена товара).
    Метод __str__:
        Возвращает строковое представление объекта, чтобы его можно было удобно вывести с помощью print.
    """
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Продукт (Название={self.name}, Цена={self.price})"