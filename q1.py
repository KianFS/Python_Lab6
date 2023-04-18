import math
from math import factorial

print("****************part1 e^n ******************")

n = int(input("enter the value of n: "))
x = int(input("enter the value of x: "))

sum_list = list(map(lambda k: (n ** k) / factorial(k), range(x + 1)))
e_to_n = sum(sum_list)

print(f"e^{n} = {e_to_n}")

print("****************part2******************")

result1 = 0


def sigma(n):
    """
    This function computes the sum of the series using a recursive function and a global variable.
    :param n: the number of items in the series to compute
    :return:nothing
    """
    global result1
    if n == 1:
        result1 = 1
    else:
        current_item = ((-1) ** (n + 1)) / n
        sigma(n - 1)
        result1 += current_item


n = int(input("Enter a number: "))
sigma(n)
print("result is: " + str(result1))
