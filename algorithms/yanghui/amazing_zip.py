def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    l1 = [1]
    l2 = []
    for n in range(0, numRows):
        l2.append(l1)
        l1 = [sum(t) for t in zip([0] + l1, l1 + [0])]
    return l2


print(generate(11))