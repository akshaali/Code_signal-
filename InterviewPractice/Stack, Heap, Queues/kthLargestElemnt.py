"""
Note: Avoid using built-in std::nth_element (or analogous built-in functions in languages other than C++) when solving this challenge. Implement them yourself, since this is what you would be asked to do during a real interview.

Find the kth largest element in an unsorted array. This will be the kth largest element in sorted order, not the kth distinct element.

Example

For nums = [7, 6, 5, 4, 3, 2, 1] and k = 2, the output should be
kthLargestElement(nums, k) = 6;
For nums = [99, 99] and k = 1, the output should be
kthLargestElement(nums, k) = 99.

"""
from random import choice

def kthLargestElement(nums, k):
    if len(nums) == 1:
        return nums[0]
    else:
        p = choice(nums)
        a, b = [], []
        c = 0
        for n in nums:
            if n > p:
                a.append(n)
            elif n == p:
                c += 1
            else:
                b.append(n)
        if len(a) >= k:
            return kthLargestElement(a, k)
        elif len(a)+c >= k:
            return p
        else:
            return kthLargestElement(b, k-len(a)-c)
    
