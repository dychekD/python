def choose_mode ():
    print ('------------MENU------------')
    print ('enter 0 to view all employees\n'
            'enter 1 to add a new employee\n'
            'enter 2 to start search\n'
            'enter 3 to delete an employee\n'
            'enter 4 to exit')
    mode = int (input('enter your value: '))
    if mode > 4 or mode < 0: 
        print ('please enter integer between 0 and 2')
        mode = int(input())
    return mode




    