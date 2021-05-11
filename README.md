# Axel A. - A German Voice Assistant
This is a work-in-progress __voice assistant__ (named ___Axel A.___) built with Python.

### Capabilities

The voice assistant is activated through the wake word ___hallo___, and is currently capable of performing the following tasks:

1. __Read__ first paragraph of __wikipedia__ search results (User: _"suche Berlin auf Wikipedia"_),
2. state __weather information__: (User: _"Wie ist das Wetter?"_ Axel A.: _"nenne den Namen der Stadt"_),
3. __answer mathematical or geographical questions__ through the Wolfram Alpha API (User: _"Ich habe eine Frage"_ Axel A.: _"stelle deine Frage. Ich kann mathematische und geografische Fragen beantworten."_),
4. state the __current time__ (User: _"Wie spät ist es/ Nenne die Uhrzeit/ Wieviel Uhr?"_),
5. tells __random facts__ (User: _"Sag mir einen Fakt/ Erzähl etwas"_),
6. tells __jokes__ (User: _"Erzähle einen Witz."_),
7. plays the __radio__ (User: _"spiele Radio"_),
8. sets an __alarm clock__ (User: _"Stelle einen Wecker/Alarm"_),
9. opens __news__ in a new tab (User: _"Zeige Nachrichten/Neuigkeiten"_),
10. opens __Google__ (User: _"google"_ Axel A.: _"Wonach soll ich suchen?"_),
11. opens __GMail__ (User: _"öffne GMail"_),
12. opens __YouTube__ (User: _"öffne Youtube"_),
13. __pauses listening__ for a given time (User: _"Pause/hör nicht zu"_ Axel A: _"wie viele Sekunden soll ich nicht zuhören?"_),
14. and responds to questions such as _who are you?_ (_"wer bist du?"_), _what are you capable of?_ (_"was kannst du?"_), _how are you?_ (_"wie geht's dir?"_), _are you a spy?_ (_"bist du ein Spion?"_), and _who made you?_ (_"wer hat dich gemacht?"_).

### Usage

- Create a folder (e.g. 'voice_assistant') on your computer. Open it in VSCode.

- in the terminal, set up a virtual environment:
create:
```python3 -m venv venv```
activate:
```source venv/bin/activate```

- Install dependencies:
```pip install -r requirements.txt```
    
- Run main.py
```python main.py```
    
- wait for Axel A. to boot

![image](https://user-images.githubusercontent.com/71432794/117809679-bfd4db00-b25e-11eb-9577-d9dadfa9b661.png)

### Libraries used

1. speech_recognition
2. pyttsx3
3. datetime
4. wikipedia
5. webbrowser
6. os
7. time
8. subprocess
9. pyjokes
10. wolframalpha
11. json
12. requests
13. randfacts
14. deep_translator

#### APIs

1. Open Weather Map
2. WolframAlpha

### Sources/ links

1. ___How to build your own AI personal assistant using Python___: https://towardsdatascience.com/how-to-build-your-own-ai-personal-assistant-using-python-f57247b4494b
2. ___How to build your own Python Voice Assistant___: https://itnext.io/how-to-build-your-own-python-voice-assistant-thecodingpie-eaa1f70aabb6
3. ___The ultimate guide to speech recognition with Python___: https://realpython.com/python-speech-recognition/
4. ___Building A Simple Voice Assistant for Your Mac in Python___: https://towardsdatascience.com/building-a-simple-voice-assistant-for-your-mac-in-python-62247543b626
