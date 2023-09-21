#Animal Crossing Player by WinterTech13
from winsound import *
from datetime import datetime
import random
import time

def timecheck(hour):
    if hour >= 13:
        song = str(f"{hour - 12}pm")
    elif hour == 0:
        song = str(f"{hour + 12}am")
    elif hour == 12:
        song = str(f"{hour}pm")
    else:
        song = str(f"{hour}am")
    return song

def wintercheck(month, day):
    if month == 1:
        snowy = True
    elif month == 2 and day <= 24:
        snowy = True
    elif month == 11 and day >= 26:
        snowy = True
    else:
        snowy = False
    return snowy

def player(hour, song, snowy):
    x = random.randint(1, 2)
    y = True
    if snowy == True and x == 2:
        song = str(f"{song} Snowy")
    if snowy == False and x == 2:
        song = str(f"{song} Rainy")
    print(f"Now playing: {song}")
    PlaySound(f"{song}.wav", SND_LOOP + SND_ASYNC | SND_FILENAME)
    while y == True:
        y = timechange(hour)
    main()

def timechange(hour):
    new = datetime.now()
    diff = int(new.hour) - hour
    if diff == 1 or diff == -23:
        return False
    else:
        time.sleep(1)
        return True
        
def main():
    now = datetime.now()
    hour = now.hour
    month = now.month
    day = now.day
    song = timecheck(hour)
    snowy = wintercheck(month, day)
    player(hour, song, snowy)
    
main()
