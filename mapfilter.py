def pow(n):
    return n ** 2

st1 = [1,2,3]


st2 = [pow(st1[0]), pow(st1[1]), pow(st1[2])]

st2 = list(map(pow, st1))

def dbl(e):
    return e*2
print(list(map(dbl,(1,3,4))))

print(list(map(dbl, 'hello')))


def sum(n1, n2):
    return n1 + n2

st1 = [1,2,3]
st2 = [3,2,1]

st3 = list(map(sum, st1, st2))
print(st3)

def rev(s):
    return s[::-1]

st =["one","two","three"]

rst = list(map(rev, st))
print(rst)

rst = list(map(lambda  s: s[::-1], st))
print(rst)
