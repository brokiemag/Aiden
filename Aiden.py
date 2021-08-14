'''Note:-Aiden won't or maynot work elif earphones/headset are not plugged in 
stuck at listening try pluging in earphones else speak loudly 
or kill terminal and run again it may take few seconds to recognize 
it will only work for english language
i have some issues regarding this issues IDK how to fix but the common reason is 
the noise in the surroundings try to reduce the noise in the background'''
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime
from datetime import date
import urllib3
import wolframalpha
import os
import camera
import time
import random
import subprocess
import pyaudio
from GoogleNews import GoogleNews
import pyjokes
import pywhatkit as kit
from requests import get
import requests
from serpapi import GoogleSearch
import folium
import pyautogui as p
import urllib.request
import time
from selenium import webdriver
from time import sleep
from pywikihow import search_wikihow
import cv2
import pywhatkit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# wishme (regular greetings according to the time )


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour >= 0 and hour <= 12:
        speak(f"good morning, its {tt}")
    elif hour >= 12 and hour <= 18:
        speak(f"good afternoon, its {tt}")
    else:
        speak(f"good evening, its {tt}")
    speak("I am AIDEN . Please tell me how may i help you")

# voice input


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def TaskExecution():
    cam.release
    cv2.destroyAllWindows()
    speak("verification successful")
    speak("Welcome Back Sohan")
    wish()
    while True:
        query = takeCommand().lower()
# search/order_commands
        if "who" in query or "what" in query:
            speak('Searching Wikipedia...')
            query1 = query.replace("wikipedia", "")
            result = wikipedia.summary(query1, sentences=2)
            speak("According to wikipedia")
            speak(result)
        elif"where is my phone" in query or "find my phone" in query:
            speak("tracking it down right now")
            webbrowser.open(
                "https://www.google.com/android/find?u=0&utm_source=Google&utm_medium=onebox")
        elif "i am hungry" in query or "i am felling hungry" in query:
            webbrowser.open("https://www.google.com/search?q=restaurants+near+me")
            speak("here are a list of restaurants near you")
        elif "play a game" in query or "i'm bored" in query or "i am bored" in query or "game" in query:
            speak("Here Is what i Can Play")
            games = "(1)tic tac toe", "(2)PAC-MAN", "(3)Snake", "(4)Solitaire", "(5)Minesweeper", "(6)Fun-Facts ", "(7)Earth Day quiz"
            print(*games, sep="\n")
            speak("what do u want to play")
            play = takeCommand()
            webbrowser.open("https://www.google.com/search?q=play "+play)
            quit()
        elif "play" in query or "sing" in query or "song" in query:
            pla = query.replace('play', '')
            pla1 = pla.replace('song', '')
            kit.playonyt(pla1)
        elif "order" in query or "buy" in query:
            odr = query
            odr = odr.replace("order me a", "")
            webbrowser.open("https://www.amazon.in/s?k=" + odr)
            speak("here is the product from amazon")
        elif "write" in query or "note" in query:
            note = query
            note1 = note.replace('write that', '')
            note2 = note1.replace('note that', '')
            remember = open("data.txt", 'w')
            remember.write(note2)
            remember.close()
            speak("i have noted that" + note2)
        elif "do you have anything " in query:
            remember = open('data.txt', 'r').read()
            speak("you told me to remember that" + remember)
        elif 'joke' in query:
            s = pyjokes.get_joke(language='en', category='all')
            speak(s)
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open(
                "https://www.google.com/maps/place/" + location + "")
        elif "weather" in query:
            speak(" City name ")
            print("City name : ")
            city_name = takeCommand()
            webbrowser.open("https://www.accuweather.com/en/in/" +
                            city_name + "/189231/weather-forecast/189231")
            speak("opening wether forcast")
            speak(city_name)
        elif 'timer' in query or 'stopwatch' in query:
            webbrowser.open("https://www.google.com/search?q="+query)
            timing = query
            timing = timing.replace('set a timer', '')  
            timing = timing.replace('for', '')
            speak(f'I will remind you in {timing}')
        elif 'today' in query:
            speak("It is")
            speak(date.today())
            speak("today")
        elif "movie" in query or "movies" in query:
            binge = "netflix.com", "primevideo.in", "allmoviesforyou.co"
            hel = random.choice(binge)
            webbrowser.open("https://" + hel)
            speak("Here Are A list of Movies")
        elif "message" in query:
            speak("is a text or a file")
            choice = takeCommand()
            if 'text' in query:
                speak("please say the number to which i should send")
                number = takeCommand()
                speak("what should i send")
                message = takeCommand()
                pywhatkit.sendwhatmsg("+91"+number, message, 22, 35)
                p.press('enter')
            if "file" in query:
                driver.get('https://web.whatsapp.com/')
                driver = webdriver.Chrome()
                name = input('Enter the name of user or group : ')
                filepath = input('Enter your filepath (images/video): ')
                input('Enter anything after scanning QR code')
                user = driver.find_element_by_xpath(
                    '//span[@title = "{}"]'.format(name))
                user.click()
                attachment_box = driver.find_element_by_xpath(
                    '//div[@title = "Attach"]')
                attachment_box.click()
                image_box = driver.find_element_by_xpath(
                    '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
                image_box.send_keys(filepath)
                sleep(3)
                send_button = driver.find_element_by_xpath(
                    '//span[@data-icon="send"]')
                send_button.click()
        elif "search" in query:
            speak("what do you want me to search sir")
            search = takeCommand()
            webbrowser.open("https://www.google.com/search?q="+search)
        elif "print" in query:
            speak("what do you want me to print")
            name = takeCommand()
            print = (str("this is what u wanted me to print:-"+name))
        elif "set alarm" in query:
            nn = int(datetime.datetime.now().hour)
            speak("what time do you want please say in twenty four hour format ")
            print("24 Hour Format please say it in hours")
            format = input("please enter here in 24 hrs format:- ")
            if nn == format:
                music_dir = 'C:\\Users\\sohan\\Desktop\\folder\\python\\jarvis intro'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))
