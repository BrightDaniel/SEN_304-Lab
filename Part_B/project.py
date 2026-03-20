def calculate_average(scores):
    total = 0
    for score in scores:
        total += float(score)
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