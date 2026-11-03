# שאלה 1
# def apply_to_all(numbers, action):
#     r=[]
#     for i in numbers:
#         r.append(action(i))
#     return r
#
# def double(i):
#     return i*2
#
# print(apply_to_all([1, 2, 3],double))
# print(apply_to_all([1, 2, 3], lambda n: n * n))
# print(apply_to_all([1.6, 2.4], round))

# שאלה 2
# prices = [20, 75, 120, 45, 90]
# o=list(filter(lambda p:p >50 ,prices))
# print(o)
# j=list(map(lambda  p:p+10,o))
# print(j)

# שאלה 4
# def make_discount(percent):
#     def discountn(n):
#
#         return n-(n/100*percent)
#     return discountn
#
#
# ten_off = make_discount(10)
# half_price = make_discount(50)
# print(ten_off(200))
# print(half_price(200))

