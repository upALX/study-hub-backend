# #Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

def get_second_grade(list_grade):
    list_sorted = sorted(list_grade, key=lambda x:x[1])
    second_minor_grade_student = list_sorted[1][1]
    print('Arr sorted in function', list_sorted)
    print('Num arr', list_sorted.__len__())
    print('Value sorted', )


    if list_sorted.__len__() == 2:
        if list_sorted[0][1] == list_sorted[1][1]:
            return ['SAME']
    elif second_minor_grade_student == list_sorted[0][1]:
        real_second_value_list = [x for x in list_sorted if x[1] != second_minor_grade_student]

        print(real_second_value_list)

        print('REAL LIST', real_second_value_list)
        
        second_grade_list = [x for x in real_second_value_list if x[1] == real_second_value_list[0][1]]

        print('SECOND', second_grade_list)

        return second_grade_list
    else:
        list_grade = [x for x in list_sorted if x[1] == list_sorted[0][1]]

        return list_grade

            # if second_minor_grade_student == item[1]:
            #     list_grade_students_name.append(item[0])

list_students = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    dict_student_information = [name, score]
    list_students.append(dict_student_information)

student_names_list = get_second_grade(list_students)

print('Only names', student_names_list)
    
if student_names_list.__len__() == 1:
    print('All students with same grade')
else:
    for item in sorted(student_names_list): 
        print(item[0])

# list_grade = [['harry', 37.21], ['barry', 37.21], ["Tina", 37.2], ["Akrt", 41]]

# sorted_list = sorted(list_grade, key=lambda x:x[1])

# print(sorted_list[])

# list_names = ["alx", 10, "luana", 3, "fulano", 2]