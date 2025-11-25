# age = 25
# print(type(age))
# age_as_str=str(age)
# print(age_as_str,"of type",type(age_as_str))
from stringprep import b1_set

from numpy.ma.core import divide
from pandas.core.interchange.from_dataframe import primitive_column_to_ndarray

from module6.main2 import result

# x=5
# y=4,3
#
# result=x+y
# print(type(result))
#
# age=25
# message="I am" + str(age) + "years old"
# print(message)
#
# a=5
# b="3"
# print(type(b))
# b1=int(b)
# result2=a+int(b)
# print(type(b))
# print(result)

# name=input("Enter your name:")
# print(f"Hello,{name}")
#
# age=input("Enter your age:")
# print(type(age))
#
# num1=int(input("Enter the first number:"))
# num2=int(input("Enter the second number:"))
# result=num1+num2
# print(result)
#



# try:
#     result=10/2
#     print(result)
# except ZeroDivisionError:
#     print("Opps! Tried to divide to zero")
#
# fruits={
#     "apple":5,
#     "orange":7
# }
#
# try:
#     print(fruits["orange"])
# except KeyError:
#     print("The key does not exist")
#
#

try:
    result=10/0
    print(result)
except ZeroDivisionError:
    print("Opps! Tried to divide to zero")
finally:
    print("Finally block executed")

def divide_num(a,b):
    try:
        result=a/b
        print(result)
    except ZeroDivisionError:
        print("Invalid division by zero")
    except TypeError:
        print("Invalid type for division")
    except Exception as e:
        print({e})


divide_num(10,2)
divide_num(10,0)
divide_num(10,'2')


