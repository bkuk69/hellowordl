A ={"a","b",'c',"d"}
B ={"a","d","f","e"}

print(A-B)
print(A & B)
print(A | B)
print(A -B)
print (A ^ B)

os ={1,2,3,4,5}
os.add(6)
os.discard(1)
print(os)
os.update({7,8,9})
print(os)
os &={2,4,6,8}
print(os)
os -={2,4}
print(os)
os ^={1,3,6}
print(os)