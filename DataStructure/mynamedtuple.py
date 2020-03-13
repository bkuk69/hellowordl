from collections import namedtuple
Tri  = namedtuple("Tiangle", ["bottom","height"])

t = Tri(3,7)
print(t[0], t[1])

print(t.bottom, t.height)


def show(n1, n2):
    print(n1, n2)

t = Tri(3,8)
show(*t)
