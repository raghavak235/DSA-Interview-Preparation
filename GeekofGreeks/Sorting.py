def optimized_bubble_sort(l):
    n = len(l)
    for i in range(n-1):
        swapping = False
        
        # After placing highest value at the end there is no need to take and compare the value. so thats why n-i-1
        for j in range(n-i-1):
            if l[j] > l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
                swapping = True
        if swapping == False:
            return l
            
TC : O(n2) for unsoted and O(n) for sorted
print(optimized_bubble_sort(l=[1,2,10,8,5]))
