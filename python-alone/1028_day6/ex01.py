# 파이썬 Day 6 (2026-10-28) - 7장 Set
visited = {"스타벅스", "이디야", "스타벅스", "메가커피"}
print(visited)

orders = ["라떼", "모카", "라떼", "녹차", "모카"]
menu = set(orders)
print(menu)
print(len(menu))

import random

dice = random.randint(1, 6)
print(dice)

import random

lunch = ["김치찌개", "돈까스", "냉면", "비빔밥"]
pick = random.choice(lunch)
print(f"오늘 점심은 {pick}!")

import random
drink = ["아이스티", "라떼", "레몬에이드"]
pick = random.choice(drink)
print(f"추천 음료: {pick}")

msg = "아이스 아메리카노"
short = msg.replace("아이스 ", "")
print(msg)
print(short)

coupon = "Cafe2026"
print(coupon.upper())
print(coupon.lower())
print(coupon)

answer = "YES"
if answer.lower() == "yes":
    print("확인됐어요")

phone = "010-1234-5678"
file = "menu.png"
print(phone.startswith("010"))
print(file.endswith(".png"))
print(file.endswith(".jpg"))

