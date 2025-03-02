def gridChallenge(grid):
    if not grid:
        return 'NO'
    k = len(grid[0])
    for i in range(len(grid)):
        if len(grid[i]) != k:
            return 'NO'
        grid[i] = sorted(grid[i])
    for i in range(len(grid[0])):
        for j in range(1, len(grid)):
            if grid[j][i] < grid[j - 1][i]:
                return 'NO'
    return 'YES'

# print(gridChallenge(['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv'])) # YES
# print(gridChallenge(['kc', 'iu'])) # YES
# print(gridChallenge(['uxf', 'vof', 'hmp'])) # NO
# print(gridChallenge(['abc', 'def', 'ghi'])) # YES
# print(gridChallenge(['mpxz', 'abcd', 'wlmn'])) # NO
print(gridChallenge(["zxc","aaa"])) # NO"
#c 