# my_set = {1, 2, 3}
# my_set = set()
# my_set = set([4, 5, 6])
#
# print(my_set)

#
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
#
# union_result_method = set1.union(set2)
# print("Union:", union_result_method)
#
# union = set1 | set2
# print("Union method:", union)
#
# intersection = set1 & set2
# print("Intersection method:", intersection)
#
# difference = set1 - set2
# print("difference method:", difference)
#
# symmestrical = set1 ^ set2
# print("symmestrical method:", symmestrical)
#
# #set methods

# my_set = {1, 2, 3}

# my_set.add(4)
# my_set.remove(3)
# my_set.discard(1)
# my_set.clear()
#
# print (my_set)

# set_length = len(my_set)
# print("Length of set:", set_length)


# Using sets - removing duplicates

# my_list = [1, 2, 2, 3, 3, 4, 4, 5]
#
# unique_set = set(my_list)
#
# unique_list = list (unique_set)
#
# print(unique_list)

# In and NOT IN

# loyalty_members = {"Alice", "Bob", "Charlie"}
#
# customer = "Bob"
#
# is_member = customer not in loyalty_members
#
# print(is_member)


# age = 18
#
# if age >=18:
#     print("You can vote")
# else:
#     print("ypu cannot vote")



# temp = 28
#
# if temp > 30:
#     print("its a hot day")
# elif 20 <= temp <= 30:
#     print("its a good day")
# else:
#     print("its a cold day")


student_gpa = 4.5
student_score = 75

if student_gpa >= 3.5:
    if 50 <= student_score <=65:
        print(f"Students with GPA{student_gpa} and test score of {student_score} may be eligible for a partial scholarship")
    elif student_score > 65:
         print(f"Students with GPA {student_gpa} and test score of {student_score} is not eligible for a full schoolarship")
    else:
        print(f"Students with GPA {student_gpa} and test score of {student_score} is not eligible for schoolarship")
else:
    print(f"Students with GPA {student_gpa} and test score of {student_score} is not eligible for schoolarship")












