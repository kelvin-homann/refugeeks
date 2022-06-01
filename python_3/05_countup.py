def countUp(n):
    if n == 0:
        return
    else:
        countUp(n - 1)
        print(n)


countUp(5)
