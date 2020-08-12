#   Using pass and break

for x in range(30):
    if x % 2 == 0:
        print(x, 'is par')
    elif x == 25:
        print('X is equal 25. BREAK.')
        break
    else:
        pass

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)