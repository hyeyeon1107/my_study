print("="*10)

for row in range(1, 4):
    for cup in range(1, row + 1):
        print("☕", end="")
    print()
# ☕
# ☕☕
# ☕☕☕
# print()가 1칸이면 바깥 for(row)에 속해요. 
# → 안쪽 for가 커피를 다 그린 다음에 한 번 엔터 → 줄마다 1번

print("="*10)

for row in range(1, 4):
    for cup in range(1, row + 1):
        print("☕", end="")
        print()
# ☕
# ☕
# ☕
# ☕
# ☕
# ☕
# print()가 2칸이면 안쪽 for(cup)에 속해요. → 커피를 한 잔 그릴 때마다 엔터