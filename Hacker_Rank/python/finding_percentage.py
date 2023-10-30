# The provided code stub [toco, ponta, coto, cepo, raiz] will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks [marca, marco, alvo, símbolo, indicação, característica, rótulo, meta, limite, signo, cicatriz, sinal distintivo, mira, sinete, fronteira, sintomas, marcar, assinalar, notar, distinguir, anotar, caracterizar, selecionar, designar, acompanhar] array for the student name provided, showing 2 places after the decimal.

def calculate_average(list_students_marks) -> float:
    sum_student_marks_values = sum(list_students_marks)
    
    # return the average with len of array
    return sum_student_marks_values / list_students_marks.__len__()

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    
    query_name = input()
    
    # verify if exists on dict
    
    if query_name in student_marks:
        if student_marks[query_name].__len__() == 3:
            
            average_students_mark = calculate_average(student_marks[query_name])
            
            #get the array values of key AND # sum all values
        
            print(f"{average_students_mark:.2f}")
    else:
        print('The student was not found!')