import time
from os import system

def countDown(t):
 while t>0:
    print(f"Time remaining: {t} seconds")
    time.sleep(1)
    system("clear")
    t-=1
    
 print("Time is out")

countDown(5)
