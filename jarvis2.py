import speech_recognition as sr
import pyttsx3
import wikipediaapi
import pywhatkit
import openai

audio = sr.Recognizer()
maquina = pyttsx3.init()

def listen_command():
    try:
        with sr.Microphone() as source:
            print('Escutando...')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            if 'jarvis' in comando:
                comando = comando.replace('jarvis', '')
                maquina.say(comando)
                maquina.runAndWait()

    except Exception as e:
        print(f'Microfone não está ok {e}')

    return comando

def execute_command():
    comando = listen_command()
    if 'procure por' in comando or 'pesquise por' in comando:
        procurar = comando.replace('procure por', '')
        wikipediaapi.set_lang('pt')
        resultado = wikipediaapi.summary(procurar, 2)
        print(resultado)
        maquina.say(resultado)
        maquina.runAndWait()
    else:
        pass

while True:
    execute_command()
