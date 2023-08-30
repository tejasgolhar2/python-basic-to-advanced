
# Student Grades
# Implement a function which takes a dictionary as a parameter in which student scores are stored and converts their scores to grades and return it as new dictionary.

# This is the scoring criteria:

# Scores 85 - 100: Grade = "Outstanding"
# Scores 65 - 84: Grade = "Good"
# Scores 50 - 64: Grade = "Acceptable"
# Scores 50 lower: Grade = "Fail"
# Example

# student_scores = {
#   "John": 90,
#   "Edy": 68,
#   "Marry": 88, 
#   "Ewan": 79,
#   "Park": 62,
# }
# convert_grade(student_scores)
# Output

# {
#  'John': 'Outstanding', 
#  'Edy': 'Good', 
#  'Marry': 'Outstanding', 
#  'Ewan': 'Good', 
#  'Park': 'Acceptable'
# } 

def convert_grade(scores):
    grades = dict()
    for value in scores:
        if (scores[value]<=100) and  (scores[value]>=85):
            grades[value]="Outstanding"
        elif (scores[value]<=84) and (scores[value]>=65):
            grades[value]="Good"
        elif (scores[value]<=64) and (scores[value]>=50):
            grades[value]="Acceptable"
        else:
            grades[value]="Fail"
    return grades
            
student_scores = {
  "John": 90,
  "Edy": 68,
  "Marry": 88, 
  "Ewan": 79,
  "Park": 62,
}
print(convert_grade(student_scores))