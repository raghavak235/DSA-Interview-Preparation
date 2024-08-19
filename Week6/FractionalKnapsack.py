
def fractionalKnapSack(profit, weights, M):
    pass
    fractions = [0] *len(profit)
    objects = list(range(len(profit)))

    # profit/weight ratio
    ratio = [profit/weights for profit, weights in zip(profit, weights)]

    #sort the ratio in the decreasing order
    objects.sort(key=lambda i: ratio[i], reverse=True)

    #take the objects sequentially, decreasing the net wright and increasing the profit
    n = len(profit)
    maxProfit = 0
    for i in objects:
        if weights[i]<= M:
            M -= weights[i]
            maxProfit += profit[i]
            fractions[i]=1
        else:
            maxProfit += profit[i] * (M/weights[i])
            fractions[i]=M/weights[i]
            break
    return maxProfit, fractions



weights = [5,10,12,4,7,9,3]
profit = [25, 75, 100,50,45,90,30]
M =37


maxmimumProfit, fractions = fractionalKnapSack(profit, weights, M)
print(maxmimumProfit, fractions)