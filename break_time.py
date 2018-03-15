import time
import random
import webbrowser   # used to open the webbrowser

# to open a specific webbrowser webbrowser.get(webbrowser name)
# webbrowser.open_new(url)-opens in a new window
# webbrowser.open_new_tab(url)-opens in a new tab
# time.sleep
# time.ctime which specifies the current time

#This is the list default collection of youtube videos
you_collection = ["https://www.youtube.com/watch?v=bek1y2uiQG",
       "https://www.youtube.com/watch?v=4uTNVumfm84",
       "https://www.youtube.com/watch?v=09R8_2nJtjg",
       "https://www.youtube.com/watch?v=PT2_F-1esPk",
       "https://www.youtube.com/watch?v=2Vv-BfVoq4g",
       "https://www.youtube.com/watch?v=nYh-n7EOtMA",
       "https://www.youtube.com/watch?v=1NktXS1GiWU",
       "https://www.youtube.com/watch?v=JGwWNGJdvx8",
       "https://www.youtube.com/watch?v=FM7MFYoylVs",
       "https://www.youtube.com/watch?v=dT2owtxkU8k",
       "https://www.youtube.com/watch?v=lY2yjAdbvdQ",
       "https://www.youtube.com/watch?v=VbfpW0pbvaU"
      ]

total_breaks = int(input("Enter the total number of breaks you want to take: "))
# This is the total number of breaks a user is going to take
while True:
    total_breaks = int(input("Invalid Value\nPlease Enter a Positive no.: ")) # To ensure that user inputs a positive value
    if total_breaks>0:
        break
break_number = 0  # Break number

sleep_time = int(input("Enter the time between breaks: "))
while True:
    sleep_time = int(input("Invalid Value\nEnter the Positive no.: "))        # To ensure that user inputs a positive value
    if sleep_time>0:
        break

url = input("Enter Your Favorite Youtube Playlist Url or Press Enter to Continue with our Collection:")
#for user entered url
if len(url)>0:
    print("The program started on:- "+time.ctime())
    while break_number < total_breaks:
        time.sleep(sleep_time)  # sleeps for 10 seconds
        webbrowser.open(url)
        break_number += 1
#if user chose our collection
else:
    url = you_collection
    print("The program started on:- "+time.ctime())
    while break_number < total_breaks:
        time.sleep(sleep_time)  # sleeps for 10 seconds
        surprise = random.randint(0,len(url))  #to get different videos every time
        webbrowser.open(url[surprise])
        break_number += 1
