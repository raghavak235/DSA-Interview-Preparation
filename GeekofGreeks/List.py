def getMax(l):
    if not l:
        return None
    else:

        res = l[0]                  # assume l[0] is the max
        for i in range(1, len(l)):  # iterate through index 1 to last
            if l[i] > res:           # check whether current element is greater than res
                res = l[i]          # if current element is greater than res ,update res to current
        return res
TC: O(n)
SC: O(1)





def getSecMax(l):
    if len(l) <= 1:
        return None
    lar = l[0]; slar = None

    for x in l[1:]:
        if x > lar:         # if current element is greater than lar(largest element)
            slar = lar          # update slar to largest
            lar = x         # update lar to current element(largest)

        elif x != lar:      # if x is less then largest and not equal to lar(largest element)
            if slar == None or slar < x:    # if x is greater then second largest
                slar = x                    # assign current element is second largest
    return slar

TC: O(n)
SC: O(1)



def verifysort(l):
    sort = None
    for i in range(len(l)-1):
        if l[i] <= l[i+1]:
            sort = True
        else:
            sort = False
    return sort

TC: O(n)
SC: O(1)
    
    
# print(verifysort(l=[50,10,1]))


def verifysort_while(l):
    i = 1
    while i < len(l):
        if l[i] < l[i-1]:
            return False
        i +=1
        return True

print(verifysort_while(l=[10,20,20,30]))            
TC: O(n)
SC: O(1)


def leftrot(l, k):
    k = k % len(l)  # Normalize k
    return l[k:] + l[:k]
TC: O(n)
SC: O(1)

    

# Example usage:
print(leftrot(l=[10, 20, 30, 40], k=2))  # Output: [30, 40, 10, 20]


def leftrot(l,k):
    initialv=l[0]
    for i in range(1,len(l)):
        l[i-1] =l [i]
        
    l[-1] = initialv
    return l
    TC: O(n)
SC: O(1)


Q:https://www.geeksforgeeks.org/batch/ds-with-python/track/list-basic-python/problem/find-immediate-smaller-than-x
class Solution:
    def immediateSmaller(self, arr, n, x):
        closest_smaller = float('inf')  # Initialize with a large value
        
        for num in arr:
            if num < x:
                closest_smaller = min(closest_smaller, x - num)  # Store the minimum difference
        
        return x - closest_smaller if closest_smaller != float('inf') else -1  # Convert back to the closest number

TC: O(n)
SC: O(1)

Q: https://www.geeksforgeeks.org/batch/ds-with-python/track/list-basic-python/problem/find-immediate-greater-than-x

class Solution:
    # inf has been imported in driver code
    def immediateGreater(self,arr,n,x):
        #return required ans
        output = float('inf')
        for i in arr:
            if i > x:
                output = min(output, i-x)
                # print(i-x,output)
                
        return output+x if output != float('inf') else -1
        #code here

TC: O(n)
SC: O(1)


Q: https://leetcode.com/problems/rotate-array/description/

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Rotate an array by `k` elements in a counter-clockwise direction.
        The rotation is done in-place using the reversal algorithm.

        :param nums: List[int] - The input array to be rotated.
        :param k: int - Number of elements to rotate.
        :return: None - The function modifies `nums` in place.
        """

        # Step 1: Compute the effective rotation count
        # If k is greater than the array length, take modulo to avoid redundant rotations.
        arr = nums  # Using reference to nums to modify in-place
        d = k % len(arr)

        # Step 2: Reverse the entire array
        # This reverses all elements, making the last `d` elements come to the front
        l, r = 0, len(arr) - 1
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l, r = l + 1, r - 1

        # Step 3: Reverse the first `d` elements
        # This step ensures that the rotated section is in the correct order
        l, r = 0, d - 1
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l, r = l + 1, r - 1

        # Step 4: Reverse the remaining `n - d` elements
        # This step restores the order of the remaining elements
        l, r = d, len(arr) - 1
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l, r = l + 1, r - 1

        # The function modifies `nums` in place and does not return anything
TC: O(n)
SC: O(1)
