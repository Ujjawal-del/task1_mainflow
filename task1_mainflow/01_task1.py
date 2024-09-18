# STUDY PYTHON SYNTEX

#Variables
a = 15
name_student = "sanju"
is_student = True
marks = 51.22

#Data type
a1 = 32              
greet = "hello"
score = 41.1
is_valid = False
                            #OUTPUT
print(type(a1))             # <class 'int'> 
print(type(greet))          # <class 'str'>
print(type(score))          # <class 'float'>
print(type(is_valid))       # <class 'bool'>


#LOOPS
#for loop
for i in range(1, 10):
    print(i)

#while loop
i = 1
while(i<11):
    print(2*i)
    i += 1


#functions
def func1(name):
    print("Hello "+ name)

func1("rahul")

#function number 2
def avg():
    a1 = int(input("enter number 1 "))
    a2 = int(input("enter number 2 "))
    a3 = int(input("enter number 3 "))

    average = (a1+a2+a3)/3

    return average

avg1 = avg()
print(avg1)

