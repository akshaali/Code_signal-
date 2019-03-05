""""
Check if all digits of the given integer are even.

Example

For n = 248622, the output should be
evenDigitsOnly(n) = true;
For n = 642386, the output should be
evenDigitsOnly(n) = false.

""""

def evenDigitsOnly(n):
    n = str(n)
    sum_n = 0
    for r in n:
        if int(r)%2 != 0 :
            return False
    return True

