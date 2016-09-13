from menu_main import *
from db_init import create_table
from model.model_city import City
from model.model_school import School

# The InterviewSlot isn't fill with data.
# The database created, but when you run the menu the function called wrong path.
create_table()
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
InterviewSlot.add_interview_slot()
print("Interview slots added.")
input("[Press Enter]\n")
Applicant.add_applicants()
print("Applicant added.")
input("[Press Enter]\n")
Applicant.finding_city()
print("Applicant get their assigned school and code.")
input("[Press Enter]\n")
Applicant.set_app_code()
print("\nApplicant get their interview time and notification.\n")
Applicant.assign_interview_slot()
input("\n\n[Press Enter to enter the user menu or press Ctrl+d to quit!]\n\n")
main_menu()
