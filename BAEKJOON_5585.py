#BAEKJOON_5585

a = int(input())
a = 1000 - a
cnt = 0

if(a >= 500):
    a -= 500
    cnt += 1

if(a >= 100):
    b = a // 100
    a -= 100 * b
    cnt += b

if(a >= 50):
    a -= 50
    cnt += 1

if(a >= 10):
    b = a // 10
    a -= 10 * b
    cnt += b

if(a >= 5):
    a -= 5
    cnt += 1

print(cnt + a)