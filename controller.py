from view import choose_mode
from hwtask21 import game
from hwtask21 import game_vs_bot
from logger import log_winner


def run_game ():
    mode = choose_mode()
    if mode == 1: 
        for_log = game()
    else: 
        for_log = game_vs_bot() 
    log_winner (for_log)
    return for_log
    
