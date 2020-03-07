import pyttsx3 
import webbrowser   #for opening youtube/google
import smtplib  #for email
import random   #making random choices
import speech_recognition as sr
import wikipedia    #searching wikipedia results
import datetime
import wolframalpha     #API for executing 90% queries
import os 
import sys

#pyttsx3 is the speak engine used by windows
engine = pyttsx3.init('sapi5')
client = wolframalpha.Client('2EXX7V-25AG74LU5P')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    print('Jarvis :: '+ audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon')

    if currentH >= 18 and currentH < 24:
        speak('Good Evening')
    
greetMe()
speak('Hello Ani, Jarvis here')
#speak('Sad to hear about Tony')
speak('How may i help you?')

def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:     #Microphone is now active
        print('Listening :: ')
        r.energy_threshold = 3000   #Energy level above which sound will be accepted
        r.pause_threshold = 0.8       #  time pause after speaking
        audio = r.listen(source)    # audio stores the users command
        #audio = r.record(source) also works but usually used when we want to record something
        #with some specified duration, by default it records till no more audio input is there
    try:                            #if query is successful then print user query
        query = r.recognize_google(audio, language='en-in')
        print("User :: " + query + '\n')
    
    except sr.UnknownValueError:
        speak('Sorry Ani, didn\'t get you! Do u mind typing it down?')
        query = str(input("Type it here :: "))

    return query

while True:
    query = myCommand()
    query = query.lower()

    if 'open youtube' in query:
        speak('Opening Youtube in a second !')
        webbrowser.open('www.youtube.com')
    elif 'open google' in query:
        speak('Opening Google in a second !')
        webbrowser.open('www.google.com')
    elif 'open monkey accounts' in query:
        speak('Opening Monkey Accounts Application in a second !')
        webbrowser.open('www.monke.herokuapp.com')
    
    elif 'what\'s up' in query or 'how are you' in query or 'what are you doing' in query:
        stMsgs = ['Chillin with ma homies', 'Nothing much, just bored', 'Netflix and chill bro']
        speak(random.choice(stMsgs))

    elif 'bye-bye' in query or 'abort' in query or 'good night' in query or 'stop' in query:
        speak("Sure Bye Bye")
        speak("Hope you have a good day")
        sys.exit()
    
    elif 'hello' in query:
        speak("Yo what\'s up bro ?")

    else:
        query = query
        speak("Searching ...")
        try:
            try:
                res = client.query(query)
                results = next(res.results).text
                #speak("Larvis says :: Umm ?")
                speak("Got it bro")
                speak(results)
            except:
                results = wikipedia.summary(query, sentences=2)
                speak('Got it bro')
                #speak('Tony thinks what u r looking for is')
                speak(results)
        except:
            speak("Sorry bro, google it for yourself")
            webbrowser.open('www.google.com')

    speak("Anything else ? :")