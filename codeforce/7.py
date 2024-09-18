n = int(input())

set = set(range(n, 0, -1))


for i in range(1, n):
    a = int(input())
    if a in set:
        set.remove(a)

print(set.pop())
