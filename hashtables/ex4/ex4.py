def has_negatives(a):
    """
    YOUR CODE HERE
    """
    hm = {}
    arr = []
    for i in range(len(a)):
        if a[i] not in hm and a[i] != 0:
            hm[a[i]] = False
        if (a[i] * -1) in hm:
            hm[a[i]] = True
    for key in hm:
        if hm[key]:
            if key < 0:
                key *= -1
            arr.append(key)
    return arr


if __name__ == "__main__":
    print(has_negatives([1, -1, 2, 3, -4, -3, 4, -5, 6, 7]))
