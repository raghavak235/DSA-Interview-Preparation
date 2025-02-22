def binary_iterative():
    arr = [10,20,30,40,50]
    val=51
    start = 0
    end = len(arr)-1
    
    while start <= end:
        mid =(start + end)//2
        if arr[mid]==val:
            return mid
        elif arr[mid] > val:
            end = mid -1
        else:
            start = mid+1
        
            
    return -1
# print(binary_iterative())

TC: O(logn)
SC: O(1)

def binary_recursion(arr, val, start, end):
    if start > end:
        return -1
    
    mid =(start + end)//2
    if arr[mid]==val:
            return mid
    if arr[mid] > val:
        end = mid -1
        return binary_recursion(arr, val, start, end)
    else:
        start = mid +1
        return binary_recursion(arr, val, start, end)
TC: O(logn)
SC: O(logn)    
        
        
