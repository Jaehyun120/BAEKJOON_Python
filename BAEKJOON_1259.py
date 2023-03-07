#BAEKJOON_1259

while True:
    a = input()

    if a == '0':
        break


    while a[0] == '0':
        a = a[1:]

    b = True
    for i in range(0, (len(a) // 2), 1):
        if a[i] != a[len(a) - i - 1]:
            b = False
            break
    
    if b == True:
        print("yes")
    else:   print("no")