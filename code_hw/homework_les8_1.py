#начало
#создать систему для интернет магазина
import sys
from datetime import datetime
from classes_1.product import Product
from classes_1.order import Order
from classes_1.discount import Discount
from classes_1.customer import Customer
sys.stdout.reconfigure(encoding='utf-8')  # для корректного отображения кириллицы в консоли
#
# создаем продукты
product1 = Product("Ноутбук", 130)
product2 = Product("Смартфон", 50)
product3 = Product("Телевизор", 80)
# создаем клиентов
customer1 = Customer("Иван Иванов","")
customer2 = Customer("Петр Петров","")
customer3 = Customer("Сидор Сидоров","")
# создаем скидки
discount_10_season = Discount(10, "Скидка 10% на все товары сезонная")
discount_2_over100 = Discount(2, "Скидка 2% на товары в заказе с общей суммой заказа более 100")
# рассчитываем цену со скидкой для первого продукта
discounted_price_product1 = Discount.calculate_discounted_price(product1.price, discount_10_season.discount_percent)
# рассчитываем цену со скидкой для второго и третьего продукта
discounted_price_product2 = Discount.calculate_discounted_price(product2.price, discount_10_season.discount_percent)
discounted_price_product3 = Discount.calculate_discounted_price(product3.price, discount_10_season.discount_percent)
#
# создаем заказ
order1 = Order([product1, product2])  # заказ с двумя продуктами
print(order1.nomber)  # вывод информации о номере заказа
# расчитываем стоимость первого заказа с учетом скидки discount_10_season
discounted_price_order1 = sum(product.price for product in order1.products) * (1 - discount_10_season.discount_percent / 100)
# привязываем заказ к клиенту -добавляем заказ в список заказов клиента
customer1.add_order(order1)
# выводим информацию о клиенте и заказе
print(f'{customer1} Стоимость:{sum(product.price for product in order1.products)} \nОбщая стоимость заказа со скидкой "{discount_10_season.description}" : {discounted_price_order1}')  # вывод информации о заказе
# рассчитыавем стоимость первого заказа с оптовой скидкой (если сумма заказа с учетом скидки discount_10_season больше 100)
if discounted_price_order1 > 100:
    discounted_price_order1 = Discount.calculate_discounted_price(discounted_price_order1, discount_2_over100.discount_percent)
    print(f'Стоимость со скидкой "{discount_2_over100.description}" для заказа  № {order1.nomber} : {discounted_price_order1}')  # вывод стоимости со скидкой для первого заказа
#
# создаем второй заказ с одним продуктом
order2 = Order([product3])  # заказ с одним продуктом
print(order2.nomber) # вывод информации о номере заказа
# расчитываем стоимость второго заказа с учетом скидки discount_10_season
discounted_price_order2 = sum(product.price for product in order2.products) * (1 - discount_10_season.discount_percent / 100)
# привязываем заказ ко второму клиенту - добавляем заказ в список заказов клиента
customer2.add_order(order2)
# выводим информацию о втором клиенте и заказе
print(f'{customer2} Стоимость:{sum(product.price for product in order2.products)} \nОбщая стоимость заказа со скидкой "{discount_10_season.description}" : {discounted_price_order2}')  # вывод информации о заказе
# рассчитыавем стоимость второго заказа с оптовой скидкой (если сумма заказа с учетом скидки discount_10_season больше 100)
if discounted_price_order2 > 100:
    discounted_price_order2 = Discount.calculate_discounted_price(discounted_price_order2, discount_2_over100.discount_percent)
    print(f'Стоимость со скидкой "{discount_2_over100.description}" для заказа № {order2.nomber} : {discounted_price_order2}')  # вывод стоимости со скидкой для второго заказа
#
# создаем третий заказ с одним продуктом
order3 = Order([product3])  # заказ с одним продуктом
print(order3.nomber)  # вывод информации о номере заказа
# расчитываем стоимость третьего заказа с учетом скидки discount_10_season
discounted_price_order3 = sum(product.price for product in order3.products) * (1 - discount_10_season.discount_percent / 100)
# привязываем заказ к первому клиенту - добавляем второй заказ в список заказов клиента
customer1.add_order(order3)
# выводим информацию о первом клиенте и третьем заказе
print(f'{customer1} Стоимость:{sum(product.price for product in order3.products)} \nОбщая стоимость заказа со скидкой "{discount_10_season.description}" : {discounted_price_order3}')  # вывод информации о заказе
# рассчитыавем стоимость третьего заказа с оптовой скидкой (если сумма заказа с учетом скидки discount_10_season больше 100)
if discounted_price_order3 > 100:
    discounted_price_order3 = Discount.calculate_discounted_price(discounted_price_order3, discount_2_over100.discount_percent)
    print(f'Стоимость со скидкой "{discount_2_over100.description}" для заказа № {order3.nomber} : {discounted_price_order3}')  # вывод стоимости со скидкой для третьего заказа
#
#
# выводим информацию о скидках
print(f'Скидка "{discount_10_season.description}" : {discount_10_season.discount_percent}%')  # вывод информации о скидке discount_10_season
print(f'Скидка "{discount_2_over100.description}" : {discount_2_over100.discount_percent}%')  # вывод информации о скидке discount_2_over100
# выводдим информацию о ценах на товары со скидкой
print(f'Цена со скидкой "{discount_10_season.description}" для {product1.name}: {discounted_price_product1}')
print(f'Цена со скидкой "{discount_10_season.description}" для {product2.name}: {discounted_price_product2}')
print(f'Цена со скидкой "{discount_10_season.description}" для {product3.name}: {discounted_price_product3}\n\n')
#
# выводим общее количество заказов
print(f'Всего заказов: {Order.sum_total_orders([order1, order2, order3])}\n\n')
# выводим общую стоимость всех заказов без учета скидок
print(f'Общая стоимость всех заказов без учета скидок: {Order.cash_total_orders([order1, order2, order3])}\n\n')
# выводим общую стоимость всех заказов с учетом скидок
total_discounted_price = discounted_price_order1 + discounted_price_order2 + discounted_price_order3
print(f'Общая стоимость всех заказов с учетом скидок: {total_discounted_price}\n\n')
# время и дата выполнения программы
from datetime import datetime
print(f'Время и дата выполнения программы: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n\n')
# конец