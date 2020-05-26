import msvcrt as m
import re
import os

#initiate the dictionary outside de class
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
    actioninput.action = input('            Please choose an option and press <Enter>: ').lower();

def backtomain(): #escape not working
    if m.kbhit() and m.getch()[0] == 27: #not working
        main_menu()

def inputprojectname():
    #ask for input on the name of project and check if valid
    pass

def checkuserinput():
    #check if input is valid. It will be adaptable according to the use
    pass

def lookup_project(projectnamegiven):
    global projectfound
    global words
    projectfound = None
    fhandle = open('all_projects.txt', 'r')
    for line in fhandle:
        words = line.split(',')
        if projectnamegiven != words[0] or len(words) < 1:
            projectfound = False
            continue
        elif projectnamegiven == words[0]:
            projectfound = True
            break
    fhandle.close()
    return projectfound
    return words

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
            fhandle = open('all_projects.txt', 'a+')
            project_name = input("""
            Enter the project name: """).lower()
            if not re.match('[a-zA-Z]', project_name): #checks in the name is valid
                print("""
            Name must have letters and numbers""")
                continue
            else:
                lookup_project(project_name)
                if projectfound == False:
                    nameofproject = '\n' + project_name + ','
                    fhandle.write(nameofproject)
                    all_projects[project_name] = {}
                    for line in fhandle:
                        words = line.split(',')
                elif projectfound == True:
                    print("""
            Name already exists. Please enter a new name.""")
                    continue
                break
            fhandle.close()

    def func_vote_project():
        names_voters = []
        while True:
            action_v = input("""
            Enter the project name: """).lower()
            lookup_project(action_v)
            if projectfound == False:
                print(input("""
            Project not found. Press <ESC> to go back to
            the Main Menu or press <ENTER> to try again: """))
                backtomain()  #will go back to the main menu if project name does not exist so it can be looked up or added
                continue
            else:
                if action_v != words[0] or len(words) < 1:
                    continue
                else:
                    print(f"""
                    There are {words[1]} team members""")
                    findlastmember = 1 + int(words[1])
                    names_voters = words[2:(findlastmember+1)] #Makes a list with names from the file for looping thro
                    members_being_voted = names_voters
                    print(members_being_voted)

                while True:
                    for nv in names_voters:
                        total = 0
                        vote = 0
                        print(f"""
                    Enter {nv}'s votes, points must add up to 100: """)
                        for mbv in members_being_voted:
                            if nv != mbv:
                                vote = input(f"""
                    Enter {nv}'s points for {mbv}:    """)
                                try:
                                    if type(int(vote)) == 'int' :
                                        continue
                                except:
                                    print("""
                    <ERROR> Points should be a valid number in between
                    0 and 100. Please press  <ENTER>  and start again.""")
                                    continue
                                else:
                                    total = total + int(vote)
                                    continue

                        if re.match('[0-9]', vote) and total != 100 :
                            print("""
                    Points must add up to 100. Please start again.""")
                            break
                        else:
                            fhandle.write(nv, mbv, int(vote),)
                            continue
                        break
                fhandle.close()

        print(input("""
            Press <Enter> to return to the main menu: """), 'Line143');

#child class
class Person(Project):
    def func_add_members():
        global temp_list
        fhandle = open('all_projects.txt', 'a+')
        while True:
            number_of_members = input("""
            Enter the number of team members: """)
            try:
                int(number_of_members) > 0
            except:
                print("""
            <ERROR> It must be a number greater than 0""")
                continue
            else:
                number_of_members = int(number_of_members)
                break

        all_projects[project_name]['Number_of_members'] = number_of_members
        fhandle.write(str(number_of_members) + ',')

        member_number = 0
        temp_list = []
        while number_of_members > 0:
            number_of_members -= 1
            member_number += 1
            while True:
                member_name = input(f"""
            Enter the name of team member {member_number}: """).lower()
                if not re.match('[a-zA-Z]', member_name):
                    print("""
            Please enter a valid name""")
                    continue
                else:
                    temp_list.append(member_name)
                    member_name = member_name + ','
                    fhandle.write(member_name)
                    break

        fhandle.close()
        members_names = temp_list
        all_projects[project_name]['Members'] = members_names
        proj_members = {n : 0 for n in all_projects[project_name]['Members']}
        all_projects[project_name]['Members'] = proj_members

        print(input("""
            Press <Enter> to return to the main menu: """, ));

def func_a():
    print("""
    Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labor
    et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi uts
    aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cil
    dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa quis
    officia deserunt mollit anim id est laborum.""");

def func_s():
    action_s = input("""
    Enter the project name: """).lower()

    lookup_project(action_s) #checks if given project names is in the file
    if projectfound == True:
        fhandle = open('all_projects.txt', 'a+')
        for line in fhandle:
            words = line.split(',')
            for word in words:
                findlastmember = 1 + words[1]
                listofnames = words[2:findlastmember] #Makes a list with names from the file for looping thro
                random_iterator = iter(line)
                for name in listofnames:
                    for w in random_iterator:
                        if w == name and next(random_iterator, '').isnumeric() == True:
                            name = []
                            print(name, 1)
                            located = line.index(w) +1
                            vote_received = int(line[located])
                            vote_shared = 100 - vote_received
                            rate = (vote_shared/vote_received)
                            name.append(rate)
                            print(name, 2)
                            continue

                    else:
                        break

                    name = 1 / 1 + sum(name)
                    print(name, 1)

    print("""
    The point allocation based on votes is: """)
    print("""
    words[5]: """)
    print("""
    words[10]: """)
    print("""
    words[15]: """)

    print(input("""
                Press <Enter> to return to the main menu: """, ));


def func_error():
    print("""
    <ERROR> Please choose another option""");

def condfun():
    if actioninput.action == 'a' :
        func_a()

    elif actioninput.action == 'c' :
        Project.func_add_project()
        Person.func_add_members()

    elif actioninput.action == 'v':
        Project.func_vote_project()

    elif actioninput.action == 's':
        func_s()
        pass

    elif actioninput.action == 'q':
        exit()

    else:
        func_error()
        pass

while True:
    main_menu()
    actioninput()
    condfun()
