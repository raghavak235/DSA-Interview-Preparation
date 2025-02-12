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
