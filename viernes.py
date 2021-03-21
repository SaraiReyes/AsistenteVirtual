import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install SpeechRecognition
import wikipedia #pip install wikipedia
import smtplib
import webbrowser as wb
import psutil #pip install psutil
import pyjokes #pip install pyjokes (pero esta en inlges, hace el cambio )
import os
import pyautogui #pip install pyautogui (For Screenshot)
import random

engine = pyttsx3.init()

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
    speak('El CPU es '+usuage)

    battery=psutil.sensors_battery()
    speak('La bateria esta al '+battery.percent)

def joke():
    speak(pyjokes.get_joke())

def screenshot():
    img = pyautogui.screenshot()
    #cambiar por la ruta en la que desear guardar las capturas de pantalla
    img.save('D:\Biblioteca\Imagenes\screenshot.png')


if __name__=="__main__":

    wishme_()
    joke()

    while True:
        query= TakeCommand_().lower()      
    
    #si algo de lo que dices es por ejemplo hora, el asiatente te dira que hora es
        if 'hora' in query: 
             time_()
        elif 'fecha' in query:
             date_()
        elif 'wikipedia' in query:
            speak("Buscando...")
            query=query.replace('wikipedia','')
            result=wikipedia.summary(query, sentences=3)
            speak('De acuerdo con wikipedia')
            print(result)
            speak(result)

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
            wb.open('https://www.youtube.com/results?search_query=='+search_Term)

        elif 'busca en google' in query:
            speak("Qué deseas buscar?")
            search_Term=TakeCommand_()
            speak("Buscando ")
            wb.open('http://www.google.com/search?q='+search_Term)

        elif 'cpu' in query:
            cpu()

        elif 'broma' in query:
            joke()

        elif 'apagate' in query:
            speak("Apagando, Nos vemos...")
            quit()

        elif 'word' in query:
            speak('abriendo word...')

        elif 'word' in query:
            speak("oAbriendo word...")
            word = r'Word path'
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

        elif '¿Tengo algo que recordar?' in query:
            remember =open('memory.txt', 'r')
            speak("Me pediste que recordara esto "+remember.read())