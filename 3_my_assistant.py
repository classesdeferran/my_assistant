import speech_recognition as sr
import pyttsx3

es = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0'
en = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'


def audio_a_texto():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        r.pause_threshold = 0.8

        print("Ya puedes hablar...")

        audio = r.listen(source)

        try:

            text = r.recognize_google(audio, language="es")

            print("Has dicho :", text)

            return text
        
        except sr.UnknownValueError:

            print("No te he entendido")
            return "Error"
        
        except sr.RequestError:

            print("Problemas en el hardware")
            return "Error"
        
        except:

            print("Error indeterminado")
            return "Error"
        

def respuesta_PC(text):

    engine = pyttsx3.init()

    # rate = engine.getProperty("rate")
    engine.setProperty("rate", 160)

    # volume = engine.getProperty("volume")
    engine.setProperty("volume", 1)

    engine.setProperty('voice', es)


    engine.say(text)

    engine.runAndWait()

# respuesta_PC("Hello everyone!")







