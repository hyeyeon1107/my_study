# Day 4 - while 다시 배우기

# ① print가 while 밖 → 1번만
n = 10
while n > 0:
    n -= 3
print(n)        # -2

# ② print가 while 안 → 매 바퀴
n = 10
while n > 0:
    n -= 3
    print(n)    # 7 4 1 -2

# ③ break: if에는 "멈추고 싶은 상황"
n = 10
while n > 0:
    n -= 3
    if n < 0:
        break
    print(n)    # 7 4 1
