def student_discount(price):
    return price * (0.9 if price > 1000 else 0.95)
def regular_discount(price):
    return price * 0.85 if price > 2000 else price
def discount(price, category):
    strategies = {
        "student": student_discount,
        "regular": regular_discount,
    }
    return strategies.get(category, regular_discount)(price)
print(discount(1500, "student"))
print(discount(1500,"regular"))
print(discount(2500,"student"))
print(discount(2500,"regular"))


