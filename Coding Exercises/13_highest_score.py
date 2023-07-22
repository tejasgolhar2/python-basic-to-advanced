# A List of scores of students are given,
# implement a program that calculates the
# highest score from the given list.

student_scores = [80, 60, 50, 65, 75, 55]

min = 0
for score in student_scores:
    if score > min:
        min = score
print(f"The highest score in the class is: {min}")
