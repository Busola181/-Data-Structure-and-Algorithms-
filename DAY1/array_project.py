# 🧠 Project Title: Student Grade Analyzer


#Creating a dynamic array to store student's scores
students_scores =[]

# Function to store and analyze student scores
def add_student_score(name, score):
    """Add a student's score to the list."""
    students_scores.append((name, score))

#Function to calculate the average score of students
def average_score():
    total_score = 0
    for student in students_scores:
       total_score += student[1]
    average = total_score/len(students_scores)
    return average

def highest_score():
    highest = students_scores[0]
    for student in students_scores:
        if student[1] > highest[1] :
            highest = student
    return highest


def lowest_score():
    lowest = students_scores[0]
    for student in students_scores:
        if student[1] < lowest[1]:
            lowest = student
    return student
    
def passed_students():
    count = 0
    pass_mark = 50
    for student in students_scores:
        if student[1] >= 50:
            count += 1
    return count
    
#Sorting student scores in descending order
def sort_students_descending():
    return sorted(students_scores, key=lambda x: x[1], reverse=True)

add_student_score("Alice", 75)
add_student_score("Bob", 45)
add_student_score("Charlie", 82)
add_student_score("David", 39)


print("\n STUDENT'S SCORE ANALYSIS")
print(f"Average_score: {average_score()}")
print(f"Highest_score: {highest_score()[0]} with {highest_score()[1]}")
print(f"Lowest_score: {lowest_score()[0]} with {lowest_score()[1]}")
print(f"Number_of_students_who_passed: {passed_students()}")

print("\n Student score in descending order")
for student in sort_students_descending():
    print(f"{student[0]} has score {student[1]}")
