import time 
from time import strptime

def get_time():
    time = strptime("2024-2-25 15:06:00 %p")
    return time 
while True:
    print(get_time(), end = "")
    print("\r", end = "")
    time.sleep(1)