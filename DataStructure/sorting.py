ns =[("Yoon",33),("Lee",12),("Park",29)]
def age(t):
    return t[1]
ns.sort(key=age)
print(ns)
ns =[("Yoon",13),("Lee",12),("Park",29)]
def name(t):
    return t[0]
ns.sort(key=name)
print(ns)
ns =[("Yoon",13),("Lee",12),("Park",29)]
ns.sort(key= lambda t : t[1])
print(ns)

ns =[("Yoon",13),("Lees",12),("Park",29)]
ns.sort(key= lambda t: t[0])
print(ns)


ns =["steve","park","seventeen"]
ns.sort(key = len)
print(ns)

nums = [(3,1),(2,9),(0,5)]
nums.sort(key = lambda  x: x[0] + x[1], reverse= True )
print(nums)

org =  [("Yoon",13),("Lee",12),("Park",29)]
cpy = sorted(org, key= lambda t: t[0])
print(org)
print(cpy)

org = (3,1,2)
cpy = tuple(sorted(org))
print(cpy)
org = ("321","214","397")
cpy = tuple(sorted(org, key = lambda s : int(s[0])))
print(cpy)