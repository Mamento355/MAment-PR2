def dif(J, S):
    x = set(J)
    count = 0
    for y in S:
        if y in x:
            count += 1
    return count
J = "ab"
S = "aabbccd"
result = dif(J, S)
print(result)