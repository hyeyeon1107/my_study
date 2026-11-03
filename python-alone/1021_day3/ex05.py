cup = 1
while cup <= 3:
    print(f"{cup}번째 커피 내리는 중")
    cup += 1
print("커피 완성")

# 1번째 커피 내리는 중
# 2번째 커피 내리는 중
# 3번째 커피 내리는 중 
# 커피 완성

print(f"반복이 끝난 뒤 cup: {cup}")

pw = ""
while pw != "cafe1234":
    pw = input("비밀번호를 입력하세요: ")
print("와이파이 연결 완료!")
# cafe랑 1234만 눌렀을 때는 다시 비밀번호를 입력하세요로 돌아간다.
# 왜냐면 cafe1234가 아니기 때문에 반복. 
# cafe1234를 작성했을 시, 와이파이 연결 완료! 라고 메시지가 뜬다.

pw = ""
while pw == "cafe1234":
    pw = input("비밀번호를 입력하세요: ")
print("와이파이 연결 완료!")
# False 아닌가? 
# 와이파이 연결 완료!만 뜸

count = 0
while True:
    menu = input("메뉴를 입력하세요 (주문 마감은 '끝'): ")
    if menu == "끝":
        break
    print(f"{menu} 추가!")
    count += 1
print(f"총 {count}잔 주문 완료")