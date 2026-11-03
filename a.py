import json
VAT_RATE = 0.17
def add_vat(amount):
    p=amount
    amount= round(amount*VAT_RATE+p)
    return amount


def apply_discount(amount, percent):
    o=amount/percent
    amount-=o
    return round(amount,2)


g=apply_discount(200,10)
u=add_vat(g)
print(g)
print(u)




o={"name":12}
p="profile.json"
with open( p , "w", encoding="utf-8") as file:
    json.dump(o, file, indent=2, ensure_ascii=False)

with open(p, "r",encoding="utf-8")as file:
    k=json.load(file)
    print(k)
