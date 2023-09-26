with open("courses.txt") as courses_file:
    for line in courses_file:
        # line = "CSE 110,98.5"
        clean_line = line.strip()
        print(clean_line)

        parts = line.split(",")

        parts = ["CSE 110", "98.5"]
        name = parts[0]
        grade = float(parts[1])

        bonus_grade = grade + 3

        print(f"{name} - grade: {grade}, after bonus: bonus: {bonus_grade}")

        

        print()


