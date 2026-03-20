# MIVA Level 300 Result Calculator (FIXED VERSION)

def calculate_average(scores):
    total = 0
    
    for score in scores:
        try:
            total += float(score)   
        except ValueError:
            print("Invalid score detected:", score)
            continue
    
    if len(scores) == 0:
        return 0
    
    return total / len(scores)


def get_grade(avg):
    if avg >= 70:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 50:
        return "C"
    elif avg >= 45:
        return "D"
    else:
        return "F"


# Student Data (MIVA Level 300)
student_name = "John - MIVA Level 300"
scores = [70, 65, "80", 90]

try:
    average = calculate_average(scores)

    if average > 50:
        print(student_name + " passed")
    else:
        print(student_name + " failed")

    grade = get_grade(average)

    print("Average:", average)
    print("Grade:", grade)

except Exception as e:
    print("An error occurred:", e)