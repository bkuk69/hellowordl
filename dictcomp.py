d1 =dict(a=1,b=2,c=3)

d2 = {k:v*2 for k, v in d1.items()}

d3 = {k:v*2 for k, v in d2.items()}

print(d1)
print(d2)
print(d3)

d1 =dict(a=1,b=2,c=3, d=4)
d2 = {k:v for k, v in d1.items() if v % 2 !=0}
print(d2)

ks =["a","b","c","d"]
vs =[1,2,3,4]

d = {k:v for k, v in zip(ks, vs)}
print(d)

d = {k:v for k, v in zip(ks, vs) if v %2}
print(d)