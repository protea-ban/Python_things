class Goods(object):
    def __init__(self):

        self.original_price = 100
        self.discount = 0.8

    @property
    def price(self):
        new_price = self.original_price * self.discount
        return new_price

    @price.setter
    def price(self, value):
        self.original_price = value

    @price.deleter
    def price(self, value):
        del self.original_price


if __name__ == '__main__':
    obj = Goods()
    # print(obj.price)
    obj.price = 200
    print(obj.price)

    del obj.price