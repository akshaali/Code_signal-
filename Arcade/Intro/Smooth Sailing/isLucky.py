""""
Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.

Example

For n = 1230, the output should be
isLucky(n) = true;
For n = 239017, the output should be
isLucky(n) = false.

""""

def isLucky(n):
    l = len(str(n))
    n_list = list(str(n))
    half_1, half_2 = 0, 0
    for j in range(int(l/2)):
        half_1 += int(n_list[j])
        half_2 += int(n_list[l-j-1])
    if half_1 == half_2:
        return 1
    else:
        return 0