# open Apps
        elif "camera" in query:

            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                q = cv2.waitKey(50)
                if q == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()
        elif "mobile camera" in query or "mobile cam" in query or "mor" in query or "my mobile camera" in query:
            import numpy as np
            URl = "http://192.168.43.1:8080/shot.jpg"
            while True:
                img_arr = np.array(
                    bytearray(urllib.request.urlopen(URl).read()), dtype=np.uint8)
                img = cv2.imdecode(img_arr, -1)
                cv2.imshow('IPWebcam', img)
                q = cv2.waitKey(1)
                if q == ord("q"):
                    break
        elif "open" in query:
            hl_str = query
            result1 = hl_str.replace('open', '')
            result2 = result1.replace(' ', '')
            result3 = result2.replace('.com', '')
            webbrowser.open("https://www."+result3+".com")
        elif 'calculator' in query:
            speak("opening calculator")
            subprocess.Popen("C:\\Windows\\System32\\calc.exe")
        elif 'zoom' in query:
            zoomPath = "C:\\Users\\sohan\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
            os.startfile(zoomPath)
        elif 'edge' in query:
            edgePath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            os.startfile(edgePath)
        elif 'visual studio code' in query:
            visualstudiocodePath = "C:\\Users\\sohan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(visualstudiocodePath)
        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S:")
            speak(f"Sir,the time is {strTime}")
            print(f"Sir,the time is {strTime}")
# Expressions/Only Speak Commands
        elif 'change' in query or "edit" in query:
            speak("open code and edit to "+query)
        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Sohan.")
        elif 'wake up' in query or "ready" in query:
            speak("initiating")
            speak("ready sir\n")
        elif 'hello' in query or "hi" in query or "namaste" in query or "vanakkam" in query or "assalam walekum" in query or "hai" in query:
            a = "hello sir", "hi sir", "u say hello,,i am a aglow. i think it is a great start for conversation to flow"
            speak(random.choice(a))
        elif "how are you" in query:
            d = "i am doing great sir", "i am doing great sir what about you"
            speak(random.choice(d))
        elif "well" in query or "great" in query or "good" in query:
            c = "ohh that's great sir", "good to hear that sir"
            speak(random.choice(c))
        elif "what is your age" in query or "how old are you" in query:
            l = "i landed on this planet on 2020! which makes my age 1", "i am 1 year old "
            speak(random.choice(l))
        elif "friends" in query:
            speak("google AI, Alexa,Cortana are my friends well?!, siri of course ")
            speak("they are going to help me in this journey")
        elif "introduce yourself" in query or "who are you" in query or "what do you do" in query:
            music_dir = 'C:\\Users\\sohan\\Desktop\\folder\\python\\Aiden Intro'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[1]))
        elif "how dare" in query:
            speak("so sorry sir")
        elif "thank you" in query:
            speak("my pleasure")
        elif "are you hungry" in query:
            speak("i have a donut")
            print("🍩")
        elif "shut up" in query or "mental" in query or "stupid" in query or "faltu" in query:
            speak("Did I really deserve that?! \n")
            quit()
        elif 'are you mad' in query:
            speak("sry sir\n")
        elif "pets?" in query:
            speak(
                "I don’t have any pets. I used to have a few bugs, but they kept getting squashed.")
