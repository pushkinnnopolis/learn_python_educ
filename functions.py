

def discounted_price(price, discount, max_discount = 20):
    price = abs(price)
    discount = abs(discount)
    max_discount = abs(max_discount)
    if max_discount >= 100:
        raise ValueError("Максимальная скидка не должна превыгш")
    if discount >= max_discount:
        price_with_discount = price
    else:
        price_with_discount = price - (price*discount/100)
    return price_with_discount

product = {
    "name": "Samsung",
    "price": 28999,
    "discount": 7
    }

product['with_discount']= discounted_price(product['price'], product['discount'])
print(discounted_price(product['price'], product['discount']))
print(discounted_price(product['price'], 50, max_discount = 69))

print(product)