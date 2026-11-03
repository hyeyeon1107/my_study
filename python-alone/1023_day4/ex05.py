# Day 4 - 빈 리스트 + append, 리스트 연산
cart = []
for i in range(1, 4):
    cart.append(i * 1000)
print(cart)       # [1000, 2000, 3000]

a = ["우유", "빵"]
b = ["계란"]
print(a + b)      # ['우유', '빵', '계란']
print(b * 3)      # ['계란', '계란', '계란']
