def bell():
    print("딩동")

print("시작")
bell()
print("끝")

def order(menu):
    print(f"{menu} 한 잔 나왔습니다")

order("라떼")
order("모카")

def weather(city):
    print(f"{city} 날씨를 알려 드려요")

weather("제주")
weather("서울")

def pay(item, price):
    print(f"{item}: {price}원")

pay("우유", 2500)
pay("식빵", 3000)

def total(price, count):
    return price * count

money = total(4500, 2)
print(money)
print(total(1500, 3))

def add_tip(price):
    return price + 1000

result = add_tip(5000)
print(result) #6000
print(add_tip(2000)) #8000??

#?? 원래 그럼 5000원인데 한 번 받아서 5000+1
#근데 add_tip 2000이라고 적혀있으면 이걸 어캐 받아야대?? 아님 내가 이해 잘못한 걸까

'''
첫 번째 6000은 정답이에요! 👍 두 번째는 3000이에요. 좋은 질문이라 바로 설명할게요.

8000은 앞에서 나온 6000에 2000을 더한 거죠? 그런데 함수는 호출할 때마다 처음부터 새로 시작해요. 앞 호출의 결과를 기억하지 않아요. 어제 get()의 기본값이 다음 줄까지 이어지지 않았던 것과 같아요.

호출	빈칸 price에 들어가는 값	계산	돌려주는 값
add_tip(5000)	5000	5000 + 1000	6000
add_tip(2000)	2000 (새로)	2000 + 1000	3000

레시피 카드로 보면 이래요. 첫 주문은 “5000원짜리에 팁 붙여 줘”, 두 번째 주문은 “2000원짜리에 팁 붙여 줘”예요. 두 번째 주문은 첫 주문과 상관없어요. 괄호에 넣은 그 값 하나만 받아요.

6000은 result 상자에 담겨 있을 뿐이고, 함수 안으로 들어가지 않아요. 만약 6000에 이어서 더하고 싶다면 add_tip(result)처럼 직접 넣어 줘야 해요.
'''

def double(n):
    return n * 2

print(double(3)) #6
print(double(10)) #20

def total_a(price, count):
    print(price * count)

def total_b(price, count):
    return price * count

#문제 할인 가격을 계산해서, 그 결과를 다른 계산에 또 쓰고 싶어요. print 함수와 return 함수 중 어느 쪽으로 만들어야 할까요? 이유도 한 줄로 써 주세요.
# return을 써야함. print는 화면에 보여주지만 기억하지 않기 때문에 사라짐. return은 값을 건네주고, 변수 기억하고 있기 때문에 다음에 이어서 사용하고 싶으면 return을 쓰는 게 맞다.
# return은 값을 밖으로 건네준다 → 상자에 담으면 상자가 기억한다 → 다음 계산에 쓸 수 있다.

def make():
    cup = "라떼"
    print(cup)

make()
print(cup)
'''
라떼
NameError: name 'cup' is not defined
'''

def make():
    cup = "라떼"
    return cup

drink = make()
print(drink)     # 라떼