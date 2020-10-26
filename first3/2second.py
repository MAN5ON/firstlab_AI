def func():
    i = 0
    n = int(input('Enter N in the interval from 1 to 20: '))
    if 0 < n <= 20:
        while i <= n:
            print(str(i) + ' в квадрате: ' + str(i**2))
            i = i + 1
    func()

func()
