import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import datetime
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)

engine.setProperty('voice' , voices[1].id, )
engine.setProperty('rate' , 178 )

#this fuction is created for speak in the program
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    

#This fuction is for created for wishing on different times
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        speak("Good morning  sir! ")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir! ")
    else:
        speak("Good morning sir! ")

    speak("i am alexa sir please tell me how may i help you! ")

#this function is for taking command by microphone from the user and return string output

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listing....")
        r.pause_threshold = 0.8

        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language="en-US" )
        print(f"user said: {query}\n")

    except Exception as e:
        # print(e)

        speak("say that again please sorry!")
        return "None"
    return query

#for running this function successflly you'll have to allow less secure appps in your google account otherwise this funtion will not work
def sendEmail(to , content):
    server = smtplib.SMTP("smtpl.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("yourgmail@gmail.com","you password")
    server.sendmail("youremail@gamil.com",to , content)
    server.close()






if __name__ == '__main__':
    # speak("Ali is  a good boy")
    wishMe()
    while True:
        query = takecommand().lower()

    #logic for execution tasks based on query
        if "wikipedia" in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia...")
            print(results)
            speak(results)
        
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open facebook" in query:
            webbrowser.open("facebook.com")
        elif "open netflix" in query:
            webbrowser.open("netflix.com")
        elif "open twitter" in query:
            webbrowser.open("twitter.com")
        elif "open stackoverflowr" in query:
            webbrowser.open("stackoverflow.com")

        elif "play music" in query:
            music_dir = "d:\\New folder\\favorite songs"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif"the time" in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strtime}")

        elif "open code" in query:
            codepath = "C:\\Users\\Al Hafiz Enterprises\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif "email to Ali" in query:
            try:
                speak("What should i say..")
                content = takecommand()
                to = "abdulrehman76261@gmail.comm"
                sendEmail(to , content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("sorry sir i am not able to send email i don't where is the problem i try my best sorryy")

        elif "goodbye" in query:
            speak("okay sir bye for now i'm always avaiable for you call me anytime")
            exit()
