import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install SpeechRecognition
import wikipediaapi #pip install wikipedia-api
import sys 
import smtplib
import webbrowser as wb
import psutil #pip install psutil
import pyjokes #pip install pyjokes (pero esta en inlges, hace el cambio )
import os
import pyautogui #pip install pyautogui (For Screenshot)
import random
import time
import operator
import json
from urllib.request import urlopen #pip3 install urllib3 
import requests

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

##
wikipediaapi.log.setLevel(level=wikipediaapi.logging.DEBUG)

# Set handler if you use Python in interactive mode
out_hdlr = wikipediaapi.logging.StreamHandler(sys.stderr)
out_hdlr.setFormatter(wikipediaapi.logging.Formatter('%(asctime)s %(message)s'))
out_hdlr.setLevel(wikipediaapi.logging.DEBUG)
wikipediaapi.log.addHandler(out_hdlr)
##

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    Time=datetime.datetime.now().strftime("%I:%M:")#Formato de 12 horas 
    speak("La hora es "+Time)


def  date_():
    year=datetime.datetime.now().year
    mont=datetime.datetime.now().month
    date=datetime.datetime.now().day
    decirMes="del mes"
    if mont==1:
        decirMes="de enero"
    elif mont==2:
        decirMes="de febrero"   
    elif mont==3:
        decirMes="de marzo"
    elif mont==4:
        decirMes="de abril"
    elif mont==5:
        decirMes="de mayo"
    elif mont==6:
        decirMes="de junio"
    elif mont==7:
        decirMes="de julio"
    elif mont==8:
        decirMes="de agosto"
    elif mont==9:
        decirMes="de septiembre"
    elif mont==10:
        decirMes="de octubre"
    elif mont==11:
        decirMes="de noviembre"
    else:
        decirMes="de diciembre"

    speak("La fecha es..."+ str(date)+decirMes+" del año "+ str(year))


def wishme_():
    speak("Bienvenido de nuevo")
    time_()
    date_()
    #saludos
    hour=datetime.datetime.now().hour

    if hour>=1 and hour<12:
        speak("Buenos dias")    
    elif hour>=12 and hour<18:
        speak("Buenas tardes")        
    else: 
        speak("Buenas noches")
    speak("Tu asistenten personal Viernes a tu servicio, dime ¿en qué puedo ayudarte?")
    
def TakeCommand_():# pip install speechRecognition python -m speech_recognition
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Estoy escuchando ...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Reconociendo...")
        query=r.recognize_google(audio, language = "es-ES")
        print(query)

    except Exception as e:
        print(e)
        print("Por favor, dilo de nuevo")
        speak("Hubo un error, no reconozco la voz")
        return "None"

    return query

