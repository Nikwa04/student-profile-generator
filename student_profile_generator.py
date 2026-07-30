# Session 1: Student Profile Generator

# Create variables that prompt the user for their information

name = input("Please enter your full name and surname: ")
age = int(input("Please enter your age: "))
course = input("Please enter your course: ")
favourite_hobby = input("What is your favourite hobby?: ")
cut_student = bool(input("Are you a registered CUT student? [Yes/No]: "))

# Display the user's input using f-strings
print("\n")
print("=" * 50)
print("STUDENT PROFILE GENERATOR")
print("=" * 50)

print("\n")
print(f"Name:                                 {name}")
print(f"Age:                                  {age}")
print(f"Course:                               {course}")
print(f"Favourite Hobby:                      {favourite_hobby}")
print(f"CUT Student:                          {cut_student}")