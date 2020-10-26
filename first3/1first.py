import math


def function():
    n = int(input('Enter N in the interval from -100 to 100: '))
    if n > 100 or n < -100:
        print("Error! N can only be in the interval -100 <= N <= 100 ")
        function()
    else:
        if n > 0 and n % 2 != 0 and math.sqrt(n) > 10:
            print('Weird')
            function()
        elif 2 <= n <= 4 and n % 2 == 0:
            print('Weird')
            function()
        elif n < 0 and n % 2 == 0 and 60 < n ** 2 < 100:
            print('Weird')
            function()
        elif n % 2 != 0 and 20 <= n <= 50 or 70 <= n <= 100:
            print('Not Weird')
            function()
        else:
            print('OUT OF LENGTH')
            function()
function()