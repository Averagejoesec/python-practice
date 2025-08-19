import csv

def average(scores):
    scores_list = scores.split(", ")
    scores_length = float(len(scores_list))
    total = 0
    for score in scores_list:
        try:
            score = round(float(score), 2)
            if score >= 0 and score <= 100:
                total = score + total
            else:
                print("Invalid input: all scores must be numbers between 0 and 100 and separated by commas")
                break
        except:
            print("Invalid input: all scores must be numbers between 0 and 100 and separated by commas")
            exit()
    average_score = total / scores_length
    average_score = round(average_score, 2)

    grade = ""
    if average_score >= 90.00:
        grade = "A"
    elif average_score >= 80 and average_score <= 89:
        grade = "B"
    elif average_score >= 70 and average_score <= 79:
        grade = "C"
    elif average_score >= 60 and average_score <= 69:
        grade = "D"
    elif average_score <= 59:
        grade = "F"
    
    verdict = "Fail"
    if grade == "A" or "B" or "C" or "D":
        verdict = "Pass"

    return average_score, grade, verdict


def write_to_csv(data):
    with open("grades.csv", "w", newline="") as csvfile:
        field_names = ["Score", "Grade", "Pass/Fail"]
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

if __name__ == "__main__":
    data = []
    while True:
        scores = input("Enter scores separated by commas: ")
        average_score, grade, verdict = average(scores)
        data.append(({"Score": average_score, "Grade": grade, "Pass/Fail": verdict}))
        if average_score and grade and verdict:
            print(f"Average: {average_score}")
            print(f"Letter Grade: {grade}")
            print(f"Result: {verdict}")
        another_student = input("Would you like to add another student? (Y/N) ")
        if another_student.lower() == "n":
            write_to_csv(data)
            exit()
