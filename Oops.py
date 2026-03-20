#OOPs- Object oriented programming structure.
#definition- A class contains attributes or variables and methods or functions that can manipulate the data
#A class is the blueprint of an object
#An object is an initiation of a class
#Methods or functions define inside the body of the class.

#oops syntax
'''class classname():
    name="codegnan"
    age=2018
    place="vja"
    def fname(method):
        print(statements........)
a=classname()
print(dir(a))
a.fname()'''

#class declaration
'''class details():
    name="harika"
    age=25
    place="eluru"
    def display(self):
        print(self.name,self.age,self.place)
a=details()
print(dir(a))
a.display()'''

#object instantiation

'''class Details():
    def Data (self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.Data("harika",25,"eluru")
a.display()
b=Details()
b.Data("taruni",21,"vja")
b.display()'''

#object initialization

'''class details():
    #creating a constructor
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=details("taruni",22,"vja")
a.display()'''

#task runtime

'''class details():
    def __init__(self):
        self.name=input("enter your name")
        self.age=int(input("enter your age"))
        self.place=input("enter your place")
    def display(self):
        print(self.name,self.age,self.place)
b=details()
b.display()'''


class details():
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=details(input("name"),int(input("age")),input("place"))
a.display()
        


