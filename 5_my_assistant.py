import speech_recognition as sr
import pyttsx3
import datetime

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

def pedir_dia():

    dia = datetime.date.today()
    # print(dia)

    dia_semana = dia.weekday()
    print(dia_semana)

    # diccionario con los días
    dict_dias_semana = {0: "Lunes",
                        1: "Martes",
                        2: "Miércoles",
                        3: "Jueves",
                        4: "Viernes",
                        5: 'Sábado',
                        6: "Domingo"}
    
    respuesta_PC(f"Hoy es {dict_dias_semana[dia_semana]}")

def pedir_hora():

    hora = datetime.datetime.now()

    hora = f"En este momento son las {hora.hour} con {hora.minute} minutos y {hora.second} segundos"

    respuesta_PC(hora)

def saludo_inicial():

    hora = datetime.datetime.now()

    if 6 <= hora.hour < 14:
        ahora = "Buenos días"
    elif 14 <= hora.hour < 20:
        ahora = "Buenas tardes"
    else:
        ahora = "Buenas noches"

    respuesta_PC(f"{ahora}, soy Helena tu asistente personal.")
    respuesta_PC("¿En qué puedo ayudarte?")

# saludo_inicial()







