snack = {"삼각김밥": 1500, "바나나우유": 1700, "컵라면": 1300}
print(snack["바나나우유"]) #1700

weather = {"월": "맑음", "화": "비", "수": "흐림"}
print(weather["화"]) #비

snack = {"삼각김밥": 1500, "컵라면": 1300}
snack["바나나우유"] = 1700
snack["컵라면"] = 1400
print(snack) #{'삼각김밥': 1500, '컵라면': 1400, '바나나우유': 1700}

money = {"용돈": 30000, "간식": 5000}
money["간식"] = 8000
money["교통"] = 12000
print(money)
# {'용돈': 30000, '간식': 8000, '교통': 12000}

snack = {"삼각김밥": 1500, "컵라면": 1300, "바나나우유": 1700}
for name in snack:
    print(name, snack[name])
#삼각김밥 1500
#컵라면 1300
#바나나우유 1700

score = {"국어": 90, "수학": 75, "영어": 85}
for subject in score:
    print(f"{subject}: {score[subject]}점")
#국어: 90점
#수학: 75점
#영어: 85점

snack = {"삼각김밥": 1500, "컵라면": 1300, "바나나우유": 1700}
for name, price in snack.items():
    print(name, price)

#삼각김밥 1500
#컵라면 1300
#바나나우유 1700

cart = {"우유": 2, "식빵": 1, "계란": 10}
for item, count in cart.items():
    print(f"{item} {count}개")
#우유 2개
#식빵 1개
#계란 10개

snack = {"삼각김밥": 1500, "컵라면": 1300}
order = "떡볶이"
if order in snack:
    print(snack[order])
else:
    print("없는 메뉴예요")
#없는 메뉴예요


weather = {"월": "맑음", "화": "비", "수": "흐림"}
print("화" in weather) # True
print("비" in weather) # False


bag = {"지갑": 1, "우산": 2}
print("우산" in bag) # True
print(bag["우산"]) # 2

snack = {"삼각김밥": 1500, "컵라면": 1300}
print(snack.get("컵라면"))
print(snack.get("떡볶이"))
print(snack.get("떡볶이", 0))

stock = {"사과": 5, "배": 0}
print(stock.get("배")) # 0
print(stock.get("귤", "품절"))  # 품절

point = {"민지": 300}
print(point.get("준호", 0)) #0
print(point.get("준호")) #None