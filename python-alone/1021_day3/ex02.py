'''
dust = int(input("미세먼지 농도를 입력하세요: "))

if dust >= 151:
    print("매우 나쁨: 외출을 자제하세요")
elif dust >= 81:
    print("나쁨: 마스크를 꼭 쓰세요")
elif dust >= 31:
    print("보통")
else:
    print("좋음: 산책하기 좋은 날!")
'''

'''
# for

for table in range(1, 4):
    for guest in range(1, 3):
        print(f"{table}번 테이블 {guest}번 손님 주문 받음")
'''
        
for day in range(1, 3):
    print(f"{day}일차 운동 시작")
    for num in range(1, 4):
        print(f"스쿼트 {num}세트")-
    print("오늘 운동 끝")

# 1일차 운동 시작 
# 스쿼트 1세트 
# 스쿼트 2세트 
# 스쿼트 3세트  
# 오늘 운동 끝 
# 2일차 운동 시작 
# 스쿼트 1세트
# 스쿼트 2세트 
# 스쿼트 3세트 
# 오늘 운동 끝

