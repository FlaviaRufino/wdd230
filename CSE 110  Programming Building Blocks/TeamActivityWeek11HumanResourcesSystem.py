with open("hr_system.txt") as system_file:
    for line in system_file:
        clean_line = line.strip()
        #print(clean_line)

        parts = line.split(" ")
        name = parts[0]
        title = parts[2]

        print(f"Name: {name}, Title: {title}")
        

        
        