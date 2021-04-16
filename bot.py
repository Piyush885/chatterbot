def ask_bot():
    query = textF.get()
    query=str(query)
    if "hi" in query or "hii" in query:
        msgs.insert(END,"you :" + str(query))
        msgs.insert(END,"bot:" + "hello sir")
        speak("hellooo sirrr   I am a robot and here to help youuu")
        textF.delete(0,END)
        msgs.yview(END)
    elif "good morning" in query or "gm" in query or "morning" in query:
        msgs.insert(END,"you :" + str(query))
        msgs.insert(END,"bot:" + "good morning sir")
        speak("good morning sir")
        textF.delete(0,END)
        msgs.yview(END)
    elif "good afternoon" in query or "ga" in query or "afternoon" in query:
        msgs.insert(END,"you :" + str(query))
        msgs.insert(END,"bot:" + "good afternoon sir")
        speak("good afternoon sir")
        textF.delete(0,END)
        msgs.yview(END)
    elif "good night" in query or "gn" in query or "night" in query:
        msgs.insert(END,"you :" + str(query))
        msgs.insert(END,"bot:" + "good night sir")
        speak("good night sir")
        textF.delete(0,END)
        msgs.yview(END)
        
    elif "wikipedia" in query:
        query=query.replace("wikipedia","")
        results=wikipedia.summary(query,sentences=2)
        msgs.insert(END,"you :" + (query))
        msgs.insert(END,"bot :" + str(results))
        textF.delete(0,END)
        msgs.yview(END)
    elif "youtube" in query:
        webbrowser.open('youtube.com')
        textF.delete(0,END)
        msgs.yview(END)
    elif "google" in query:
        webbrowser.open('google.com')
        textF.delete(0,END)
        msgs.yview(END)
    elif "time" in query:
        t=datetime.datetime.now().strftime("%H:%M:%S")
        msgs.insert(END,"you :" + str(query))
        msgs.insert(END,"bot:" + t)
        textF.delete(0,END)
        msgs.yview(END)
    elif "date" in query:
        d=date.today().strftime("%D:%M:%Y")
        msgs.insert(END,"you :" + str(query))
        msgs.insert(END,"bot:" + d)
        textF.delete(0,END)
        msgs.yview(END)
        
    else:    
        query=textF.get()
        ans_from_bot=bot.get_response(query)
        msgs.insert(END,"you :" + str(query))
        msgs.insert(END,"bot:" + str(ans_from_bot))
        textF.delete(0,END)
        msgs.yview(END)
import os
import tkinter as tk
from tkinter import *
from tkinter import PhotoImage
from chatterbot import preprocessors
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import wikipedia
import os
import pyttsx3
import datetime
from datetime import date
import webbrowser
import logging
import speech_recognition as sr
logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)
engine = pyttsx3.init('sapi5')
voice= engine.getProperty('voices') #getting details of current voice
engine.setProperty('voice', voice[1].id)
def speak(audio):
    engine.say(audio) 
    engine.runAndWait()        
           
bot=ChatBot("my bot")
convo=[
    "hello",
    "hi",
    "what is your name",
    "my name is bot",
    "how are you",
    "I am fine",
    "who made you",
    "made by Piyush Rai",
    "byy",
    "byy sir",
    "bot byy",
    "byy sir",
    "byy bot",
    "byy sir"
    ]
trainer=ListTrainer(bot)
trainer.train(convo)
main = tk.Tk()
main.geometry("500x650")
main.title("my chatbot")
img=PhotoImage(file="jason-leung-1DjbGRDh7-E-unsplash (1).png")
photoL=Label(main,image=img)
photoL.pack(pady=5)
frame=Frame(main)
sc=Scrollbar(frame)
msgs=Listbox(frame,width=80,height=20,yscrollcommand=sc.set)  
sc.pack(side=RIGHT,fill=Y)
msgs.pack(side=LEFT,fill=BOTH,pady=10)
frame.pack()
#creating text field
textF=Entry(main,font=("Verdana",20),borderwidth=10,relief=SUNKEN)
textF.pack(fill=X,pady=10)
btn=Button(main,text="Ask from Bot",font=("bold",10),command=lambda:ask_bot())
btn.pack()
def enter_function(event):
    btn.invoke()
main.bind('<Return>',enter_function)
btn2=Button(main,text="Help",font=("bold",10),bg="grey",borderwidth=10,relief=SUNKEN,command=lambda:helpbot() )
btn2.pack()
def helpbot():
    root=tk.Tk()
    root.geometry("800x800")
    l1=Label(root,text='''This robot is made by Piyush Rai.\n
    This is a helping robot.\n you can communicate with him using text commands. \n
    You can start conversation by greeting him like hii,hello,good morning,gm,good afternoon and can end convertation by typing byy
    \n You can press enter button or use vitural button to process your command
    \n Ask his name.He will reply you and ask "how are you"\n
    \n If you want to get any inforormation from robot just use these words in your conversation \n
    wikipedia search----wikipedia\n
    opening google---google\n
    opening youtube---youtube\n
    getting time or date---time or date\n
    The robot is in learning phase.Please share your feedback so that we can improve him'''
    )
    l1.pack()
    
    root.mainloop()

main.mainloop()
