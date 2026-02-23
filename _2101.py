n,m = list(map(int, input().split()))

a = list(map(int, input().split()))

sum_min = 0

k = 0

while True:
    try:
        if (sum_min + min(a) <= m):
            sum_min += min(a)
            a.remove(min(a))
            k += 1
        else:
            break
    except ValueError:
        break

print(k)