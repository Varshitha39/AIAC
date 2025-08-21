def classify_age(age):
    if age >0:
        if age <13:
            return "child"
        elif age <20:
            return "teenager"
        elif age<60:
            return "adult"
        else:
            return "senior"
    else:
            return "invalid age"

age = int(input("Enter your age:"))
result = classify_age(age)
print(f"You are a {result}.")