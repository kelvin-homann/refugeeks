def countUp(n):
    if n > 0:
        countUp(n - 1)
        print(n)


countUp(10)
