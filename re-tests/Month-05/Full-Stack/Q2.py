n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def min_Difference(a,b, n, m):
    a.sort()
    b.sort()
    result = float("inf")
    p1 = 0
    p2 = 0
    while p1 < n and p2 < m:
        total = abs(a[p1] - b[p2])
        if total < result:
            result = total
        if a[p1] < b[p2]:
            p1 += 1
        
        else:
            p2 += 1
    return result

print(min_Difference(a, b, n, m))


# 1 3 15 11 2
# 23 127 235 19 8 

