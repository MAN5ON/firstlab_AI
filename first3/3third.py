def func():
    n = int(input('Enter N from -100 000 to 100 100: '))
    if -100000 > n or n > 100000:
        print('Error! Wrong number')
        func()
    else:
        odd = 0
        even = 0
        f = 0
        k = 0
        dict_even = {}
        dict_odd = {}
        while n > 0:
            if n % 2 == 0:
                even += 1
                f += 1
                i = n % 10
                dict_even[f] = i
                n = n // 10

            else:
                odd += 1
                k += 1
                j = n % 10
                dict_odd[k] = j
                n = n // 10

    print(' Четных: ' + str(even) + ' Сумма четных: ' + str(sum(dict_even.values()))
          + ' Нечетных: ' + str(odd) + ' Сумма нечётных: ' + str(sum(dict_odd.values())))


func()
