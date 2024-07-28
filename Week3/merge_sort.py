
#Time Complexity: O(nlogn)

#Space Complexity: O(n), o(logn2),n=8, logn2=8, n=4(approximately)
# Extra Space - outplace sorting algorithm.


# Explain space complexity


def mergeProcedure(arr, start, mid, end):
    # Create and Initialize the left and right subarray
    l=arr[start:mid+1]
    r=arr[mid+1:end+1]
    m = n =0
    k = start

    while m < len(l) and n <len(r):
        if l[m]<r[n]:
            arr[k]=l[m]
            m +=1
        else:
            arr[k]=r[n]
            n +=1
        k += 1
    # pending elements in left subarray
    while m < len(l):
        arr[k] = l[m]
        m +=1
        k += 1

    # pending elements in right subarray
    while n < len(r):
        arr[k] = r[n]
        n += 1
        k += 1



def merge_sort(arr, start, end):
    if start < end:

        # Divide
        mid = start +(end-start)//2
        # Conquer
        # Recursive call for left subtree
        merge_sort(arr, start, mid)
        # Recursive call for right subtree
        merge_sort(arr, mid+1, end)
        # Combine
        # Combine the results of both left and right subtree
        mergeProcedure(arr,start,mid,end)


arr=[30,20,50,2]

merge_sort(arr,0, len(arr)-1)
for i in arr:print(i)