
def apply_discount(price, discount):
    final_price = int(price * (1 - discount))
    if not 0 <= final_price < price:
        raise ValueError ("Invalid discount")
    
    return final_price