# שאלה 1
# def format_receipt(items):
#     def line(name, price):
#         return name.ljust(10) +str(price)
#     res=[]
#     for i,y in items:
#         res.append(line(i, y))
#     return res
#
#
#
# print(format_receipt([("Milk", 6), ("Bread", 9)]))
#  שאלה 2
# def make_greeter(greeting):
#     def oiii(j):
#         return f"{greeting}  {j}"
#     return oiii
#
#
# hello = make_greeter("Hello")
# shalom = make_greeter("Shalom")
# print(hello("Dana"))
# print(shalom("Avi"))


# def make_counter(step):
#     o=0
#     def oooo():
#         nonlocal o
#         o+=step
#         return o
#     return oooo
#
#
#
# by_two = make_counter(2)
# by_ten = make_counter(10)
# print(by_two(), by_two())
# print(by_ten())
# print(by_two())


def make_counter():
    count = 0
    def increment():
        count += 1
        return count
    return increment

counter = make_counter()
counter()