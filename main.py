import speech_recognition as sr
import pyttsx3
import keyboard
import simpleaudio as sa
import time

r = sr.Recognizer()

def play_sound_effect(file_path):
        wave_obj = sa.WaveObject.from_wave_file(file_path)
        play_obj = wave_obj.play()
        play_obj.wait_done()

class Listener():
    def __init__(self):
        while True:
            self.text = ""
            self.listen_for_x()

    def listen_for_x(self):
        print("Press 'X' to start recording...")
        keyboard.wait('x')
        self.record_text()
        self.output_text()

    def record_text(self):
        while True:
            try:
                with sr.Microphone() as source:
                    print("Listening...")
                    play_sound_effect('src/radio_on.wav')  # ON
                    r.adjust_for_ambient_noise(source, duration=0.2)
                    audio = r.listen(source)

                    play_sound_effect('src/radio_off.wav') # OFF
                    self.text = r.recognize_google(audio, language="fr-FR")
                    return self.text
            except sr.RequestError as e:
                print("Could not request results: {0}".format(e))
            except sr.UnknownValueError:
                print("Unknown error occurred")

    def output_text(self):
        utf8_text = self.text.encode('utf-8').decode('utf-8')
        Speaker(utf8_text)

class Speaker():
    def __init__(self, text):
        self.text = text
        self.decode_speech()

    def decode_speech(self):
        self.text = self.text.lower()

        otan_alphabet = ['alpha', 'bravo', 'charlie', 'delta', 'écho', 'foxtrot', 'golf', 'hotel', 'india', 'juliette', 'kilo', 'lima', 'mike', 'novembre', 'november', 'oscar', 'papa', 'québec', 'roméo', 'sierra', 'tango', 'uniform', 'victor', 'whiskey', 'x-ray', 'yankee', 'zulu']
        
        callsign = ""
        for letter in self.text.split():
            if letter in otan_alphabet:
                callsign += letter + " "
                play_sound_effect('src/answers/' + letter + '.wav')
                time.sleep(0.3)

        print(callsign.strip())

        # vfr aviation phraseologie
        if "bonjour" in self.text:
            play_sound_effect('src/answers/bonjour.wav')
        elif "paramètres" in self.text:
            play_sound_effect('src/answers/paramètres_vol.wav')
        elif "personnes" in self.text:
            play_sound_effect('src/answers/clearance_taxi.wav')
        elif "point" and "d'attente" in self.text:
            play_sound_effect('src/answers/aligner_clearance.wav')
        elif "décollage" in self.text:
            play_sound_effect('src/answers/décollage_clearance.wav')
                              

if __name__ == "__main__":
    Listener()
