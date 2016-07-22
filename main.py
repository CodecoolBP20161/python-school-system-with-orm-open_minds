from contact_school import ContactSchool
from application_code_gen import assign_app_codes
from example_data import *
from interview_slot_handling import InterviewHandling
from main_menu import *
from build import build


build()
print("Empty tables created! :)")
input("[Press Enter]\n")
add_city()
print("Cities added.")
input("[Press Enter]\n")
add_schools()
print("Schools added.")
input("[Press Enter]\n")
add_mentors()
print("Mentors added.")
input("[Press Enter]\n")
add_applicants()
print("Applicants added.")
input("[Press Enter]\n")
add_interview_slot()
print("Interview slots added.")
input("[Press Enter]\n")
assign_app_codes()
print("Applicants get code.")
input("[Press Enter]\n")
ContactSchool.get_nearest_school()
input("[Press Enter]\n")
InterviewHandling.interview_handling()
input("[Press Enter to Menu or press Ctrl+d to quit!]\n\n")
main_menu()
