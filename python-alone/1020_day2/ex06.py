'''
for num in range(1, 8):
    if num % 3 == 0:
        print(f"{num}번 손님: 쿠폰 당첨!")

total = 0

for price in range(1000, 6000, 1000):
    if price >= 3000:
        total += price

print(total)

3000+4000+5000=12000
'''
''' # 내가 푼 거 틀림
print(int(input("며칠 동안 저금할까요? : ")))

total = 0

for day in range(1, 11, 2):
    if day >= 2:
        total += day

print(f"{day}일째: 2000원 저금 (누적 {total}원)")
'''

'''
days = int(input("며칠 동안 저금할까요? : "))

total = 0

for day in range(1, days + 1):
    if day % 2 == 0:
        total += 2000
        print(f"{day}일째: 2000원 저금 (누적 {total}원)")

print(f"총액: {total}원")
if total >= 10000:
    print("목표 달성! 🎉")
else:
    print("조금만 더 힘내요!")
#고친 거
'''

count = 0
for n in range(5, 0, -1):
    count += 1
print(count)

for i in range(1, 4):
    total = 0
    total += i
print(total)