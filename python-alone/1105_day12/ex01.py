# 1105 파이썬 Day 12 — 총정리
# 복습 문제와 종합 문제를 여기에 적어 보세요.

class Cake:
    def __init__(self, flavor, price):
        self.flavor = flavor
        self.price = price

    def info(self):
        print(f"{self.flavor} 케이크 {self.price}원")

c = Cake("딸기", 6000)
c.info()

cart = ["우유", "빵", "계란"]
cart.append("사과") #["우유", "빵", "계란", "사과"]
first = cart.pop(0) 
print(first) 
print(cart)
print(len(cart))

date = "2026-11-05"
print(date[5:7])
print(date[:4])

stock = {"라떼": 5, "모카": 0}
stock["녹차"] = 3
print("모카" in stock) #True
print(stock.get("홍차", "없는 메뉴")) #없는 메뉴
print(stock["라떼"] + stock["녹차"]) #8

def tip(price, rate=10):
    print(price * rate // 100)

def total(price, rate=10):
    return price + price * rate // 100

a = tip(5000)
b = total(5000, 20)
print(a)
print(b)