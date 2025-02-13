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

# Example usage:
print(leftrot(l=[10, 20, 30, 40], k=2))  # Output: [30, 40, 10, 20]


def leftrot(l,k):
    initialv=l[0]
    for i in range(1,len(l)):
        l[i-1] =l [i]
        
    l[-1] = initialv
    
    return l
