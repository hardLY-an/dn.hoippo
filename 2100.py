n,m = list(map(int, input().split()))

res = (n**2) - m

for i in range(m):
    res -= 2*(n-1-i)

# res = n**2 - (m*(2*n-m)) 	slower

print(res)
