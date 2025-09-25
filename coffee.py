from order import Order

class Coffee:
    def __init__(self, name: str):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        # name must be set only once (immutable after creation)
        if hasattr(self, "_name"):
            raise AttributeError("Coffee name cannot be changed after creation.")
        if isinstance(value, str) and len(value) >= 3:
            self._name = value
        else:
            raise ValueError("Coffee name must be a string with at least 3 characters.")

    # relationship methods
    def orders(self):
        return [order for order in Order.all if order.coffee is self]

    def customers(self):
        return list({order.customer for order in self.orders()})

    # aggregate methods
    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        orders = self.orders()
        if not orders:
            return 0
        return sum(order.price for order in orders) / len(orders)
