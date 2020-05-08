def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # a = []
    # for file in files:
    #     # print(file.split("/"))
    #     for query in queries:
    #         if query in file:
    #             a.append(file)
    # return a

    a = []
    hm = {}
    for file in files:
        filed = file.split("/")
        length = len(filed) - 1
        filed = filed[length]
        if filed not in hm:
            hm[filed] = [file]
        else:
            hm[filed].append(file)

    for query in queries:
        if query in hm:
            if len(hm[query]) > 1:
                for file in hm[query]:
                    a.append(file)
            else:
                a.append(hm[query][0])
    return a


if __name__ == "__main__":
    # files = [
    #     '/bin/foo',
    #     '/bin/bar',
    #     '/usr/bin/baz'
    # ]
    files = [
        "/usr/local/share/foo.txt",
        "/usr/bin/ls",
        "/home/davidlightman/foo.txt",
        "/bin/su"
    ]
    queries = [
        "ls",
        "foo.txt",
        "nosuchfile.txt"
    ]
    # queries = [
    #     "foo",
    #     "qux",
    #     "baz"
    # ]
    print(finder(files, queries))
