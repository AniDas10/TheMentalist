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
import random

#pyttsx3 is the speak engine used by windows
engine = pyttsx3.init('sapi5')
client = wolframalpha.Client('2EXX7V-25AG74LU5P')

# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)

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

#greetMe()
#speak('Hello Ani, Jarvis here')
#speak('Sad to hear about Tony')
#speak('How may i help you?')

def response(q):
    res = []
    query = q
    query = query.lower()
    response_1 = [
    	"You might want to contact someone to talk about it",
    	"There are always people who could be helpful",
    	"Things are never as bad as they seem",
    	"calm down, everything would turn out to be fine in the end"]
    response_2 = [
    	"I am glad we could be of assistance",
    	"That's why we do what we do",
    	"Glad to help you out",
    	"You can always pay us a visit",
    	"We've got your back"]

    if 'low' in query or 'down' in query or 'sad' in query or 'suicide' in query or 'depressed' in query or 'bad' in query:
        res.append(random.choice(response_1))
    elif 'better' in query or 'feel better' in query:
        res.append(random.choice(response_2))

    elif 'what\'s up' in query or 'how are you' in query or 'what are you doing' in query:
        stMsgs = ['Just assisting people however I can', 'Crunching some data about your game progress', 'Planning future sessions']
        res.append(random.choice(stMsgs))

    elif 'appreciate' in query or 'thank you' in query or 'thanks' in query or 'good night' in query or 'stop' in query:
        res.append("I hope i was of some help")
        res.append("Have a great day")


    elif 'hello' in query:
        res.append("Hey! Glad to see you here")

    else:
        query = query
        res.append("Searching ...")
        try:
            try:
                reso = client.query(query)
                results = next(reso.results).text
                #speak("Larvis says :: Umm ?")
                res.append("I couldn't understand your problem")
                res.append("However, i've scraped the internet just for you")
                res.append("Hope you find something relevant")

                res.append(results)
            except:
                results = wikipedia.summary(query, sentences=2)
                res.append('This might be what you needed')
                #speak('Tony thinks what u r looking for is')
                res.append(results)
        except:
            res.append("Sorry I am not an expert")
            res.append("But there are surely some experts you can consult out there")

    # res.append("Could I be of any further assistance ?")
    return res

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
        res = response(query)

    except sr.UnknownValueError:
        speak('Sorry, I didn\'t get you! Do you mind repeating?')
        query = None
        res = 'Sorry, I didn\'t get you! Do you mind repeating?'

    return query, res

"""
while True:
    query = myCommand()
    query = query.lower()
    response_1 = [
    	"Maybe you wanna talk about it?",
    	"Talking about it always helps",
    	"Don't worry, stay positive",
    	"calm down, everything would turn out to be fine in the end"]
    response_2 = [
    	"I am always there for you",
    	"See, i told you",
    	"Glad to help you out",
    	"You can always pay me a visit",
    	"I will always be your friend"]

    if 'low' in query or 'down' in query or 'sad' in query or 'suicide' in query or 'depressed' in query:
        speak(random.choice(response_1))
        speak(random.choice(response_1))
    elif 'better' in query or 'feel better' in query:
        speak(random.choice(response_2))
        speak(random.choice(response_2))

    elif 'what\'s up' in query or 'how are you' in query or 'what are you doing' in query:
        stMsgs = ['Chillin with ma homies', 'Nothing much, just bored', 'Netflix and chill bro']
        speak(random.choice(stMsgs))

    elif 'appreciate' in query or 'thank you' in query or 'thanks' in query or 'good night' in query or 'stop' in query:
        speak("I hope i was of some help")
        speak("Enjoy. Stay Positive")
        sys.exit()

    elif 'hello' in query:
        speak("Yo what\'s up bro ?")
    elif 'girl' in query:
        speak("Yo my bad, what\'s up sis ?")

    else:
        query = query
        speak("Searching ...")
        try:
            try:
                res = client.query(query)
                results = next(res.results).text
                #speak("Larvis says :: Umm ?")
                speak("I couldn't understand your problem")
                speak("However, i've scraped the internet just for you")
                speak("Hope you find something relevant")

                speak(results)
            except:
                results = wikipedia.summary(query, sentences=2)
                speak('Got it bro')
                #speak('Tony thinks what u r looking for is')
                speak(results)
        except:
            speak("Sorry bro, i am not an expert")
            speak("But there are surely some experts out there")
            speak("Lemme guide you to google, search for one maybe?")
            webbrowser.open('www.google.com')

    speak("Anything else ? :")
"""

#print(response("I am feeling better"))