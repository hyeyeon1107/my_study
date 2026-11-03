'''
1열: 1-1 1-2 1-3 1-4 1-5 
2열: 2-1 2-2 2-3 2-4 2-5 
3열: 3-1 3-2 3-3 3-4 3-5
'''
print("="*30)

for row in range(1,4):
    print(f"{row}열: ", end="")
    for seat in range(1,6):
        print(f"{row}-{seat}", end=" ")
    print()