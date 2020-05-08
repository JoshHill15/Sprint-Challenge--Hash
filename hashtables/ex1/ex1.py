
def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    O(n)
    """
    hm = {}
    a = length - 1
    for i in range(length//2):
        if weights[a] + weights[i] == limit:
            print(a, weights[a], i, weights[i])
            hm[weights[i] + weights[a]] = (a, i)
        a -= 1
    if limit in hm:
        return hm[limit]
    else:
        return None


# print(get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21))  # [3,1]
print(get_indices_of_item_weights([9], 1, 9))  # None
