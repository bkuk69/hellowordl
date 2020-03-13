def who(a, b, c):
    print(a, b, c, end=" ")

who(*[1,2,3])
print()
who(*(0.1,0.2, 0.3))
print()
who(*("abc"))
print()

d = dict(a=1, b=2, c=3)
who(*d)
print()
who(**d)
print()
who(*(d.items()))
print()
def func(*args):
    print(args)
func()
func(1)
func(1,2)
func(1,2,3)
def func2(**args):
    print(args)
func2(a=1, b=2, c=3)
def func3(*arg1, ** arg2):
    print(arg1)
    print(arg2)

func3()
func3(1,a=1)
func3(1,2,a=1, b=2)