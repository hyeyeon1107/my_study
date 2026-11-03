name = input("이름: ")
age = int(input("나이: "))
money = int(input("가진 돈: "))
pay = 12000
limit = 15

print(f"{name}님은 이 영화를 볼 수 있나요? {age>=limit}")
print(f"살 수 있는 표: {money // pay}장")
print(f"표를 최대한 사고 남는 돈: {money % pay}원")
#print(f"표를 최대한 사고 남는 돈: {money-pay}원")