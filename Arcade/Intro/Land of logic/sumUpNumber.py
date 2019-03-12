"""
CodeMaster has just returned from shopping. He scanned the check of the items he bought and gave the resulting string to Ratiorg to figure out the total number of purchased items. Since Ratiorg is a bot he is definitely going to automate it, so he needs a program that sums up all the numbers which appear in the given input.

Help Ratiorg by writing a function that returns the sum of numbers that appear in the given inputString.

Example

For inputString = "2 apples, 12 oranges", the output should be
sumUpNumbers(inputString) = 14.
"""

def check_num(e):
  try:
    return int(e)
  except ValueError:
    return 0


def sumUpNumbers(inputString):
  arr = []
  for e in re.findall(r"[^\W\d_]+|\d+",inputString):
    arr.append(check_num(e))
  return sum(arr)

