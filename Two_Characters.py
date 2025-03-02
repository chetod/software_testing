def alternate(s):
    s = list(s)
    chars = list(set(s))
    max_len = 0
    for i in range(len(chars)):
        for j in range(i+1, len(chars)):
            c1 = chars[i]
            c2 = chars[j]
            last = None
            valid = True
            for c in s:
                if c == c1:
                    if last == c1:
                        valid = False
                        break
                    last = c1
                elif c == c2:
                    if last == c2:
                        valid = False
                        break
                    last = c2
            if valid:
                max_len = max(max_len, s.count(c1) + s.count(c2))
    return max_len

# print(alternate('beabeefeab')) # 5
# print(alternate('asdcbsdcagfsdbgdfanfghbsfdab')) # 8
# print(alternate('asvkugfiugsalddlasguifgukvsa')) # 0
