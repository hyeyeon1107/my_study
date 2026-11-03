# Day 4 - 리스트 기본
menu = ["아메리카노", "라떼", "모카"]
print(menu)       # ['아메리카노', '라떼', '모카']
print(menu[1])    # 라떼 (번호는 0부터)
print(len(menu))  # 3

for m in menu:
    print(f"{m} 주문 가능")   # 3줄

menu.append("녹차")
print(menu)       # ['아메리카노', '라떼', '모카', '녹차']
