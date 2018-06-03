def square(a):
    p = str("P =  " + str(a*3))
    s = str("S =  " + str(a*a))
    v = str("V =  " + str(a**3))
    cub = (p, s, v)
    return cub


obj = int(input("Input number    - "))
print("\n", square(obj))
