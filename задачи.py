m, n = map(int, input().split())
numbers = [True] * (n + 1)
for i in range(2, int(n ** 0.5) + 1):
    if numbers[i]:
        for j in range(i ** 2, n + 1, i):
            numbers[j] = False
primes_found = False
for i in range(m, n + 1):
    if numbers[i]:
        print(i, end=' ')
        primes_found = True
if not primes_found:
    print('Absent')