# Day 4 - 반복문 연습 1: 저금통 (while 직접 작성)
# 매일 1500원씩, 10000원 이상이 될 때까지
day = 0
money = 0
while money < 10000:      # while에는 "계속할 조건"
    money += 1500
    day += 1
    print(f"{day}일차: {money}원")   # 같은 반복 안의 줄은 모두 4칸
print("목표 달성!")                  # while 밖(0칸) → 1번만

# 1일차: 1500원 ~ 7일차: 10500원
# 목표 달성!
