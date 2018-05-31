def div_2_3_sum(arr):
    s = 0
    for i in range(int(len(arr))):
        if arr[i] % 2 == 0:
            if arr[i] % 3 == 0:
                s += arr[i]
                print(arr[i])
    print(" Sum  -- ", s)


a = [_ + 1 for _ in range(100)]
div_2_3_sum(a)
