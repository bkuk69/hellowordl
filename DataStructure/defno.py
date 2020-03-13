s ="robbot"
d ={}

for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] =1

print(d)

s ="robbot"
d ={}

for i in s:
    d[i] = d.setdefault(i,0) + 1

print(d)