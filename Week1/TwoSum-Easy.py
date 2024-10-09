# https://leetcode.com/problems/two-sum/

a = [-2, 1, 2, 4, 7, 11]
target = 13
def sum_two_nums_brute_force(a, target):
   # Time Complexity: o(n2)
   # Space Complexity: O(1)

   for i in range(len(a)-1):
       for j in range(i+1, len(a)):
           if a[i]+a[j]==target:
                print(i,j)
                return True

   return False


def twosum_hashmap_dict(a, target):
    # Time Complexity: o(n)
    # Space Complexity: O(n)
    keys = dict()
    for i, num in enumerate(a):
        complement = target - num
        if complement in keys:
            print(keys[complement], i)
            return [keys[complement], i]

        else:
            keys[num] = i

def twosum_two_pointer(a, target):
    # Time Complexity: o(n)
    # Space Complexity: O(1)
    start=0
    end= len(a)-1
    while start <end:
        if a[start]+a[end]==target:
            print(start, end)
            return True
        elif a[start]+a[end]<target:
            start +=1
        else:
            end -=1
