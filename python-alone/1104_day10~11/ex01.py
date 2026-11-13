# 2026-11-04 파이썬 Day 10 — 12장 클래스
# 복습 문제와 오늘 예제를 여기에 적어 보세요.

try:
    cups = int("두잔")
    print("주문 완료")
except ValueError:
    print("숫자로 입력해 주세요")
else:
    print("결제 진행")
finally:
    print("영수증 출력")
print("다음 손님")

try:
    price = 3000 / 0
except ZeroDivisionError as e:
    print(e)

    
class Item:
    def __init__(self, name, count):
        self.name = name
        self.count = count

a = Item("우유", 2)
b = Item("계란", 10)
print(a.name, b.count)

class Cafe:
    def __init__(self, drink, size):
        self.drink = drink
        self.size = size

c = Cafe("녹차", "톨")
print(c.drink)
print(c.size)

class Score:
    def __init__(self, name, kor, eng):
        self.name = name
        self.kor = kor
        self.eng = eng

    def avg(self):
        return (self.kor + self.eng) / 2

s1 = Score("민지", 80, 90)
s2 = Score("서준", 70, 100)
print(s1.avg()) #85
print(s2.name, s2.avg()) #서준 85


class Ticket:
    def __init__(self, title, person):
        self.title=title
        self.person=person

    def pay(self):
        return 12000*self.person


price = 12000
class Ticket:
    def __init__(self, title, person):
        self.title=title
        self.person=person

    def pay(self):
        return price*self.person

# 둘 다 가능하다 다른 방법 3번째도 있는데 추후 배우면서 설명한다고 함

