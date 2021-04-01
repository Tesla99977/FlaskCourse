print("Enter your number: ")
n = int(input())
def magicSpiral(n):
    num = 0
    matrix = [[0 for j in range(n)] for i in range(n)]
    j = 0
    total = 0
    print(matrix)
    i = 0
    step = n - 1;
    while num != n ** 2:

        k1 = 0
        if num == n ** 2 - 1:
            step = 1
        for k1 in range(step):
            # Вправо
            num += 1
            if num > n ** 2:
                matrix[i][i + k1] = num
                break
            matrix[i][i + k1] = num
        if num == n ** 2:
            break
        k2 = 0
        for k2 in range(step):
            # Вниз
            num += 1
            matrix[i + k2][n - i - 1] = num
        k3 = 0
        for k3 in range(step):
            # Влево
            num += 1
            matrix[n - i - 1][n - k3 - 1 - i] = num
        k4 = 0
        for k4 in range(step):
            # Вверх
            num += 1
            matrix[n - k4 - 1 - i][0 + i] = num
        i += 1
        step -= 2
    return matrix
print(magicSpiral(n))


