import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import pyjokes
# from ecapture import ecapture as ec ----------> not yet installed
import wolframalpha
import json
import requests
import randfacts
from deep_translator import GoogleTranslator

# setting wiki language
wikipedia.set_lang("de")

# initializing the assistant
print('Axel A. wird geladen...')

# confs for pyttsx3
engine=pyttsx3.init()
#voices=engine.getProperty('voices')
engine.setProperty('voice','german')

""" speak (text to speech) """
def speak(text):
    engine.say(text)
    engine.runAndWait()

""" setting wakeword """ # this will be of importance for raspberry pi
def activate(phrase='hallo'):
    try:
        with sr.Microphone() as source:
            r=sr.Recognizer()
            r.adjust_for_ambient_noise(source, duration = 0.5)
            audio = r.listen(source)
            wakeword = r.recognize_google(audio, language='de-DE')
            if wakeword.lower() == phrase:
                return True
            else:
                return False
    except:
        return None

""" greetings """
def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hallo, Guten Morgen")
        print("Hallo, Guten Morgen")
    elif hour>=12 and hour<18:
        speak("Hallo, Guten Tag")
        print("Hallo, Guten Tag")
    else:
        speak("Hallo, Guten Abend")
        print("Hallo, Guten Abend")


""" function to recognize voice and return the text_version of it """
def takeCommand():
    statement=''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Ich höre zu")
        # adjust for ambient noise
        r.adjust_for_ambient_noise(source, duration = 0.5) # wait half a second for adjust_for_ambient_noise() to do its thing
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio, language='de-DE')
            print(f"Nutzer: {statement}\n")
            return statement.lower()
        except sr.RequestError:
            speak("Entschuldige, ich kann die Google API nicht erreichen...")
        except sr.UnknownValueError:
            speak("Entschuldige, ich verstehe nicht...")


print("Axel A. wird geladen.")
speak("Axel A. wird geladen.")
wishMe()
speak("Ich bin Axel A.; Aktiviere mich indem du Hallo sagst. Sage Stopp, tschüss oder ausschalten, wenn ich mich herunterfahren soll.")

""" Main Function """
#__name__=='__main__'

