n, a = map(int, input().split())
x = list(map(int, input().split()))
sum_x = sum(x)
y_opt = (sum_x - (a * n) / 2) / n

total = 0.0
for xi in x:
    total += (y_opt - xi) ** 2 + a * y_opt

print(total)