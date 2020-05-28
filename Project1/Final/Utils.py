import msvcrt as m


#other functions
def backtomain(): #escape not working
    if m.kbhit() and m.getch()[0] == 27: #not working
        Project_Main.main_menu()

def func_error():
    print("""
            <ERROR> Please choose another option""");

def func_a():
    print("""
        Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labor et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi uts aliquip ex ea commodo consequat.

        Duis aute irure dolor in reprehenderit in voluptate velit esse cil dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa officia deserunt mollit anim id est laborum.""");
