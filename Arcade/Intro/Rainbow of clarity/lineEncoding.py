"""
Given a string, return its encoding defined as follows:

First, the string is divided into the least possible number of disjoint substrings consisting of identical characters
for example, "aabbbc" is divided into ["aa", "bbb", "c"]
Next, each substring with length greater than one is replaced with a concatenation of its length and the repeating character
for example, substring "bbb" is replaced by "3b"
Finally, all the new strings are concatenated together in the same order and a new string is returned.
Example

For s = "aabbbc", the output should be
lineEncoding(s) = "2a3bc".

"""

def lineEncoding(s):
    st = []
    count = 0
    temp = s[0]
    for i,j in enumerate(s):
        
        if temp == j:
            count += 1
        if temp != j :
            if(count==1):
                pass
            else:
                st.extend(str(count))
            st.extend(temp)
            temp = j
            count = 1
    if(count==1):
        pass
    else:
        st.extend(str(count))
    st.extend(temp)
    
    return ''.join(st)
              
        

