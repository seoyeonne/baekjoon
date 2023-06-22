a = int(input())
b = int(input())
c = int(input())

sum = a + b + c

if a == b == c == 60:
    print("Equilateral")
elif sum == 180 and (a==b or a == c or b == c):
    print("Isosceles")
elif sum == 180 and (a != b and b != c and c != a):
    print("Scalene")
elif sum != 180 :
    print("Error")