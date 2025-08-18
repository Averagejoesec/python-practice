def average(scores):
    scores_list = scores.split(", ")
    scores_length = float(len(scores_list))
    total = 0
    for score in scores_list:
        score = round(float(score), 2)
        total = score + total
    average_score = total / scores_length
    average_score = round(average_score, 2)

    grade = ""
    if average_score >= 90:
        grade = "A"
    elif average_score >= 80 and average_score <= 89:
        grade = "B"
    elif average_score >= 79 and average_score <= 70:
        grade = "C"
    elif average_score >= 60 and average_score <= 69:
        grade = "D"
    elif average_score >= 80 and average_score <= 89:
        grade = "F"
    
    verdict = "Fail"
    if grade == "A" or "B" or "C" or "D":
        verdict = "Pass"

    return average_score, grade, verdict


if __name__ == "__main__":
    scores = input("Enter scores separated by commas: ")
    average_score, grade, verdict = average(scores)
    print(f"""
            Average: {average_score}
            Letter Grade: {grade}
            Result: {verdict}
            """)
