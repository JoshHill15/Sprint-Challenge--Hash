def intersection(arrays):
    """
    YOUR CODE HERE
    """
    hm = {}
    arrs = []
    length = 0
    for arr in arrays:
        length += 1
        for numbers in arr:
            if numbers not in hm:
                hm[numbers] = 1
            else:
                hm[numbers] += 1
    for key in hm:
        if hm[key] == length:
            arrs.append(key)
    return arrs


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    # arrays = [
    #     [1, 2, 3, 4, 5],
    #     [12, 7, 2, 9, 1],
    #     [99, 2, 7, 1, ]
    # ]

    print(intersection(arrays))
