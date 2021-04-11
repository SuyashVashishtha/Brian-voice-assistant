# Welcome to Brian Voice Assistant Readme.

Brian is a Voice assistant made in Python using various Modules. It primarily based on 
Tkinter GUI and Speech Recognition Module

Brian is made for **Windows Only** and requires an Internet Connection to work Properly and 
on its full intent.

## Requirments 

Brian requires many modules such as Tkinter and Speech Recognition.
Most of these Modules can be installed with pip commands but some of them
may need Pycharm IDE.

Below is a list of Modules required to run Brian.

1. pyttsx3

2. pywin32

3. pywintypes

4. requests

5. speech_recognition as sr

6. wikipedia

7. webbrowser

8. smtplib

9. pyaudio


## Email Function

User can Send Emails with Brian using a special Command _Send email_

But first, you need to set up it.

**At line 135 you will find sendEmail Function. In there replace:-**

> youremail with your email address you wish to send an email with
> yourpassword with your respective password. (don't worry your password won't be sent to us or anyone. It is completely safe)

**To successfully send emails first enable an option in Gmail securities :-**

>Acess to less secure apps (important)

**And obviously Internet access is important**


## Features

_if you don't want to read all features just go to Brian and say **task** and it will tell
you everything he can do_

1. Send emails to described person.	
2. Open programs like Word, PowerPoint, Excel, Notepad, Vlc	
3. Open sites like Google, Facebook, Instagram, Youtube, Twitter and StackOverflow	 
4. Can make searches on Google and Youtube 
5. Can search the information and tell you of the thing you asked 
6. Can play music (for playing your music, put your music files in res\music )	     
7. Can book cabs (site open)	     						             
8. Tell time									     
9. Answer some questions


## Usage

To search something just say- search (topic)
To search something on google,say - (topic) on google
To Search for something on youtube, say - (topic) on youtube


# Note

## **After you press the mic button, brian will say listening, wait for 1 sec, and then pull the command**
