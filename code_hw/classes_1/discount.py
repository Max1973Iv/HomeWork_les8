"""класс discount представляет описание скидок для заказов с атрибутами
discount_percent (процент скидки) и description (описание скидки)"""
class Discount:
    def __init__(self, discount_percent, description):
        self.discount_percent = discount_percent  # процент скидки
        self.description = description  # описание скидки

    def __str__(self):
        return f"Discount: {self.discount_percent}%, Description: {self.description}"  # строковое представление объекта