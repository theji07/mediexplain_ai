import pyttsx3

def speak_text(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 140)  # Adjust speaking speed
    engine.setProperty('volume', 1.0)  # Max volume
    engine.say(text)
    engine.runAndWait()
