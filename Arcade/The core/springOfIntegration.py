"""
You are given an array of desired filenames in the order of their creation. Since two files cannot have equal names, the one which comes
later will have an addition to its name in a form of (k), where k is the smallest positive integer such that the obtained name is not
used yet.
Return an array of names that will be given to the files.
Example
For names = ["doc", "doc", "image", "doc(1)", "doc"], the output should be
  fileNaming(names) = ["doc", "doc(1)", "image", "doc(1)(1)", "doc(2)"].
 """
 
 def fileNaming(names):
    for i in range(len(names)):
            number = 1
            newName = names[i]
            while newName in names[:i]:
                newName = names[i] + '(' + str(number) + ')'
                number += 1
            names[i] = newName
    return names  
