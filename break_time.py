import time
import webbrowser   # used to open the webbrowser

# to open a specific webbrowser webbrowser.get(webbrowser name)
# webbrowser.open_new(url)-opens in a new window
# webbrowser.open_new_tab(url)-opens in a new tab
# time.sleep
# time.ctime which specifies the current time

total_breaks = int(input("Enter the total number of breaks you want to take: "))
# This is the total number of breaks a user is going to take
break_number = 0  # Break number
if total_breaks > 0:
    sleep_time = int(input("Enter the time between breaks: "))
    print("The program started on "+time.ctime())
    while break_number < total_breaks:
        time.sleep(sleep_time)  # sleeps for 10 seconds
        webbrowser.open("https://www.youtube.com/watch?v=bek1y2uiQGA")
        break_number += 1
else:
    print("Number of breaks should be greater than 0")


