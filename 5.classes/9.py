class Product:
    def __init__(self, price) -> None:
        self.__price = price

    def get_price(self):
        return self.__price

    def set_price(self, price):
        if (price < 0):
            raise ValueError("Price can not be less than zero!!!")
    price = property(get_price, set_price)
