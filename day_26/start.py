import random
import pandas
#List Comprehension
numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]
# print(new_list)

name = "Angela"
nuevo_list = [letter for letter in name]
# print(nuevo_list)

list_n = [n*2 for n in range(1,5)]
# print(list_n)

#Conditional List Comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [item for item in names if len(item) < 5]
upper_names = [name.upper() for name in names if len(name) > 5]
# print(upper_names)

#Dictionary Comprehension

# new_dict = {new_key: new_value for (key, value) in dict.items()}
students_scores = {student: random.randint(1, 100) for student in names}

passed_students = {student: score for (student, score) in students_scores.items() if score >= 60}
# print(passed_students)

student_dict = {
    "student ": ["Alex", "Beth", "Caroline"],
    "score": [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

#Loop through a dataframe(same as dictionary)
# for (key, value) in student_data_frame.items():
#     print(value)

#Pandas inbuilt loop
for(index, row) in student_data_frame.iterrows():
    print(row)