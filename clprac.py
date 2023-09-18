"""

det = lambda c: print(f'{c} < 8') if c < 8 else print(f'{c} too high')

det(10)

"""


class Phone:
    price_raise_rate = 0.12

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def raise_price(self):
        self.price = self.price * self.price_raise_rate
        return self.price


iphone = Phone("Apple", 1000)
galaxy = Phone("Samsung", 800)
Phone.price_raise_rate = 0.1
iphone.price_raise_rate = 0.08
print(iphone.raise_price(), galaxy.raise_price())