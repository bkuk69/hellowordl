s = "My Friend %s is %d years old and %fcm tall" %("Jung", 22, 178.5)
print(s)
s = "%(name) s : %(age)d" % {"name":"Yoon","age":22}
print(s)