import speech_recognition as sr

# Capture Voice
# takes command through microphone
def take_voice_input():
    r = sr.Recognizer()
    print("Recognizer created")
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language="en-in")
        print(f"The User said {query}\n")
    except Exception as e:
        print("say that again please.....")
        return "None"
    return query
