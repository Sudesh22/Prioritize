M = int(input())
Y = int(input())
R = int(input())
G = int(input())

if ((Y+R) or (Y*R)) > M:
    print(Y+R)
    print(Y*R)
    print(1)
else:
    print(0)