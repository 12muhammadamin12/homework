def calculate_class_averages(scores: dict) -> dict:
    # Custom rounding function
    def round_custom(value):
        return int(value) if value % 1 <= 0.5 else int(value) + 1

    averages = {}
    for class_name, marks in scores.items():
        if marks:
            avg = sum(marks) / len(marks)
            averages[class_name] = round_custom(avg)
        else:
            averages[class_name] = 0
    return averages

scores1 = {"Class A": [70, 80, 90], "Class B": [50, 60]}
scores2 = {"Class A": [85, 90, 95], "Class B": [60, 70], "Class C": [50], "Class D": [100, 80, 60, 40]}
scores3 = {"Class A": [90, 80], "Class B": [], "Class C": [70], "Class D": [100, 95, 90, 85], "Class E": []}
scores4 = {"Class A": [90.5, 0, 70.8], "Class B": [100, 50.6, 75.2], "Class C": [45, 67.5],
           "Class D": [89.9, 90.1, 91.0]}

print(calculate_class_averages(scores1))
print(calculate_class_averages(scores2))
print(calculate_class_averages(scores3))
print(calculate_class_averages(scores4))
