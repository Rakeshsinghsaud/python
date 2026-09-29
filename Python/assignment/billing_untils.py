def apply_discount(amount, percent):
    discount = amount * percent / 100
    final_amount = amount - discount
    return final_amount


def apply_tax(amount, percent):
    tax = amount * percent / 100
    final_amount = amount + tax
    return final_amount