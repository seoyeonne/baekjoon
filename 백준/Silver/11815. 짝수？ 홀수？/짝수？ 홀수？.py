N = int(input())
X = list(map(int, input().split()))

for x in X:
    if x == int(x ** 0.5) ** 2:
        print(1, end=' ')
    else:
        print(0, end=' ')
print()
