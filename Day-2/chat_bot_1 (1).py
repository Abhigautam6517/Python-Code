import datetime
import os
import webbrowser
hello = ["heyy", "hello", "heyy there", "hi"]
bye = ["bye", "talk to you later", "see you", "later"]
while True:
    msg = input("enter your message: ")
    if msg in hello:
        print("Heyy there!")
    elif msg in bye:
        print("See you soon!!")
        break
    elif "date" in msg and "time" in msg:
        print(datetime.datetime.now())
    elif "date" in msg:
        print(datetime.date.today())
    elif "time" in msg:
        print(datetime.datetime.now().strftime("%H:%M:%S"))
    elif "song" in msg:
        song_list = os.listdir("songs")
        os.startfile("songs\\"+song_list[0])
    elif "google" in msg:
        webbrowser.open("www.google.com")
    else:
        print("I don't understand")
