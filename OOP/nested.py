def maker(m):
    def inner(n):
        return m * n
    return inner
f1 = maker(2)
f2 = maker(3)

print(f1(4))
print(f2(5))