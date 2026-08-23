def student_info(name, age, department):
    print("Student Name:", name)
    print("Age:", age)
    print("Department:", department)


def calculate_average(marks):
    total = sum(marks)
    average = total / len(marks)
    return average


def check_result(average):
    if average >= 50:
        return "Pass"
    else:
        return "Fail"