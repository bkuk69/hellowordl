
def deco(func):
    def df():
        print("Emoticon")
        func()
        print("Emoticon")
    return df

@deco
def smile():
    print("^_^")
@deco
def confused():
    print("@_@")
smile()

confused()



def adder_deco(func):
    def ad(*args):
        print(*args, sep=" + ", end=" ")
        print("= {0}".format(func(*args)))
    return ad
@adder_deco    
def adder2(n1, n2):
    return n1 + n2

@adder_deco
def adder3(n1, n2, n3):
    return n1 + n2 + n3

adder2(3,4)
adder3(3,4,5) 

def deco1(func):
    def inner():
        print("deco1")
        func()
    return inner
def deco2(func):
    def inner():
        print("deco2")
        func()
    return inner

@deco2
@deco1
def smile2():
    print("Smile")

smile2()

