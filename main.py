from playsound import playsound
from deep_translator import GoogleTranslator
from gtts import gTTS

from lanugages import dic
from take_voice_input import take_voice_input
flag = 0


# query = take_voice_input()
# while query == "None":
#     query = take_voice_input()
query = "Tarun is a bot"

def destination_language():
    print(
        """Enter the language in which you 
	want to convert : Ex. Hindi , English , etc."""
    )
    # some comment

    # Input destination language in
    # which the user wants to translate
    to_lang = take_voice_input()
    while to_lang == "None":
        to_lang = take_voice_input()
    to_lang = to_lang.lower()
    return to_lang


# to_lang = destination_language()
to_lang = "telugu"

# Mapping it with the code
while to_lang not in dic:
    print(
        """Language in which you are trying
to convert is currently not available , 
please input some other language"""
    )
    print()
    to_lang = destination_language()

to_lang = dic[dic.index(to_lang) + 1]


# invoking Translator
# translator = Translator()
translator = GoogleTranslator(source="auto", target=to_lang)


# Translating from src to dest
text_to_translate = translator.translate(query, dest=to_lang)

text = text_to_translate

# Using Google-Text-to-Speech ie, gTTS() method
# to speak the translated text into the
# destination language which is stored in to_lang.
# Also, we have given 3rd argument as False because
# by default it speaks very slowly
speak = gTTS(text=text, lang=to_lang, slow=False)

# Using save() method to save the translated
# speech in capture_voice.mp3
speak.save("captured_voice.mp3")

# Using OS module to run the translated voice.
playsound("captured_voice.mp3")
# os.remove("captured_voice.mp3")

# Printing Output
print(text)
