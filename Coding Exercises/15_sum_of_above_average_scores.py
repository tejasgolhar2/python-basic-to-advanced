# Implement a function which takes a List as a parameter 
# and returns the sum of the scores which are above average.


def sum_score_above_average(p_student_scores):
    # TODO
    sum = 0
    val = 0
    count = 0
    res = 0
    for val in p_student_scores:
        sum += val
        count += 1
    avg = (sum) / (count)
    for val in p_student_scores:
        if val > avg:
            res += val
    return res
    
    
    
student_scores = [80, 60, 50, 65, 75, 55]
result = sum_score_above_average(student_scores)
print(result)