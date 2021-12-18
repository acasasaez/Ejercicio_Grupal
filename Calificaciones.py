import math
import os
import random
import re
import sys

def gradingStudents(grades):
    list[73, 77, 38, 33]
    for grades in (grades):
        list.append(FinalGrade(grades))
        return list
def FinalGrade(grades):
    roundgrade = 0
    if(grades < 40):
        roundgrade=grades     
    else:
        cociente=int(grades/5 +1)
        multiplo = cociente*5
        if(multiplo-grades<3):
            roundgrade=multiplo
        else:
            roundgrade=grades
    return roundgrade    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'] + "Calificaciones", 'w')
    print("Número de estudiantes")
    grades_count = int(input().strip())
    grades = []

    for _ in range(grades_count):
        print("Nota de cada estudiante")
    grades_item = int(input().strip())
    grades.append(grades_item)
    result = gradingStudents(grades)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
