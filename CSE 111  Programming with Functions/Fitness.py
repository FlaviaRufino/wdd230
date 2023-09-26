from datetime import datetime

def compute_age(birth_str):
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()
    years = today.year - birthdate.year

    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1

    return years

def kg_from_lb(pounds):
    return pounds * 0.45359237

def cm_from_in(inches):
    return inches * 2.54

def body_mass_index(weight, height):
    return (10000*weight) / (height**2)

def basal_metabolic_rate(weight, height, age, gender):
    if gender.lower()  == "f":
        bmr = 447593 + 9247 * weight + 3098*height - 4330*age
    elif gender.lower() == "m":
        bmr = 88362 + 13397 * weight + 4799*height - 5677*age
    return bmr

def main ():
    gender = input("Please type your gender (F/M): ")
    birthdate = input("Please type your birthdate in this format YYYY-MM-DD: ")
    weight_pounds = float(input("Please type your weight in U.S. pounds: "))
    height_inches = float(input("Please type your height in U.S. inches: "))

    weight_kg = kg_from_lb(weight_pounds)
    height_cm = cm_from_in(height_inches)
    age = compute_age(birthdate)

    bmi = body_mass_index(weight_kg, height_cm)
    bmr = basal_metabolic_rate(weight_kg, height_cm, age, gender)

    print(age)
    print(weight_kg)
    print(height_cm)
    print(bmi)
    print(bmr)

main()