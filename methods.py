fs ='{0}...{1}...{2}'
ms = fs.format("Robot", 125, "Box")
print(ms)
ms = '{0}....{1}....{2}'.format("Jane", 52, "All")
print(ms)

my =["Box", (24, 31)]
print("{0[1]}...{0[2]}...{1[1]}".format(*my))

d ={"toy":"Robot","price": 3000}
print("toy = {0[toy]}, price ={0[price]}".format(d))
print('{0}'.format(3.14))
print("{0:f}".format(3.14))

print('{0:*^10.4f}'.format(31.4))
print("{0:+<10}".format(7))
print("{0:^^10}".format("hi"))