from logger import *
from model import *
from view import *

def run_book ():
    while True:
        mode = choose_mode ()
        if mode < 4:
            if mode == 0:
                show_all_contacts ()
            elif mode == 1:
                log_contact(get_data())
            elif mode == 2:
                view_search_res (search_contact())
            elif mode == 3:
                delete_employee ()
        elif mode == 4:
            exit()
    


