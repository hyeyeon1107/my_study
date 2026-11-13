cart = {"우유": 2800, "빵": 3500, "계란": 6000}

def receipt(basket):
    total = 0
    for name, price in basket.items():
        print (f"{name} {price}원")
        total += price
    print(f"총액 {total}원")
    return total
pay = receipt(cart)

if pay>=10000:
    print("배송비 무료")
else:
    print("배송비 3000원")