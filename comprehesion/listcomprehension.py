r1 = [1,2,3,4,5]

r2 = [] 

for i in r1:
    r2.append(r1 *2)



r3 = [x * 2 for x in r1]

r4 = []
for i in r1:
    if i %2 :
        r4.append(i *2)

r4 =[x * 2 for x in r1 if x % 2]
print(r4)

f1 = ["Black","White"]
f2 = ["Red", "Blue","Green"]

f3 = [x + y for x in f1 for y in f2]
print(f3)

r = [m * n for m in range(2,10) for n in range(1,10)]
print(r)

r = [m * n for m in range(2,10) for n in range(1,10) if (m * n)% 2==1]
print(r)
