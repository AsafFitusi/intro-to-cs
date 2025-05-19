"""""
student: Asaf Fitusi
ID:318763430
Assignment no.2
program:rounding

"""

def round_down(n, k):
    """
    This function rounds the number "n" down to the nearest multiple of "k".
    """
    if n % k == 0:
        return n
    else:
        n = n - n % k
        return n 

def round_up(n, k):
    """
    This function rounds the number "n" up to the nearest multiple of "k".
    """
    if n % k == 0:
        return n 
    else:
        n = n + (k - n % k)
        return n

def round_(n, k):
    """
    This function rounds the number "n" to the nearest multiple of "k".
    If "n" is equally far from two multiples, it returns the larger one.
    """
    up = round_up(n, k) - n
    down = n - round_down(n, k)
    if up == down:
        return max(round_up(n, k), round_down(n, k))
    else:
        if up > down:
            return round_down(n, k)
        else:
            return round_up(n, k)

def main():
    """
    this function asks the user to enter a range of Fahrenheit temperatures
    (minimum and maximum). It then rounds these values to the nearest multiples of 10 and
    converts them to Celsius, displaying the results in a table.
    """
    k = 10
    min = int(input("please enter an min:"))
    max = int(input("please enter an max:"))
    if min > max or min == max:
        print("min should be smaller then max")
    else:
        round_(min, k)
        round_(max, k)
        print("                      ")
        print("fahrenheit    celsius")
        print("_ _ _ _ _     _ _ _ _ _ ")
        c = round_(min, k)
        for i in range(round_(min, k), round_(max, k) + 1, 5):
            c = (i - 32) * 5 / 9
            print(str(i), "             ", int(c))

main()