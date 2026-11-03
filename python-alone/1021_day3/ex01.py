print("녹차" != "녹차") # False
print(5 != 9) # True

for n in range(3, 12, 4):
    print(n)
# 3, 7, 11

for n in range(6, 0, -2):
    print(n)
# 6,4,2

# (가)
cups = 0
for day in range(3):
    cups += 2
print(cups)

# 6

# (나)
for day in range(3):
    cups = 0
    cups += 2
print(cups)
# 2

# (가)는 상자를 한 번만 비우고 3일치를 계속 쌓음, (나)는 매일 아침 상자를 비우고 그날 2잔만 담음

for n in range(2, 10, 3):
    print(n)
    # 2, 5, 8

for n in range(9, 0, -3):
    print(n)
    # 9, 6, 3

for week in range(4):
    money = 0
    money += 5000
print(money)
    # 5000