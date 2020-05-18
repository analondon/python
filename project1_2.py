import msvcrt as m
import re

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

def actioninput():
    actioninput.action = input('            Please choose an option and press <Enter>: ').upper();


class Project:

    def func_add_project():
        global project_name
        global nameofproject
        project_name, nameofproject = "", ""
        global members_names
        members_names = []

        while True:
            project_name = input('    Enter the project name: ')
            if not re.match('[a-zA-Z0-9]', project_name):
                print('Name must have letters and numbers')
                continue
            else:
                if not project_name in all_projects :
                    nameofproject = project_name
                    all_projects[project_name] = {}
                    print(all_projects)
                    return nameofproject
                else:
                    print('Name already exists. Please enter a new name.')
                    continue
                break

    def func_vote_project():
        while True:
            action_v = input('    Enter the project name: ')
            if not action_v in all_projects.keys():
                print('Project not found')
                continue
            else:
                print(f"There are {all_projects[nameofproject]['Number_of_members']} team members")
                break

        names_voters = temp_list
        allvotes = []
        while True:
            for nv in names_voters:
                total = 0
                vote = 0

                print(f"Enter {nv}'s votes, points must add up to 100: ")
                for k, v in all_projects[nameofproject]['Members'].items():
                    if nv != k:
                        vote = input(f"       Enter {nv}'s points for {k}: ")
                        total = total + int(vote)
                        all_projects[nameofproject]['Members'][k] = v + int(vote)
                        print(all_projects, 2)
                        print(k, v, 3)

                if total != 100 :
                    print('Points must add up to 100. Please start again.')
                    continue
            break

        print(input('Press <Enter> to return to the main menu: ', ));

class Person(Project):
    def func_add_members():
        global temp_list
        while True:
            number_of_members = input('Enter the number of team members: ')
            if not re.match('[0-9]', number_of_members):
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
        print(proj_members, 'XXX')

        # print(members_names, '3')
        print(all_projects)
        print(input('Press <Enter> to return to the main menu: ', ));

def func_a():
    print('Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.');

def func_error():
    print('<ERROR>');

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
