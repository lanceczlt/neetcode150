a = [4, 0, 1, -2, 3]
n = 5

b = [0 for _ in range(n)]

def solution(a, n):
    b[0] = a[0] + a[1]
    b[n - 1] = a[n - 2] + a[n - 1]


    for i in range(1, n - 1):
        b[i] = a[i - 1] + a[i] + a[i + 1]
    
    return b

print(solution(a, n))