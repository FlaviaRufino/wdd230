import csv


YEAR_COLUMN = 0
FATALITIES_COLUMN = 1
INJURIES_COLUMN = 2
CRASHES_COLUMN = 3
FATAL_CRASHES_COLUMN = 4
DISTRACT_COLUMN = 5
PHONE_COLUMN = 6
SPEED_COLUMN = 7
DUI_COLUMN = 8
FATIGUE_COLUMN = 9


def main():
    try:
        filename = input("Name of file that contains NHTSA data: ")
        with open(filename, "rt") as text_file:
            perc_reduc = get_percentage_reduction()

            print()
            print(f"With a {perc_reduc}% reduction in using a cell",
                "phone while driving, approximately the",
                "following number of injuries and deaths",
                "would have been prevented in the USA.", sep="\n")
            print()
            print("Year, Injuries, Deaths")

            reader = csv.reader(text_file)
            next(reader)

            for row in reader:
                year = row[YEAR_COLUMN]
                injur, fatal = estimate_reduction(row, PHONE_COLUMN, perc_reduc)
                print(year, injur, fatal, sep=", ")

    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied. You don't have the necessary permissions to access the file.")
    except ValueError:
        print("Error: Invalid input. Please enter a valid percentage.")
    except csv.Error:
        print("Error: Invalid CSV file format.")

def get_percentage_reduction():
    while True:
        try:
            perc_reduc = float(input("Percent reduction of texting while driving [0, 100]: "))
            if perc_reduc < 0 or perc_reduc > 100:
                raise ValueError
            return perc_reduc
        except ValueError:
            print("Error: Invalid input. Please enter a valid percentage.")

def estimate_reduction(row, behavior_key, perc_reduc):
    behavior = int(row[behavior_key])
    fatal_crashes = int(row[FATAL_CRASHES_COLUMN])
    ratio = perc_reduc / 100 * behavior / fatal_crashes

    fatalities = int(row[FATALITIES_COLUMN])
    injuries = int(row[INJURIES_COLUMN])

    reduc_fatal = int(round(fatalities * ratio, 0))
    reduc_injur = int(round(injuries * ratio, 0))
    return reduc_injur, reduc_fatal


if __name__ == "__main__":
    main()
