
n = int(input("Enter a value for n: "))
i = 2
while i <= n:
    j = 0
    while j <= n:
        print(i, j)
        j = j + n // 4
    i = i + 1