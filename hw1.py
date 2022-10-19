a, b, c = map(int, input().split())

d = b**2 - 4*a*c

if d < 0:
    print("Корней нет")
elif d == 0:
    print(f"x = {-b/(2 * a)}")
else:
    print(f"x1 = {(-b + d**0.5)/(2 * a)}, x2 = {(-b - d**0.5)/(2 * a)}")
