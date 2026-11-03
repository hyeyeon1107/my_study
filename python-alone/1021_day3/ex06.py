'''
가격을 입력하세요 (끝내려면 0): 3000
가격을 입력하세요 (끝내려면 0): 4500
가격을 입력하세요 (끝내려면 0): 1200
가격을 입력하세요 (끝내려면 0): 0
총 8700원입니다
'''

total=0
while True:
    money=int(input("가격을 입력하세요 (끝내려면 0): "))
    if money== 0:
        break
    total += money
print(f"총 {total}원 입니다")