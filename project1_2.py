import msvcrt as m
import re

def backtomain(): #escape not working
    escape = input('Project not found. Press <ESCAPE> to go back to the Main Menu or <ENTER> to try again: ', )
    if m.kbhit() and m.getch()[0] == 27:
        main_menu()

all_projects = {}

def main_menu():
    print("""
    Welcome to Split-It

    About            (A)
    Create Project   (C)
    Enter Votes      (V)
    Show Project     (S)
    Quit             (Q)

    """
    )
#gets input from user, converts into uppercase to be compared with the option in condfun()
def actioninput():
    actioninput.action = input('            Please choose an option and press <Enter>: ').upper();

#parent class
class Project:
    #allowes our user to add a new project into the file
    def func_add_project():
        global project_name
        global nameofproject
        project_name, nameofproject = "", ""
        global members_names
        members_names = []

        while True:
            project_name = input('    Enter the project name: ')
            if not re.match('[a-zA-Z0-9]', project_name): #checks in the name is valid
                print('Name must have letters and numbers')
                continue
            else:
                if not project_name in all_projects :
                    nameofproject = project_name #project_name will be turned into a dictionary named after the input from the user. String from input saved in a new variable to be accessed later in the code
                    all_projects[project_name] = {} #addsthe new project created into the main dictionary of projects
                    return nameofproject #returns string from user input
                else:
                    print('Name already exists. Please enter a new name.')
                    continue
                break

    def func_vote_project():
        while True:
            action_v = input('    Enter the project name: ')
            if not action_v in all_projects.keys():
                backtomain() #will go back to the main menu if project name does not exist so it can be looked up or added
                continue
            else:
                print(f"There are {all_projects[nameofproject]['Number_of_members']} team members")
                break

        names_voters = temp_list #temp list is created in class Person. A copy is made for looping thro
        while True:
            for nv in names_voters:
                total = 0
                vote = 0

                print(f"""Enter {nv}'s votes, points must add up to 100: """)
                for k, v in all_projects[nameofproject]['Members'].items():
                    if nv != k:
                        vote = input(f"""
                               Enter {nv}'s points for {k}:""")
                        if not re.match('[0-9]', vote):
                            print('Points should be a valid number in between 0 and 100. Please press <ENTER> and start again.')
                            break
                        else:
                            total = total + int(vote)
                            all_projects[nameofproject]['Members'][k] = v + int(vote)
                            continue

                if re.match('[0-9]', vote) and total != 100 :
                    print('Points must add up to 100. Please start again.')
                    break
            break

        print(input('Press <Enter> to return to the main menu: ', ));

#child class
class Person(Project):
    def func_add_members():
        global temp_list
        while True:
            number_of_members = input('Enter the number of team members: ')
            try:
                int(number_of_members)
            except:
                print('<ERROR> It must be a number greater than 0')
                continue
            else:
                if int(number_of_members) > 0:
                    number_of_members = int(number_of_members)
                    break

        all_projects[nameofproject]['Number_of_members'] = number_of_members
        member_number = 0
        temp_list = []
        while number_of_members > 0:
            number_of_members -= 1
            member_number += 1
            while True:
                member_name = input(f'Enter the name of team member {member_number}: ')
                if not re.match('[a-zA-Z]', member_name):
                    print('Please enter a valid name')
                    continue
                else:
                    temp_list.append(member_name)
                    break

        members_names = temp_list
        all_projects[nameofproject]['Members'] = members_names
        proj_members = {n : 0 for n in all_projects[nameofproject]['Members']}
        all_projects[nameofproject]['Members'] = proj_members

        print(input('Press <Enter> to return to the main menu: ', ));

def func_a():
    print('Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.');

def func_error():
    print('<ERROR> Please choose another option');

def condfun():
    if actioninput.action == 'A' :
        func_a()

    elif actioninput.action == 'C' :
        Project.func_add_project()
        Person.func_add_members()

    elif actioninput.action == 'V':
        Project.func_vote_project()

    elif actioninput.action == 'S':
        pass

    elif actioninput.action == 'Q':
        exit()

    else:
        func_error()
        pass

while True:
    main_menu()
    actioninput()
    condfun()
