personal_data = {
    "name": "Harsha Javadala", 
    "age": 25,
    "height": 1.75,
    "is_student": True
}

# Task 1: Variables and Data Types
name = personal_data["name"]
age = personal_data["age"]
height = personal_data["height"]
is_student = personal_data["is_student"]
print(name, age, height, is_student)
# Task 2: String Formatting
print(f"Name: {name} | Age: {age} | Height: {height} | Student: {is_student}")
# Task 3: Arithmetic Operations
age_in_months = age * 12
age_in_days = age * 365
remainder = age % 7
age_squared = age ** 2
print(f"Age in months: {age_in_months}")
print(f"Age in days: {age_in_days}")
print(f"Remainder when age is divided by 7: {remainder}")
print(f"Age raised to the power of 2: {age_squared}") 