from application_menu import *



def main_menu():

    choice = None

    while choice != '0':
        # clear()
        print("="*35+"\nPlease, specify which user you are!\nEnter '0' to quit.\n")
        for key, value in menu.items():
            print('{}) {}'.format(key, value.__doc__))
        choice = input('Menu number: ').lower().strip()

        if choice in menu:
            clear()
            menu[choice]()




menu=OrderedDict([
    ('1', applicant_menu_loop),
])
