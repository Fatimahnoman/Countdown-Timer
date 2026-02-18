#                         ----------------------------
# ======================== Project:  "CountDown Timer" ================================
#                         ----------------------------

import time

def countdown(seconds):
    while seconds >= 0:
        mins = seconds // 60
        secs = seconds % 60
        print(f"{mins:02}:{secs:02}", end="\r")
        time.sleep(1)
        seconds -= 1
    print("00:00")

# User se input lena
time_seconds = int(input("Enter time in seconds: "))
countdown(time_seconds)







#import time 
# time module ko import karte hain taake sleep function use kar sakein

#def countdown_timer(seconds):  # Yeh function hai jo seconds ki value lega
