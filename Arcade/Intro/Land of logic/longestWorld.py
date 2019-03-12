"""
Define a word as a sequence of consecutive English letters. Find the longest word from the given string.

Example

For text = "Ready, steady, go!", the output should be
longestWord(text) = "steady".
"""
def check(literal):
    if ord(literal) in range(ord('a'), ord('z')+1) or ord(literal) in range(ord('A'), ord('Z')+1):
           return True 
    return False
    
def longestWord(text):
    text_split = []
    temp = []
    for i,j in enumerate(text):
        if check(j):
            if (i==0):
                temp.append(j)
            else:
                temp.append(j)
        elif(i<len(text)-1 and temp):
            text_split.append(''.join(temp))
            temp = []
        elif(i<len(text)-1 and not temp):
            pass
        else:
            text_split.append(''.join(temp))
    text_split.append(''.join(temp))

    len_list = ([len(x) for x in text_split])
    max_len_pos = len_list.index(max(len_list))
    return text_split[max_len_pos]
        
    

