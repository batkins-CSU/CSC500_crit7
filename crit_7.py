
courseRooms = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411"
}

courseInstructors = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee"
}

courseTime = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m."
}

def main ():
    course = "None"
    while course not in courseRooms:
        course = input("Enter a course number: ").upper().strip()
        try:
            print("Room:", courseRooms[course])
            print("Instructor:", courseInstructors[course])
            print("Time:", courseTime[course])
        except:
            print(f"Course not found, courses available are: {list(courseRooms.keys())}")


if __name__ == "__main__":
    main()

