def choose_mode ():
    print ('please enter 0 to add a new contact or 1 to start search')
    mode = int (input())
    if mode > 1 or mode < 0: 
        print ('please enter 0 or 1')
        mode = int(input())
    return mode


    