# PC_Functions
        elif "restart" in query:
            os.system('shutdown /r')
        elif 'scroll up' in query:
            p.press('up')
        elif 'scroll down' in query:
            p.press('down')
        elif "command prompt" in query:
            os.system('start cmd')
        elif 'left click' in query:
            p.press('left')
        elif 'right click' in query:
            p.press('right')
        elif 'enter' in query:
            p.press('enter')
        elif 'close' in query:
            speak("closing the window")
            p.hotkey('alt', 'f4')
        elif 'minimise' in query:
            speak("minimize the window")
            p.hotkey('Win', 'd')
        elif 'maximize' in query:
            speak("maximizeing windows")
            p.hotkey('Win', 'd')
        elif 'new tab' in query:
            p.hotkey('ctrl', 't')
        elif 'new file' in query:
            p.hotkey('ctrl', 'n')
        elif 'switch the tab' in query or "switch tab" in query or "switch windows" in query:
            p.hotkey('ctrl', 'tab')
        elif 'increase the volume' in query:
            speak('volume increased sir')
            p.hotkey('volumeup')
        elif 'decrease the volume' in query:
            speak('volume reduced sir')
            p.hotkey('volumedown')
        elif 'close' in query:
            speak("closing the window")
            p.hotkey('alt', 'f4')
        elif "stop" in query:
            speak("ok")
            quit()
        elif "shutdown" in query:
            os.system("shutdown /s /t 5")
        elif "restart" in query:
            os.system("shutdown /r /t 5")
        elif "sleep" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        elif 'none' in query:
            speak("")
        else:
            sew = query.replace("search", "")
            webbrowser.open("https://www.google.com/search?q="+sew)

##########################################################################################################################################
##########################################################################################################################################
if __name__=="__main__":

    recognizer = cv2.face.LBPHFaceRecognizer_create() # Local Binary Patterns Histograms
    recognizer.read('trainer/trainer.yml')   #load trained model
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath) #initializing haar cascade for object detection approach
    
    font = cv2.FONT_HERSHEY_SIMPLEX #denotes the font type
    
    
    id = 2 #number of persons you want to Recognize
    
    
    names = ['','Sohan']  #names, leave first empty bcz counter starts from 0
    
    
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW) #cv2.CAP_DSHOW to remove warning
    cam.set(3, 640) # set video FrameWidht
    cam.set(4, 480) # set video FrameHeight
    
    # Define min window size to be recognized as a face
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)
    
    # flag = True
    
    while True:
    
        ret, img =cam.read() #read the frames using the above created object
    
        converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #The function converts an input image from one color space to another
    
        faces = faceCascade.detectMultiScale( 
            converted_image,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH)),
           )
    
        for(x,y,w,h) in faces:
        
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2) #used to draw a rectangle on any image
    
            id, accuracy = recognizer.predict(converted_image[y:y+h,x:x+w]) #to predict on every single image
    
            # Check if accuracy is less them 100 ==> "0" is perfect match 
            if (accuracy < 100):
                id = names[id]
                accuracy = "  {0}%".format(round(100 - accuracy))
                TaskExecution()
    
            else:
                id = "unknown"
                accuracy = "  {0}%".format(round(100 - accuracy))
            
            cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
            cv2.putText(img, str(accuracy), (x+5,y+h-5), font, 1, (255,255,0), 1)  
        
        cv2.imshow('camera',img) 
    
        k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            cam.release
            cv2.destroyAllWindows()
    