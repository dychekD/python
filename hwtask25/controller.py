from logger import get_data as gd
from logger import log_contact as lg
from model import search_contact as sc
from model import view_search_res as vsr
from view import choose_mode as cm

def run_book ():
    mode = cm ()
    if mode == 0:
        lg(gd())
    else: vsr (sc())


