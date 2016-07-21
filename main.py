from contact_school import ContactSchool
from application_code_gen import assign_app_codes
from example_data import *
from interview_slot_handling import InterviewHandling


add_city()
print("Cities created.")
input("[Press Enter]")
add_schools()
print("Schools created.")
input("[Press Enter]")
add_mentors()
print("Mentors created.")
input("[Press Enter]")
add_applicants()
print("Applicants created.")
input("[Press Enter]")
add_interview_slot()
print("Interview slots created.")
input("[Press Enter]")
assign_app_codes()
print("Applicants get code.")
input("[Press Enter]")
ContactSchool.get_nearest_school()
input("[Press Enter]")
InterviewHandling.check_reserved_interviews()
