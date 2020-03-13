names =["김현주", "박선주","윤나은","이지선","장현지"]

dnames ={}
names.sort()
i=1
for name in names:
    dnames[i] = name
    i += 1
print(dnames)

names =["김현주", "박선주","윤나은","이지선","장현지"]
eo = enumerate(names)
for n in eo:
    print(n ,end=" ")
print()
names2 =["김현주", "박선주","윤나은","이지선","장현지"]
for n in enumerate(names2, 10):
    print(n, end=" ")
print()
names2 =["김현주", "박선주","윤나은","이지선","장현지"]
dnames2 = {k:v for k,v in enumerate(sorted(names2),1)}
print(dnames2)