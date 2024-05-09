import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize speech recognition and text-to-speech engines
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet():
    speak("Hello! How can I assist you today?")

def get_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {current_time}")

def get_date():
    current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
    speak(f"Today is {current_date}")

def search(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

def main():
    greet()
    while True:
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio)
            print(f"User said: {query}")

            if "hello" in query.lower():
                greet()
            elif "time" in query.lower():
                get_time()
            elif "date" in query.lower():
                get_date()
            elif "search" in query.lower():
                speak("What would you like me to search for?")
                audio = recognizer.listen(source)
                search_query = recognizer.recognize_google(audio)
                search(search_query)
            elif "exit" in query.lower():
                speak("Goodbye!")
                break
            else:
                speak("I'm sorry, I didn't understand that.")

        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

if __name__ == "__main__":
    main()
