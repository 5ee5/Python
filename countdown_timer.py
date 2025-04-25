import time
import datetime

def countdown(hours, minutes, seconds):
    # Calculate total seconds from hours, minutes, and seconds
    total_seconds = hours * 3600 + minutes * 60 + seconds
    
    while total_seconds > 0:
        # Calculate remaining hours, minutes, and seconds
        hrs, rem = divmod(total_seconds, 3600)
        mins, secs = divmod(rem, 60)
        
        # Print the time left in HH:MM:SS format
        print(f'{hrs:02}:{mins:02}:{secs:02}', end='\r')
        time.sleep(1)  # Wait for 1 second
        total_seconds -= 1  # Decrement total seconds

    print("TIME'S UP!")  # Notify when the countdown is finished

# User input for hours, minutes, and seconds
try:
    h = int(input("Enter the number of hours: "))
    m = int(input("Enter the number of minutes: "))
    s = int(input("Enter the number of seconds: "))
    countdown(h, m, s)  # Start the countdown
except ValueError:
    print("Please enter valid integers.")