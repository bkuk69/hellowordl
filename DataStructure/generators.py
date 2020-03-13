def gen_for():
    for i in [1,2,3]:
        yield i

def gen_for2():
    yield from [1,2,3]

g = gen_for()
g2 = gen_for()
for id2 in g2:
    print(id2, end=" ")
print()   
for id in g:
    print(id, end=" ")
print()

def gen_mygen():
    print("Hello World")
    yield 1
    
    print("Hello World")
    yield 2

    
    print("Hello World")
    yield 3

    
my_gen = gen_mygen()
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
