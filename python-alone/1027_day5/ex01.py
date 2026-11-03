li = [12, 7, 15, 3]
#for i in range(n):
#for i in range(0, n, m): -> 0 이상 n 미만의 범위에서 (n은 포함 안 됨) m만큼의 간격으로
#for i in li:

for i in range(len(li)-1):
    for j in range(i+1, len(li)):
        if li[i] > li[j]:
            tmp = li[i]
            li[i] = li[j]
            li[j] = tmp    

        print(f'i: {i}, j: {j} -> {li}')

print(li)

cards = [5, 8, 1, 4]

for i in range(3):
    for j in range(i+1, 4):
        if cards[j] < cards[i]:
            cards[i], cards[j] = cards[j], cards[i]
    print(i+1, "회전:", cards)

print(cards)

score = [70, 95, 80]
rank = [1, 1, 1]

for i in range(3):
    for j in range(3):
        if score[j] > score[i]:
            rank[i] += 1

print(rank)

jump = [40, 65, 52, 30]
rank = [1, 1, 1, 1]

for i in range(4):
    for j in range(4):
        if jump[j] > jump[i]:
            rank[i] += 1

print(rank)

menu = ["라떼", "모카", "녹차"]
z = menu.reverse()
print("z:", z)
print("menu:", menu)

menu = ["라떼", "모카", "녹차"]
menu.reverse()
print("menu:", menu)