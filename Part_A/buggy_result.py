# MIVA Level 300 Result Calculator (BUGGY VERSION)

def calculate_average(scores):
    total = 0
    
    for i in range(len(scores)):
        total = total + scores[i]
    
    average = total / len(scores)
    return average


def get_grade(avg):
    if avg >= 70:
        grade = "A"
    elif avg >= 60:
        grade = "B"
    elif avg >= 50:
        grade = "C"
    elif avg >= 45:
        grade = "D"
    else:
        grade = "F"
    
    return grade


# Student Data (MIVA Level 300)
student_name = "John - MIVA Level 300"
scores = [70, 65, "80", 90]   # BUG 1: string inside list

average = calculate_average(scores)

if average > 50
    print(student_name + " passed")   # BUG 2: missing colon

grade = get_grade(average)

print("Average:", average)
print("Grade:", grade)

print("Extra:", extra)   # BUG 3: undefined variable