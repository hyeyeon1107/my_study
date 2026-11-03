coin = [[500, 100],
        [100, 50, 10]]

total = 0
for row in coin:
    for c in row:
        total += c

print(total)
