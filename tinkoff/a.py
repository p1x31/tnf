n, a = map(int, input().split())
t = list(map(int, input().split()))
prev_end = 0
for ti in t:
    start = max(ti, prev_end)
    end = start + a
    print(end)
    prev_end = end