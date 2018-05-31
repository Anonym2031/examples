def sort_sum_fact(arr):
    print("To sort, Type \n Up  or Down \n or Exit for close")
    s = str(input("Sorting Method    -"))
    if s == "Up":
        arr = list((sorted(arr)))
        sum_elem(arr)
        fact(arr)
    elif s == "Down":
        arr = list(reversed(sorted(arr)))
        sum_elem(arr)
        fact(arr)

    elif s == "Exit":
        return s
    else:
        print("Error")

    while s == "Exit":
        break
    sort_sum_fact(arr)


def sum_elem(arr):
    s = int(0)
    for i in range(int(len(arr))):
        s += arr[i]
    print("Elements Sum- ", s)


def fact(arr):
    s = int(1)
    for i in range(int(len(arr))):
        s *= arr[i]
    print("Elements Multiply - ", s)


a = [_ + 1 for _ in range(20)]
sort_sum_fact(a)
