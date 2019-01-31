if 1==1:
    print("True")
elif 1==2:
    print("False")
else:
    print("How'd I get here")

ar = [1,2,3]
ar.append(4)
ar.append("5")
ar += [6]
ar[0]=4
x = range(len(ar))
print(ar)
# print(x)
# for item in ar:
#     print(item)
# print(ar)
# for i in range(len(ar)):
#     print(i)
#     print(ar[i])

di = { "key":"value", "key2":2}
di["key3"]=4.1
di["key"]=4.1
# print(di["key"])

tu = ({"key":1},2,3)
# tu[0]=2
tu[0]["key"]=4
# print(tu[0]["key"])
# for i in tu:
#     print(i)

def functions(x, y=5):
    print(x+y)

functions(1,3)

class Person:
    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name

    def print_name(self):
        try:
            print(self.f_name + " " + self.l_name)
        except:
            print("User is an error")

    def __str__(self):
        return str(self.f_name) + " " + str(self.l_name)


# import math as m
from math import ceil

class Student(Person):

    def __init__(self, f_name, l_name, gpa):
        Person.__init__(self,f_name,l_name)
        self.gpa = gpa
    def print_name(self):
        try:

            print(str(ceil(self.gpa)) + " "+ self.f_name + " " + self.l_name)
        except Exception as e:
            print("User is an error" + str(e))

ryan = Student("Ryan", "Saitta", 3.8)
er = Person(5, 6)
er.print_name()
ryan.print_name()
print(ryan)

string_x = "This is a string : here's another"
print(string_x.split())
for item in string_x.split(":"):
    item = item.lstrip()
    print(item[0:3].lstrip())







# dsd
