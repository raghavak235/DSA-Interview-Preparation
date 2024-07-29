
#Time Complexity: T(n)= T(mid-p)+T9q-mid)+n= T(nlogn)

#Space Complexity: O(n), o(logn2),n=8, logn2=8, n=4(approximately)


def partition(arr, p,q):
    pivot = arr[p]
    i=p
    for j in range(i+1, q+1):
        if arr[j] < pivot:
            i +=1
            # swap between arr[i] and arr[j]
            arr[i], arr[j]=arr[j], arr[i]

    # final swap between arr[i] and pivot
    arr[i], arr[p] = arr[p], arr[i]
    return i

def quick_sort(arr, p, q):
    if p<q:
        #Divide
        mid = partition(arr, p, q)
        #Recursively call the left subtree
        quick_sort(arr, p, mid-1)
        # Recursively call the right subtree
        quick_sort(arr,mid+1,q)
    return arr


arr = [30, 20, 50, 2]

quick_sort(arr, 0, len(arr) - 1)
for i in arr: print(i)