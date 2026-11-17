class Ticket:
    price = 12000

    def __init__(self, title, person):
        self.title = title
        self.person = person

    def pay(self):
        return Ticket.price * self.person

t1 = Ticket("우주 여행", 3)
t2 = Ticket("바다 탐험", 2)
print(t1.pay())
print(t2.pay())

class Bread:
    shop = "행복 빵집"

    def __init__(self, name):
        self.name = name

a = Bread("소금빵")
b = Bread("크림빵")
print(a.name, Bread.shop) # (소금빵 행복 빵집)
print(b.name, Bread.shop) # (크림빵 행복 빵집)

class Fruit:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count

    def cost(self):
        return self.price * self.count

basket = []
basket.append(Fruit("사과", 1000, 3)) # 사과 3000
basket.append(Fruit("귤", 500, 4)) # 귤 2000

total = 0
for f in basket:
    total += f.cost()
print(total) # 사과 3000 + 귤 2000 = 5000

class Drink:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info(self):
        return f"{self.name} {self.price}원"

class Tea(Drink):
    def hot(self):
        return f"따뜻한 {self.name}"

t = Tea("녹차", 4000)
print(t.info())
print(t.hot())

class Tea:
    def __init__(self, name, price):     # ← Drink에서 물려받음 (안 보이지만 있음)
        self.name = name
        self.price = price

    def info(self):                       # ← Drink에서 물려받음 (안 보이지만 있음)
        return f"{self.name} {self.price}원"

    def hot(self):                        # ← Tea가 직접 추가
        return f"따뜻한 {self.name}"


class Pet:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} 밥 먹는 중"

class Dog(Pet):
    def walk(self):
        return f"{self.name} 산책 중"

d = Dog("콩이")
print(d.eat()) #콩이 밥 먹는 중
print(d.walk()) #콩이 산책 중

class Drink:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info(self):
        return f"{self.name} {self.price}원"

class Ade(Drink):
    def info(self):
        return f"{self.name} {self.price}원 (얼음 가득)"

a = Ade("레몬에이드", 5500)
d = Drink("라떼", 4500)
print(a.info())
print(d.info())

class Weather:
    def __init__(self, city, temp):
        self.city = city
        self.temp = temp

    def report(self):
        return f"{self.city} {self.temp}도"

    def tip(self):
        return "좋은 하루 보내세요"

class Rain(Weather):
    def tip(self):
        return "우산 챙기세요"

r = Rain("부산", 15)
print(r.report()) # 부산 15도
print(r.tip()) # 우산 챙기세요