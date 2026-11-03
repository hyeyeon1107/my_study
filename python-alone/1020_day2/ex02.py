temp = 31

if temp >= 28:
    print("에어컨을 켭니다")

print("하루 시작!")

money = 3000

if money >= 4500:
    print("아메리카노를 삽니다")

print("카페를 나갑니다")
# 카페를 나갑니다만 출력됨. 
# 사유 : 4500원보다 금액이 적기 때문에 
# 아메리카노를 살 수 없어서 아메리카노를 삽니다가 출력 불가.

weather = "비"

if weather == "비":
    print("우산을 챙겨요")
    print("장화를 신어요")

if weather != "맑음":
    print("선글라스는 두고 가요")
# 우산을 챙겨요. \n 장화를 신어요 출력됨. 비가 온다고 입력했기 때문.
# 맑음과 같지 않기 때문에 선글라스는 두고 가요도 출력됨.

money = 3000

if money >= 5000:
    print("라떼를 삽니다")
else:
    print("물을 마십니다")
# 물을 마십니다. 출력.

score = 75

if score >= 80:
    print("합격")
else:
    print("불합격")
print("시험 끝")
# 불합격 시험 끝 출력. 80점보다 값이 작기 때문에 else와 마지막 print만 출력한다.

temp = 25

if temp >= 30:
    print("반팔")
elif temp >= 20:
    print("긴팔")
else:
    print("패딩")

point = 85

if point >= 90:
    print("A")
elif point >= 80:
    print("B")
elif point >= 70:
    print("C")
else:
    print("F")

# B

point = 85

if point >= 90:
    print("A")
if point >= 80:
    print("B")
if point >= 70:
    print("C")
# B, C 둘 다 출력

height = input("키를 입력하세요: ")

if height >= 120:
    print("탑승 가능")

# 130 입력시 탑승 가능이 뜬다.