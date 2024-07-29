#Time Complexity: 2T(n/2) +c: O(n)
#Space Complexity: O(logn) Since the function is called recursively, the maximum depth of the recursion stack is O(logn)



def min_max_condition(max1,min1, max2, min2):
    max_val = min_val =0
    if max1>max2:
        max_val= max1
    else:
        max_val=max2
    if min1< min2:
        min_val = min1
    else:
        min_val=min2

    return max_val, min_val



def min_max(arr, start, end):
    # In the base case where there is only one element, there is no need to compare it with anything

    if start == end:
        return arr[start], arr[start]
    mid= start + (end-start)//2
    max1,min1 = min_max(arr, start, mid)
    max2,min2 = min_max(arr, mid+1, end)
    max_val, min_val = min_max_condition(max1,min1, max2,min2)
    return max_val, min_val


arr=[30,20,50,2,25]


max_val, min_val= min_max(arr,0, len(arr)-1)
print(max_val, min_val)