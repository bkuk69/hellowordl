def times2():
    for i in range(1,10):
        yield 2* i



def show_all(s):
    for i in s:
        print(i, end=" ")


g = times2()
show_all(g)
print()

g = (x*2 for x in range(1,10))
show_all(g)
print()
show_all(x**2 for x in range(2,11))
