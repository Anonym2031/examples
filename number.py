def number(arr):
    b = int(0)
    c = int(0)
    for i in range(int(len(arr))):
        print(arr[i])
        z = int(len(arr)) // 2
        if int(i) % z == 1:
            b = i
            c = arr[i]
    print("index -- ", b)
    print("number  -- ", c)


a = [_ + 1 for _ in range(22)]
number(a)
