def all_variants(text):
    for t in range(len(text)):
        for g in range(len(text) - t):
            yield text[t:g + t + 1]

a = all_variants("abc")
for i in a:
    print(i)


