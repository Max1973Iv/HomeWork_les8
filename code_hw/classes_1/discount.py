"""класс discount представляет описание скидок для заказов с атрибутами
discount_percent (процент скидки) и description (описание скидки)
метод __init__ инициализирует объект с этими атрибутами
метод __str__ возвращает строковое представление объекта для удобного вывода
статический метод позволяет рассчитать цену со скидкой для различных видов скидок"""
class Discount:
    def __init__(self, discount_percent, description):
        self.discount_percent = discount_percent  # процент скидки
        self.description = description  # описание скидки
#
    def __str__(self):
        return f"Discount: {self.discount_percent}%, Description: {self.description}"  # строковое представление объекта
#    @staticmethod
    def calculate_discounted_price(original_price, discount_percent):
        """Статический метод для расчета цены со скидкой"""
        if discount_percent < 0 or discount_percent > 100:
            raise ValueError("Discount percent must be between 0 and 100")
        discounted_price = original_price * (1 - discount_percent / 100)
        return round(discounted_price, 2)