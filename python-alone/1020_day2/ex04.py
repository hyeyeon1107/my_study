stamp = int(input("스탬프 개수를 입력하세요: "))

if stamp >= 10:
    print("무료 음료 쿠폰 발급!")
elif stamp >= 5:
    print("사이즈 업 쿠폰 발급!")
else:
    print("스탬프를 더 모아주세요")

    age = 25
has_ticket = True

if age >= 19 and has_ticket == True:
    print("입장하세요")
else:
    print("입장할 수 없어요")

day = "토요일"
rain = False

if day == "토요일" or day == "일요일":
    print("주말이에요")

if day == "토요일" and rain == True:
    print("집에서 영화를 봐요")
else:
    print("공원에 산책 가요")

# 주말이에요 공원에 산책 가요

'''
if, elif, else는 각각 언제 쓰나요? 조건식이 필요한 것과 필요 없는 것도 함께 말해 주세요.
if 조건에 맞는 걸 출력 시킬 때, elif 조건들 중에 필요한 조건이 나왔을 경우 이후 출력을 막아줌,
else 모든 조건에 충족하지 않을 때 출력. else는 조건식이 따로 필요하지 않음.
if를 따로 여러 개 쓰는 것과 if – elif로 묶어 쓰는 것은 어떻게 다른가요?
if를 따로 여러 개 쓰면 여러가지 조건이 충족될 경우 전부 출력이 됨. 
if-elif로 묶을 경우 처음으로 조건이 충족된 이후로는 이후 출력이 나오지 않음.
'''