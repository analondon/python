import msvcrt as m
import os
import re
import Utils
from Classes import Person, Project


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

def condfun():
    if actioninput.action == 'a' :
        Utils.func_a()

    elif actioninput.action == 'c' :
        Project.func_add_project()
        Person.func_add_members()

    elif actioninput.action == 'v':
        Project.func_vote_project()

    elif actioninput.action == 's':
        Project.func_s()

    elif actioninput.action == 'q':
        exit()

    else:
        Utils.func_error()
        pass

# __name = main
while True:
    main_menu()
    actioninput()
    condfun()
