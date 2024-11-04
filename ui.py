import os 

from deep_translator import GoogleTranslator
from playsound import playsound
import flet as ft
from gtts import gTTS
from lanugages import dic
from take_voice_input import take_voice_input


def main(page: ft.Page):
    def toggle_recording(_):
        value = languages_drop_down.value
        if value is None:
            return

        recording_icon.disabled = False
        recording_icon.update()
        page.update()

    def record_voice(_):
        query = take_voice_input()
        while query == "None":
            query = take_voice_input()

        to_lang = languages_drop_down.value

        if to_lang is None:
            return ## TODO: Show error message
        text = translate_text(query, to_lang.strip().lower())
        speak_text(text, to_lang)
        page.update()

    recording_icon = ft.IconButton(
        icon="mic",
        on_click=record_voice,
        disabled=True,
    )

    languages_drop_down = ft.Dropdown(
        on_change=toggle_recording,
        options=[ft.dropdown.Option(k) for k in dic],
    )

    page.add(recording_icon, languages_drop_down)


def translate_text(query, to_lang):
    translator = GoogleTranslator(source="auto", target=to_lang)
    text_to_translate = translator.translate(query, dest=to_lang)
    return text_to_translate


def speak_text(text: str, to_lang: str):
    print(f"Speaking {text} in {to_lang}")
    tts = gTTS(text=text, lang=to_lang, slow=False)
    audio_file = os.path.dirname(__file__) + '\\audio.mp3'
    tts.save(audio_file)
    playsound(audio_file)

ft.app(target=main)
