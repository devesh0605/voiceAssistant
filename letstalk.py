import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia


def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()


def hello():
    speak("""Hello I am Jarvis. What can I do for you sir?""")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print("Recognizing")
            query = r.recognize_google(audio, language='en-in')
            print("The command is printed=" + query)
        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"
        return query


def takeQuery():
    hello()
    while (True):
        query = takeCommand().lower()
        if "Hello how are you" in query:
            speak("I am fine")
        elif "open google" in query:
            speak("Opening Google")
            webbrowser.open("www.google.com")
        elif "open GitHub" in query:
            speak("Opening Github")
            webbrowser.open("https://github.com/devesh0605")
        elif "bye" in query:
            speak("Have a nice day Sir")
            exit()
        elif "from wikipedia" in query:
            speak("Checking the wikipedia")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=5)
            print(result)
            speak("According to wikipedia")
            speak(result)
        elif "tell me your name" in query:
            speak("I am jarvis. AI created by Shadows")

if __name__ == '__main__':
    takeQuery()
