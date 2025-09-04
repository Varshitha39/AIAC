def assign_grade(score):
    # Check for valid numeric input
    if not isinstance(score, (int, float)):
        return "Invalid input"
    # Check for valid score range
    if score < 0 or score > 100:
        return "Invalid input"
    # Grade assignment with correct boundaries
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    else:
        return "F"