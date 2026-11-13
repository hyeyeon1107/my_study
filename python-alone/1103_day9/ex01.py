# 1103 파이썬 Day 9 - 예외처리
try:
    money = int(input("용돈 : "))
    day = money // 7
    print(f"하루 {day}원")
except ValueError:
    print("숫자만 입력해 주세요")

    