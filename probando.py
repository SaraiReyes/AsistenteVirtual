import webbrowser
import speech_recognition as sr
import chistes 
######################################################################################################
###################   ESTE DOCUMETO ES SOLO PARA PROBAR CIERTAS FUNCIONES     ########################
######################################################################################################
r=sr.Recognizer()
with sr.Microphone() as source:
    print('Hola soy tu asistente virtual por voz')
    print(chistes.cuentaChiste())
    audio=r.listen(source)

    try:
        text=r.recognize_google(audio)
        print('Dijiste: {}'.format(text))
        print(text)
        if "Amazon" in text:
            webbrowser.open('http://amazon.es')

        if "noticias" in text:
            webbrowser.open("http://google.com")


    except:
         print("No entendi")