while True:
    if activate() == True:
        speak("Wie kann ich dir helfen?")
        statement = takeCommand()
        if statement==0:
            continue

        """ Goodbye"""
        if "ausschalten" in statement or "tschüss" in statement or "stop" in statement:
            speak('Axel A. fährt herunter. Hab noch einen schönen Tag!')
            print('Axel A. fährt herunter. Hab noch einen schönen Tag!')
            exit()


        """ Skills """
        if 'wikipedia' in statement: # wikipedia
            speak('Suche auf Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("Laut Wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in statement: # youtube
            webbrowser.open_new_tab("https://www.youtube.com")  # TO-DO: play yt
            speak("youtube wird geöffnet")
            #time.sleep(5)

        elif 'google' in statement:  # google search
            speak("Wonach soll ich suchen?")
            keyword = takeCommand()
            if keyword != '':
                url = "https://google.com/search?q=" + keyword
                speak("Hier sind Suchergebnisse für " + keyword)  # TO-DO: read hits
                webbrowser.open(url)
                #time.sleep(5)

        elif 'gmail' in statement: # opens gmail
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail wird geöffnet")
            #time.sleep(5)

        elif 'wetter' in statement: # weather for given city
            api_key="XXX"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("nenne den Namen der Stadt")
            city_name=takeCommand()
            complete_url=base_url+"lang=de&appid="+api_key+"&q="+city_name  #for description in german lang=de& added
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Die Temperatur in Grad Celsius beträgt " +
                      str(round(float(current_temperature - 273.15),2)) +
                      "\n die Luftfeuchtigkeit in Prozent beträgt " +
                      str(current_humidiy) +
                      "\n Beschreibung  " +
                      str(weather_description))
                print(" Die Temperatur in Grad Celsius beträgt " +
                      str(round(float(current_temperature - 273.15),2)) +
                      "\n die Luftfeuchtigkeit in Prozent beträgt " +
                      str(current_humidiy) +
                      "\n Beschreibung = " +
                      str(weather_description))
            else:
                speak(" Stadt wurde nicht gefunden ")

        elif 'neuigkeiten' in statement or 'nachrichten' in statement:                       # TO-DO: read headlines
            news = webbrowser.open_new_tab("https://www.welt.de/newsticker/")
            speak('Hier sind einige Schlagzeilen von Welt.de')
            #time.sleep(6)

        elif 'wer bist du' in statement or 'was kannst du' in statement: # who are you
            speak('Ich bin Axel A., ein Sprach Assistent. Ich kann bisher Sachen wie'
                  'youtube öffnen, auf google suchen, gmail öffnen, die Zeit ansagen, wikipedia durchforsten, das Wetter ansagen' 
                  'Schlagzeilen anzeigen, Witze oder einen Fakt erzählen, einen Wecker stellen,'
                  'das Radio abspielen,'
                  'und du kannst mir Mathe oder Erdkunde Aufgaben stellen')

        elif 'bist du ein spion' in statement: # are you a spy
            speak('das darf ich dir nicht sagen. das eff bie ei wurde informiert.')

        elif "wer hat dich gemacht" in statement or "wer hat dich programmiert" in statement: #who made you
            speak("ich wurde von Daniel geschrieben")
            print("ich wurde von Daniel geschrieben")

        elif 'frage' in statement: #asking Wolfram Alpha
            speak('stelle deine Frage. Ich kann mathematische und geografische Fragen beantworten.')
            question=takeCommand()
            app_id = "XXX"
            client = wolframalpha.Client(app_id)
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif 'bist du dabei' in statement:
            speak('Axel A. ist auch dabei')
            print('Axel A. ist auch dabei')

        elif 'wie geht es dir' in statement: # how are you
            speak('danke, gut!')
            speak('und wie geht es dir?')
            print('danke, gut!')
            print('und wie geht es dir?')
            answer = takeCommand()
            if 'nicht' not in answer:
                speak('das ist schön')
                print('das ist schön')
            else:
                speak('möchtest du darüber reden?')
                print('möchtest du darüber reden?')
                answer2 = takeCommand()
                if "ja" in answer2 or "vielleicht" in answer2:
                    speak("Ich höre dir zu.")
                else:
                    speak("melde dich, wenn ich dir helfen kann.")

        elif 'uhr' in statement or 'uhrzeit' in statement or 'wie spät' in statement: # states time
            strTime=datetime.datetime.now()
            speak("die Uhrzeit ist %d Uhr %d und %d Sekunden" %(strTime.hour, strTime.minute, strTime.second))

        elif 'witz' in statement:
            joke = pyjokes.get_joke("de", "all")
            speak(joke)
            print(joke)

        elif "pause" in statement or "hör nicht zu" in statement: # Pauses for time given
            speak("wie viele Sekunden soll ich nicht zuhören?")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif "fakt" in statement or "erzähl etwas" in statement or "random fact" in statement:      # Random Facts (only english available)
            fact = randfacts.getFact(False)
            fact = GoogleTranslator(source='auto', target='de').translate(x) # translating to german
            speak(fact)
            print(fact)

        elif "radio" in statement: # plays radio
            speak("Radio wird abgespielt")
            webbrowser.open_new("https://wdr-edge-301f-fra-ts-cdn.cast.addradio.de/wdr/cosmo/live/mp3/128/stream.mp3")

        elif "alarm" in statement or "wecker" in statement: # set up an alarm 
            speak("Auf wann soll ich einen Wecker stellen?")
            alarm_time = takeCommand()
            alarm_time = alarm_time.replace(" uhr", "")
            today = datetime.datetime.today()
            alarm_time = datetime.datetime.strptime(alarm_time, '%H:%M').replace(year=today.year,month=today.month,day=today.day)
            now = datetime.datetime.now()
            print(alarm_time)
            print(now)
            time.sleep((alarm_time - now).total_seconds()) #this causes the v.assistant to sleep, need a better solution
            print("AUFSTEHEN!")
            speak("Alarm! Aufstehen!")
            
        #elif "camera" in statement or "take a photo" in statement:
        #    ec.capture(0,"robo camera","img.jpg")                  # no camera yet



