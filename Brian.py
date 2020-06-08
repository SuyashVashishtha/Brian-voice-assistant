version = 2.4


import queue
from tkinter import *
from tkinter import ttk
import pyttsx3
import pyttsx3.drivers.sapi5
import pythoncom
import pywintypes
import requests
import threading
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import tkinter.messagebox
import smtplib
import glob

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')


engine.setProperty('voices', voices[0].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()


def wishme():
	hour = int(datetime.datetime.now().hour)
	if hour>0 and hour<12 :
		speak("Good morning Sir")
	elif hour>=12 and hour<18:
		speak("Good Afternoon Sir")
	else:
		speak("Good evening Sir")
	speak("I am brian, how can i help you ?")


wishme()


root =Tk()




menubar = Menu(root)
root.config(menu=menubar)

submenu = Menu(menubar, tearoff=0)
submenu = Menu(menubar, tearoff=0)


def help():

    readme = "res\\readme\\readme.txt"
    os.startfile(readme)


def exit():
    sys.exit()

def abrian():
    speak("Hi, I am brian, a Virtual assistant made for you")
    speak("Mr. Suyash Vashishth made me")








menubar.add_cascade(label="Options", menu=submenu)
submenu.add_command(label="Help", command=help)
submenu.add_command(label="About Brian", command=abrian)
submenu.add_command(label="Exit", command=exit)





root.title("BRIAN VOICE ASSISTANT")
root.geometry('550x650+300+10')
root.iconbitmap("res/images/icon.ico")


########### Variables #######################

eentry=StringVar()


######################################









def takeCommand():

	r = sr.Recognizer()
	with sr.Microphone() as source:
		speak("Listening")

		r.pause_threshold = 1
		audio = r.listen(source)



	try:
		speak("Recognizing")

		query = r.recognize_google(audio, language='en-in')
		speak("Done")
		statusbar['text']= f"User said: {query}\n"


	except Exception as e:


		speak("Say that again please!")
		return "None"
	return query

def sendEmail(to, content):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.login('youremail', 'youremailpassword')
	server.sendmail('youremail', to, content)
	server.close()

def talk():

    t1 = threading.Thread(target=tlk)
    t1.start()





def tlk():

    if 1:

        query = takeCommand().lower()

		#logic for task



        if 'search' in query:
            speak("searching...")
            querys = query.replace("search", "")

            results = wikipedia.summary(f"{querys}\n", sentences=1)
            #results = wikipedia.page(f"{querys}\n")
            speak("Search Completed")
            speak(results)
            print(results)
            speak("want to know more ?")
            query = takeCommand().lower()

            if 'yes' in query:
                speak("searching...")
                results = wikipedia.summary(f"{querys}\n", sentences=4)
                speak("Search Completed")
                speak(results)
                speak("still curious , let me open wikipedia for you !")
                webbrowser.open(f"https://www.wikipedia.org/wiki/{querys}\n")


            else:
                pass





        elif 'how are you' in query:
            speak("I am fine, thank you")



        elif 'task' in query:
            speak("I can do following things")

            speak("send emails,book cab (site open), open instagram, facebook, google, youtube, twitter, stackoverflow")
            speak(" ask me anything by saying , search and i will tell you info about it")
            speak("i can also search on google and youtube")
            speak("i can open apps like microsoft word, excel, powerpoint and notepad and vlc")
            speak("i can also play music")




        elif 'on youtube' in query:
            queryy = query.replace("on youtube", "")
            webbrowser.open(f"https://www.youtube.com/results?search_query={queryy}\n")



        elif 'on google' in query:
            queryg = query.replace("on google", "")
            webbrowser.open(f"https://www.google.com/search?client=chrome-b-d&q={queryg}\n")

        elif 'latest news' in query:
            queryn = query
            webbrowser.open(f"https://www.google.com/search?client=chrome-b-d&q={queryn}\n")

        elif 'what is your name' in query:
            speak("My name is Brian ")



        elif 'who are you' in query:
            speak("I am Brian, a virtual assistant, made for you")

        elif 'who is your father' in query:
            speak("Mr. Suyash made me")

        elif "origin" in query:
            speak("I am Brian, a virtual assistant made in India")

        elif 'book cab' in query:
            speak("Choose company, OLA or UBER")
            query = takeCommand().lower()

            if 'ola' in query:
                speak("Opening OLA cabs")
                webbrowser.open("https://www.olacabs.com/")

            elif 'uber' in query:
                speak("Opening UBER cabs")
                webbrowser.open("https://www.uber.com/in/en/")
            else:
                pass







        elif 'open youtube' in query:
            speak("Now opening Youtube")
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            speak("Now opening Google")
            webbrowser.open("https://www.google.com")

        elif 'play music' in query:
            speak("Now Playing Music, enjoy !")
            music_dir = glob.glob("res\\music\\*.mp3")
            print(music_dir)


            os.startfile(random.choice(music_dir))

        elif 'open stackoverflow' in query:
            speak("Now opening Stackoverflow")
            webbrowser.open("https://www.stackoverflow.com")

        elif 'open facebook' in query:
            speak("Now opening Facebook")
            webbrowser.open("https://www.facebook.come")

        elif 'open twitter' in query:
            speak("Now opening Twitter")
            webbrowser.open("https://twitter.com/explore")


        elif 'open instagram' in query:
            speak("Now opening Instagram")
            webbrowser.open("https://www.instagram.com/?hl=en")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open vlc' in query:
            speak("Now opening VLC")
            vlcPath ="C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"
            os.startfile(vlcPath)

        elif 'open paint' in query:
            speak("Now opening PAINT")
            paintpath ="C:\WINDOWS\system32\\mspaint.exe"
            os.startfile(paintpath)

        elif 'you are great' in query:
            speak("Thank you    sir")

        elif 'hello' in query:
            speak("Hi, good to see you sir")

        elif 'open notepad' in query:
            speak("Now opening Notepad")
            notePath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(notePath)

        elif 'snipping tool' in query:
            speak("Now opening Snipping tool")
            snippath ="C:\\WINDOWS\\system32\\SnippingTool.exe"
            os.startfile(snippath)



        elif 'open chrome' in query:
            speak("Now opening Chrome")
            chromepath ="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromepath)

        elif 'open word' in query:
            try:

                wordpath = "C:\\Program Files (x86)\\Microsoft Office\\Office15\\WINWORD.exe"
                speak("Now opening Word")
                os.startfile(wordpath)
            except:
                wordpath2 = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.exe"
                speak("Now opening Word")
                os.startfile(wordpath2)

        elif 'open excel' in query:
            try:

                excelpath = "C:\\Program Files (x86)\\Microsoft Office\\Office15\\EXCEL.exe"
                speak("Now opening Excel")
                os.startfile(excelpath)
            except:
                excelpath2 = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.exe"
                speak("Now opening Word")
                os.startfile(excelpath2)

        elif 'open powerpoint' in query:
            try:

                powerpointpath = "C:\\Program Files (x86)\\Microsoft Office\\Office15\\POWERPNT.exe"
                speak("Now opening powerpoint")
                os.startfile(powerpointpath)
            except:
                powerpath2 = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.exe"
                speak("Now opening Word")
                os.startfile(powerpath2)



        elif 'send email' in query:


            try:
                to = eentry.get()

                if to =="":
                    speak("please enter a email")
                    speak("don't know where to enter email ? , tap on the 3 blue line top left corner, and fill the email block")
                else:
                    speak("Now sending Email")
                    to = eentry.get()
                    speak("What should I say?")
                    content = takeCommand()
                    sendEmail(to, content)
                    speak("Email sent successfully !")

            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")

        else:
            speak("please give command from command list , see readme manual ")



#####################################


############## TOP FRAME ####################################

Topframe = Frame(root)
Topframe.place(x=80,y=10,height=150, width=420)

brian = Label(Topframe, text="Brian", font=("Agency FB", 55, "bold"), fg="red")
brian.grid(row=0, column=1, padx=180)

subtitle = Label(Topframe, text="Voice Assistant",fg="black", font=("Agency FB", 30, "bold"))
subtitle.grid(row=1,column=1, padx=0)







################### MID FRAME ###############################

Midframe = Frame(root)
Midframe.place(x=80,y=180,height=280, width=420)

mic = PhotoImage(file="res\images\mic.png")



talk = Button(Midframe,image=mic, bd=0, command=talk)
talk.grid(row=0,column=1, padx=110, pady=10)

############## Side frame ##################################

def menui():
    side.place(width=300)
    more.place(x=200)


incd = False
def inc():
    global incd

    if incd:
        global labelx
        global receiver
        global ementry
        if labelx == True:

            side.place(width=90)
            more.place(x=1)

            receiver.place_forget()
            ementry.place_forget()
            incd = False
        else:
            side.place(width=90)
            more.place(x=1)

            incd = False


    else:
        side.place(width=300)
        more.place(x=200)
        receiver = Label(side, text="Receiver Email",font=("times new roman", 18, "bold"))
        receiver.place(x=70, y=150)

        ementry = Entry(side, textvariable = eentry ,font=16)
        ementry.place(x=50, y=200, width=200)


        labelx =True

        incd = True





side = Frame(root,bd=5,relief=GROOVE)
side.place(x=0,y=0, height=650, width=90)
side.tkraise(aboveThis=Topframe)
side.tkraise(aboveThis=Midframe)

moreimg = PhotoImage(file="res\images\menu.png")

more = Button(side, image=moreimg, command=inc, bd=0)
more.place(y=10,x=1)


################################

statusbar = Label(root, text="Welcome sir", relief=SUNKEN, anchor=W, font='Times 12 italic')
statusbar.pack(side=BOTTOM, fill=X)

#################################################################################################

def on_closing():

    Msg = tkinter.messagebox.askquestion("Confirmation","Do you want to close me ?",icon = 'warning')

    if Msg == 'yes':
        sys.exit()
    else:
        pass
root.resizable(0,0)
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
