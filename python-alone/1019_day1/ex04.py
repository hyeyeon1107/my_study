# 처음 푼 방식
# name = "민지"
# money = 50000
# use_money = 32000

# print("이름: ",name)
# print("이번 달 용돈: ",money)
# print ("쓴 돈: ", use_money)
# print(f"민지님의 남은 용돈은 {money-use_money}원입니다")

# input 사용하는 방식으로 다시 풀기
name = input("이름: ")
money = int(input("이번 달 용돈: "))
use_money = int(input("쓴 돈: "))
print(f"{name}님의 남은 용돈은 {money-use_money}원입니다")


# 예제 5
#    25000 / 7000 3.5555...
#    25000//7000 3
#    25000%7000 4
#    4 ** 3 -> 잘못 이해함 3**2 

#예제 6
age=14
limit=15
print(age>=limit) #False
print(age==14) #True
print(age!=14) #True False -> True라고 생각한 이유 : age가 아니라 limit를 기준으로 생각함 바보
print(age<limit) #True

#예제 7
battery = 80
battery -= 30     # 게임을 해서 줄어듦 -> 50
battery += 50     # 충전함 -> 100
battery -= 10     # 영상을 봄 -> 90
print(battery) # -> 90

#예제 8
stamp = 8        # 모은 도장 개수
member = True    # 회원인지 여부

print(stamp >= 10 and member)    # ① False and True -> False
print(stamp >= 10 or member)     # ② False or True -> True
print(not member)                # ③ False -> False
print(stamp > 5 and stamp < 10)  # ④ True and True -> True