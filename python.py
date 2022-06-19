#var,data type 
a = 10
b = 'str'
c = True
d = [1,2,3] #list-array
e = {'a':1 ,'b':2 ,'c':3} #dictionary
f = {1,2,3,4,3} #set
g = (1,2,3,4,3) #tuple
h = None

print(a,b,c,d,e,f,g,h)


#expression and operator
# Constant Expressions
x = 15
# Arithmetic Expressions
a = 5+6
# Relation Expressions
p = 5+6 <= 12
print(p)
#Logical Expressions
P = (10 == 9)
Q = (7 > 5)  
R = P and Q
print(R)
#Bitwise Expressions
a = 100
x = a >> 2
y = a << 1
print(x, y)


#if-else
a = int(input("a:"))
b = int(input("b:"))
if a<b:
    print("a<b")
elif a==b:
    print("a=b")
else:
    print("a>b")


#for loops
for i in range(2,5):
    print(i)

#while loops
num = 10
sum = 0
i = 1
while i <= num:
    sum = sum + i
    i = i + 1
print(f"Sum of first {num} number is: {sum}")



#break
#Break statement dùng trong loop để exit vòng lặp
for i in range(10):
    if i>5:
        print("break")
        break
    print(i)
print("continue statement")
#continue
#Continue statement để skip iteration hiện tại và tiếp tục next iteration
for i in range(10):
    if i%2 == 1:
        print(f"{i} is odd")
        continue
    else:
        print(f"{i} is even")



#function
def sosanh(a,b):
    if a<b:
        print("a<b")
    elif a==b:
        print("a=b")
    else:
        print("a>b")

sosanh(a=int(input("a:")),b=int(input("b:")))




#Regular Expression
import re

txt = "The rain in Hanoi"
x = re.findall("in", txt)
print(x)



#exception
try:
  print(x)
except NameError:
  print("Variable x is not defined")
finally:
  print("Something else went wrong")


#OOP
class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age
    
    def show_age(self):
        print (f"{self.name} is {self.age} years old")
    
#Kế thừa
class Student(Person):
    def __init__(self,name,age,school):
        Person.__init__(self,name,age)
        self.school = school
    def show_school(self):
        print (f"{self.name} study at {self.school}")
    
a = Student('a',1,'HUST')
a.show_age()
a.show_school()

#Bao đóng
class Dog:
    __name = "abc" #private

    def __getName(self):       #private
        print(self.__name)
    def _getN(self):           #protected
        print(self.__name)
    def get(self):             #public
        self.__getName()

#print(Dog().__name) #error
#Dog().__getName() #error
Dog().get()
Dog()._getN()

