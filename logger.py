from datetime import datetime as dt

def log_winner (for_log):
    time = dt.now().strftime ('%H:%M')
    with open ('game_result.txt', 'a') as file:
        file.writelines ('{} - {}'
                .format(time, for_log))
