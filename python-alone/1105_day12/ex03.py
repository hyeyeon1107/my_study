money = 20000
spend = {"월": 4500, "화": 3000, "수": 6000, "목": 2500}

def report(pay):
    total = 0
    for day, spend_money in pay.items():
        print(f"{day}요일 {spend_money}원 사용")
        total += spend_money
    print(f"이번 주 사용 {total}원")
    return total
use_money = report(spend)

remain = money-use_money

if remain>=0:
    print(f"남은 용돈 {remain}원")
else:
    print("용돈 초과!")