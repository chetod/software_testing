def caesarCipher(s, k):
    for i in range(len(s)):
        if s[i].isalpha():
            if s[i].islower():
                s = s[:i] + chr((ord(s[i]) - ord('a') + k) % 26 + ord('a')) + s[i+1:]
            else:
                s = s[:i] + chr((ord(s[i]) - ord('A') + k) % 26 + ord('A')) + s[i+1:]
    return s

# print(caesarCipher('middle-Outz', 2)) # okffng-Qwvb
