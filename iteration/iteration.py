ds =[1,2,3,4]
dis = iter(ds)
print(next(dis))
print(next(dis))
print(next(dis))
print(next(dis))
print(next(dis))

ds =[1,2,3]

ir = ds.__iter__()
ir.__next__()

td =("one","two","three")

ir = iter(td)

print(next(ir))