def sendEmail(to, content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    #cambiar correo y contraseña por tus datos corresponidnetes
    server.login('usuario@gmail.com', 'contraseña')
    server.sendmail('usuario@gmail.com',to, content)
    server.close()

def cpu():
    usuage=str(psutil.cpu_percent())
    speak('la utilización actual de la CPU es  ')
    speak(usuage)
    speak('porciento')
    battery=psutil.sensors_battery()
    speak('La bateria esta al ')
    speak(battery.percent)
    speak('porciento')

def joke():
    #buscar pyjokes.py y cambiar en por es
    speak(pyjokes.get_joke())

def screenshot():
    horat=datetime.datetime.now().strftime("%j%M%Y%H-%M-%S")
    img = pyautogui.screenshot()    
    ruta='D:\Biblioteca\Imagenes\screenshot{}.png'.format(horat)
    print(ruta)
    #cambiar por la ruta en la que desear guardar las capturas de pantalla
    img.save(ruta)
#-------------------------------------------------------------------------------------
#//////////////////////////////////////////////////////////////////////////////////77
if __name__=="__main__":
    clear = lambda: os.system('cls') 
    clear()
    wishme_()
    try:

    while True:
        query= TakeCommand_().lower()      
    
    #si algo de lo que dices es por ejemplo hora, el asiatente te dira que hora es
        if 'dime la hora' in query or 'qué hora es' in query: 
             time_()
        elif 'dime la fecha' in query or 'qué fecha es' in query:
             date_()
        elif 'wikipedia' in query:
            speak("Buscando...")
            query=query.replace('wikipedia','')
            wiki = wikipediaapi.Wikipedia(language='es')
            page_ostrava = wiki.page(query)
            print(page_ostrava.summary)
            speak(page_ostrava.summary)

        elif 'enviar correo'in query:
            try:
                speak("¿Qué deseas decirle?")
                content=TakeCommand_()
                speak("Corrreo del destinatario")
                reciver=input("Correo del destinatario: ")
                to=reciver
                sendEmail(to, content)
                speak(content)
                speak('Email envido')

            except Exception as e:
                print(e)
                speak("Email no enviado")

        elif 'busca en chrome' in query:
            speak("Qué deseas buscar?")
            #Ingresar la ruta de chrome
            chromepath='C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
            search=TakeCommand_()
            wb.get(chromepath).open_new_tab(search+'.com')

        elif 'busca en youtube' in query:
            speak("Qué deseas buscar?")
            search_Term=TakeCommand_()
            speak("Estamos en YouTube")
            wb.open('https://www.youtube.com/results?search_query='+search_Term)

        elif 'busca en google' in query:
            speak("Qué deseas buscar?")
            search_Term=TakeCommand_()
            speak("Buscando ")
            wb.open('http://www.google.com/search?q='+search_Term)

        elif 'cpu' in query:
            cpu()

        elif 'dime una broma' in query:
            joke()

        elif 'apagate' in query:
            speak("Apagando, Nos vemos...")
            quit()

        elif 'word' in query:
            speak("Abriendo word...")
            word = 'path del programa'
            os.startfile(word)

        elif "Escribir nota" in query:
            speak("¿qué deseas escribir?")
            note = TakeCommand()
            file = open('note.txt', 'w')
            speak("¿Incluyo la fecha y la hora?")
            dt = TakeCommand()
            if 'si' in dt or 'esta bien' in dt or 'claro' in dt or 'por supuesto' in dt:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
                speak('Guardado')
            else:
                file.write(note)
                speak('Guardado')
        
        elif "Mostrar nota" in query:
            speak("Mostrando...")
            file = open("note.txt", "r")
            print(file.read())
            speak(file.read()) 

        elif 'captura pantalla' in query:
            screenshot()
            speak("¡Listo!")   
    
        elif 'escuchar música' in query:

            video ='D:\Biblioteca\Videos'
            audio = 'D:\Biblioteca\Musica'
            speak("¿qué deseas audio o video?")
            ans = (TakeCommand().lower())
            while(ans != 'audio' and ans != 'video'):
                speak("¿Podrías repetirlo? no te entendí")
                ans = (TakeCommand().lower())
        
            if 'audio' in ans:
                    songs_dir = audio
                    songs = os.listdir(songs_dir)
                    print(songs)
                    
            elif 'video' in ans:
                    songs_dir = video
                    songs = os.listdir(songs_dir)
                    print(songs)

            speak("Dime un número o quieres uno aleatorio")
            rand = (TakeCommand().lower())
            while('número' not in rand and rand != 'aleatorio'):                 
                speak("¿Podrías repetirlo? no te entendí")           
                rand = (TakeCommand().lower())

            if 'número' in rand:
                    rand = int(rand.replace("number ",""))
                    os.startfile(os.path.join(songs_dir,songs[rand]))
                    continue                                         
            elif 'aleatoiro' in rand:
			#numero de canciones en mi carpeta de musica
                    rand = random.randint(1,350)
                    os.startfile(os.path.join(songs_dir,songs[rand]))
                    continue
                

        elif 'Recuerda esto' in query:
            speak("¿qué recuerdo ?")
            memory = TakeCommand()
            speak("Me pediste que recordara esto "+memory)
            remember = open('memory.txt','w')
            remember.write(memory)
            remember.close()

        elif '¿Tengo algo que recordar?' in query :
            remember =open('memory.txt', 'r')
            speak("Me pediste que recordara esto "+remember.read())

        elif 'noticias' in query:
            
            try:

                jsonObj = urlopen('apikey de noticias')
                data = json.load(jsonObj)
                i = 1
                
                speak('aquí algunas noticas sobre México')
                print('''=============== TOP DE NOTICIAS ============'''+ '\n')
                
                for item in data['articles']:
                    
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
                    
            except Exception as e:
                print(str(e)) 
                speak("No puedo acceder a internet")

        elif "Donde esta" in query:
            query = query.replace("donde esta", "")
            location = query
            speak("Abriendo google maps")
            speak(location)
            wb.open("https://www.google.com/maps/place/" + location + "")
        elif "busca en el mapa" in query:
            query = query.replace("busca en el mapa", "")
            location = query
            speak("Abriendo google maps")
            speak(location)
            wb.open("https://www.google.com/maps/place/" + location + "")

        elif "abre facebook" in query or "facebook"  in query or "abre feis" in query :
            webbrowser.open('https://web.facebook.com/')
        elif "abre google" in query:
            webbrowser.open('http://google.com') 
        elif "abre twitter" in query:
            webbrowser.open('https://twitter.com/?lang=es') 

        elif "no escuches" in query or "detente un momento" in query or "duermete un momento" in query:
            speak("por cuantos segundos?")
            a = int(TakeCommand())
            time.sleep(a)
            print(a)

        elif 'apaga computadora' in query:
            os.system("shutdown -1")
        elif 'reinicia computadora' in query:
            os.system("shutdown /r /t 1")






# pip install pyinstaller
#pyinstaller --onefile 'viernes.py'