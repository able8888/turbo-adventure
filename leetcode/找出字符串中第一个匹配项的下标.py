haystack = "sadbutsad"
needle = "sad"
i = 0
while i + len(needle) <= len(haystack) - 1:
    if haystack[i: i + len(needle)] == needle:
        print(i)
        break
    else:
        i += 1
print(-1)