for i in range(3):
    print("물을 한 잔 마셔요")

for i in range(3):
    print(i, "번째 손님 주문 받기")
'''
for i in range(1, 5):
    print(f"{i}층 청소 완료")
print("퇴근!")
1층 청소 완료
2층 청소 완료
3층 청소 완료
4층 청소 완료
# 5층 청소 완료 -> 1, 5기 때문에 5는 포함하지 않는다.
퇴근!

for day in range(3):
    print("출근")
    print("퇴근")
출근
퇴근
출근
퇴근
출근
퇴근
'''

total = 0

for i in range(1, 5):
    total += i

print(total)
# 0+1+2+3+4 = 10

for minute in range(0, 31, 10):
    print(f"{minute}분: 스트레칭")
# 0분: 스트레칭
# 10분: 스트레칭 
# 20분: 스트레칭 
# 30분: 스트레칭

# Q.
total = 0
for day in range(1, 8):
    total += 3000
    print(f"{day}일째 누적 걸음: {total}걸음")
print(f"일주일 총 걸음: {total}걸음")