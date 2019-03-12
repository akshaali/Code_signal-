"""
Check if the given string is a correct time representation of the 24-hour clock.

Example

For time = "13:58", the output should be
validTime(time) = true;
For time = "25:51", the output should be
validTime(time) = false;
For time = "02:76", the output should be
validTime(time) = false.
"""

def validTime(time):
    time = time.split(':')
    if len(time)!=2:
        return False
    for i in range(len(time)):
        if len(time[i]) !=2:
            return False
    if int(time[0]) in range(0,24) and int(time[1]) in range(0,60):
        return True
    return False
