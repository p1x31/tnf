s = input().strip()
n = len(s)
from collections import defaultdict

counts = defaultdict(int)

for j in range(n):
    c = s[j]
    count = (j + 1) * (n - j)
    counts[c] += count

# Sort the keys and print
sorted_chars = sorted(counts.keys())
for char in sorted_chars:
    print(f"{char}: {counts[char]}")