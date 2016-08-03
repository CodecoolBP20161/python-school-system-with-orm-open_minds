from main_menu import *
from build import *


# The InterviewSlot isn't fill with data.
# The database created, but when you run the menu the function called wrong path.
build()
print("Empty tables created :)")
input("[Press Enter]\n")
School.add_schools()
print("Schools added.")
input("[Press Enter]\n")
City.add_cities()
print("Cities added.")
input("[Press Enter]\n")
Mentor.add_mentors()
print("Mentors added.")
input("[Press Enter]\n")
Applicant.add_applicants()
print("Applicant added.")
input("[Press Enter]\n")
# InterviewSlot.add_interview_slot()
# print("Interview slots added.")
# input("[Press Enter]\n")
input("[Press Enter to enter the user menu or press Ctrl+d to quit!]\n\n")
main_menu()
