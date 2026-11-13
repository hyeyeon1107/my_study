latte = 4500

try:
    cup = int(input("몇 잔? "))
    total = latte * cup
    print(f"총 {total}원")

except ValueError:
    print("잔 수를 숫자로 입력해 주세요")