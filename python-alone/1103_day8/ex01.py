# 1103 파이썬 Day 8 - 함수 나머지 + 모듈
def order(menu, size="톨"):
    print(f"{menu} {size} 사이즈")

order(size="그란데", menu="모카")

def bake(bread, count=1):
    print(f"{bread} {count}개 구웠어요")

bake(count=5, bread="베이글")

def show(*snacks):
    print(snacks)
    print(len(snacks))

show("쿠키", "젤리", "초코")

def add_tax(price):
    return price + 500

prices = [3000, 4500, 2000]
new_prices = list(map(add_tax, prices))
print(new_prices)

new_prices = []
for p in prices:
    new_prices.append(add_tax(p))

from random import choice
print(choice(["라떼", "모카"]))