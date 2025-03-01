def alternatingCharacters(s):
    count = 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            count += 1
    return count

# q = int(input().strip())

# for q_itr in range(q):
#     s = input()

#     print(alternatingCharacters(s))

# 5
# AAAA
# BBBBB
# ABABABAB
# BABABA
# AAABBB