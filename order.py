class Order:
    all = []  # class-level storage of all orders

    def __init__(self, customer, coffee, price: float):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        from customer import Customer
        if isinstance(value, Customer):
            self._customer = value
        else:
            raise ValueError("Order must be associated with a valid Customer.")

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        from coffee import Coffee
        if isinstance(value, Coffee):
            self._coffee = value
        else:
            raise ValueError("Order must be associated with a valid Coffee.")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value: float):
        if hasattr(self, "_price"):
            raise AttributeError("Price cannot be changed after creation.")
        if isinstance(value, (int, float)) and 1.0 <= float(value) <= 10.0:
            self._price = float(value)
        else:
            raise ValueError("Price must be a float between 1.0 and 10.0.")
