a = 0
for a in range(0,100):
    a += 1
    if a % 7 == 0 or a % 10 ==7 or a // 10 ==  7:
        continue
    print(a)
