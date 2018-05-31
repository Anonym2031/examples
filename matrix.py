def sum_diagonal(arr):
    n = 5
    s = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                s += arr[i][j]
    print("Sum on the main diagonal in matrix  =  ", s)


a = [[1, 2, 4, 5, 6],
     [2, 5, 7, 8, 6],
     [1, 4, 5, 8, 7],
     [1, 5, 4, 7, 8],
     [9, 8, 7, 5, 6]]

sum_diagonal(a)
