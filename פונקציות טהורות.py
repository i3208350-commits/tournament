# שאלה 1
# def square(n):    פונקציה טהורה כי n לא תלוי בכלום
#     return n * n
#
# def log_square(n):
#     print("squaring", n)                    לכאורה לא טהורה כי אני מדפיס למסך
#     return n * n
#
# def add_item(cart, item):     לא פונקציה טהורה כי אני משנה את הרשימה עצמה
#     cart.append(item)
#     return cart
#
# def with_item(cart, item):     פונקציה טהורה כי המונחים לא השתנו אלא רק התווסף
#     return cart + [item]



# שאלה 2- עכשיו המשתנה לא ממשיך לצבור את תוצאת הפונקציה הקודמת
# def add_price(total,price):
#
#     total += price
#     return total
#
#
# total = 0
# total = add_price(total, 10)
# total = add_price(total, 10)
# print(total)
#
# print(add_price(0, 10))
# print(add_price(0, 10))

# שאלה 3
# TAX = 1.17
#
# def apply_tax(prices):
#     riao = []
#     for i in (prices):
#         riao.append(i*TAX)
#     return riao
#
#
#
#
#
# prices = [100, 50]
# with_tax = apply_tax(prices)
# print(prices)
# print(with_tax)