phone = "010-1234-5678"
phone.replace("-", "")
print(phone)

phone = "010-1234-5678"
new = phone.replace("-", "")
print(new)

word = "latte"
big = word.upper()
print(word)
print(big)

seat = {"A1": "예약", "A2": "빈자리"}
print(seat["A2"])
print("B1" in seat)
print(seat.get("B1", "없는 좌석"))

bus = {"101": "10분", "202": "3분"}
print("303" in bus)
print(bus.get("303", "정보 없음"))
print(bus)

bus = {"101": "10분"}

print("303" in bus)
print(bus)

print(bus.get("303", "정보 없음"))
print(bus)

bus["303"] = "7분"
print(bus)

cafe = {"라떼": 4500}
print("모카" in cafe)
print(cafe.get("모카", 0))
print(cafe)