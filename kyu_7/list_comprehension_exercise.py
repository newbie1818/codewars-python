
'''You have a list of prices in a store.
 Write a function that returns only the items whose price does not exceed your budget.
 The function takes two parameters — a list of prices and a budget'''
def affordable(price, budget):

    return [i for i in price if i <= budget]

print(affordable([5, 120, 30, 8, 250, 15], 30))