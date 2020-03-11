def fuct_fac(n):
    def exp(x):
        return x ** n
    return exp


f2 = fuct_fac(2)
f3 = fuct_fac(3)

print(f2(4))
print(f3(4))

ref = lambda s: print(s)
ref("oh")

f1 = lambda n1, n2 : n1 +n2
print(f1(3,4))