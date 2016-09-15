from menu.menu_application import *
from menu.menu_administration import *

# This is the main loop, which handles the sub menu choices.

def main_menu():

    choice = None

    while choice != '0':
        print("="*14+"\nChoose a user!\nEnter '0' to quit.\n")
        for key, value in menu.items():
            print('{}) {}'.format(key, value.__doc__))
        choice = input('Menu number: ').lower().strip()

        if choice in menu:
            clear()
            menu[choice]()

# This library allows you to choose an operation.
menu = OrderedDict([
    ('1', applicant_menu_loop),
    ('2', administrator_menu_loop)
])
