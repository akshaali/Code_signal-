"""""
Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees. People can be very tall!

Example

For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].
""""

def sortByHeight(a):
    people , people_loc , count , l  = [] , [] , 0 , len(a)
    for i in range(l):
        if a[i] != -1 :
            people.append(a[i])
            people_loc.append(i)
    people_sorted = sorted(people)
    for j in people_loc:
            a[j] = people_sorted[count]
            count += 1
    return a
        
