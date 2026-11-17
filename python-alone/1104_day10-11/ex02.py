class Bike:
    def __init__(self, name, minute):
        self.name = name
        self.minuet = minute

    def fee(self):
        return 500 * (self.minute//10)

b = Bike("하늘", 35)
print(b.name, b.fee())