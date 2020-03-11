tri_one =(12,15)
print(tri_one)

tri_two = 23, 25
print(tri_two)

three, four = tri_two
print(three)
print(four)

nums =(1,2,3,4,5)
one, two, * others = nums
print(one)
print(two)
print(others)

first, * anothors, last = nums
print(first)
print(anothors)
print(last)

t = (1,2,(3,4))
a,b,(c, d) = t
print(a,b,c,d,end=" ")

p ="Hong", (32, 178), "010-1234-5678", "korea"
na,(_,he), _,_ = p
print(na, he, end=" ")

ps = [("Lee", 172), ("Jung", 182), ("Yoon", 179)]

for n, h in ps:
    print(n, h, sep=",")
