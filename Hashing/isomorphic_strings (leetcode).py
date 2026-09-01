s = "ab"
t = "cc"
d1 = {}
d2 = {}
for i in range(len(s)):
    if s[i] in d1:
        if d1[s[i]] != t[i]:
            print("false")
    else:
        d1[s[i]] = t[i]
for j in range(len(t)):
    if t[j] in d2:
        if d2[t[j]] != s[j]:
            print("false")
    else:
        d2[t[j]] = s[j]

