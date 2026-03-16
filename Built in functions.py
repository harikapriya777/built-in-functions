#Builtin functions
#1.fromkeys()

'''a="codegnan"
print(a)

print(list(a))
print(tuple(a))
print(set(a))

#print(dict(a))

b=dict.fromkeys(a)
print(b)

b=dict.fromkeys(a,"harika")
print(b)'''


#2.evaluate- eval()

'''while True:
    a=int(input("a value"))
    b=int(input("b value"))
    print(a+b)'''
    

'''while True:
    a=float(input("a value"))
    b=float(input("b value"))
    print(a+b)'''

'''while True:
    a=input("a value")
    b=input("b value")
    print(a+b)'''

'''while True:
    a=eval(input("a value"))
    b=eval(input("b value"))
    print(a+b)
    print(type(a))'''


#3.zip()- we can combine multiple collections into one collection
'''a=[10,20,30,40,50,60]
names=["harika","taruni","simhadri","adithya","bhavani"]
print(a+names)

b=zip(a,names)
print(b)#here the output gives packed elements to unpack we should use data types

c=list(zip(a,names))
print(c)

d=set(zip(a,names))
print(d)

e=tuple(zip(a,names))
print(e)

f=dict(zip(a,names))
print(f)'''

#4.enumerate()- we can give counter to the collection
'''names=["harika","taruni","simhadri","adithya"]
for i in range(len(names)):
    print(i,names[i])

b=dict(enumerate(names))
print(b)

b=list(enumerate(names,100))
print(b)'''


'''names=[10.05,20,30,40,50]
for i in range(len(names)):
    print(i,names[i])

b=dict(enumerate(names,100))
print(b)

b=list(enumerate(names,100))
print(b)'''


#5.ASCII
#chr()
print(chr(20))

