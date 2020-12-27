import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Make sure to give app access in your Google account
    server.login('rumibegum0123@gmail.com', 'rumi@0123')
    email = EmailMessage()
    email['From'] = 'rumibegum0123@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'tutl': 'mahitulcse@gmail.com',
    'forhad': 'fakhan544@gmail.com',
    'pink': 'jennie@blackpink.com',
    'lisa': 'lisa34@gmail.com',
    'kamran':'mdkamran058@gmail.com'
}


def get_email_info():
    talk('To Whom you want to send email')
    name1 = get_info()
    receiver = email_list[name1]
    print(receiver)
    talk('What is the subject of your email?')
    subject = get_info()
    talk('Tell me the text in your email')
    message = get_info()
    send_email(receiver, subject, message)
    talk('Hey  Your email is sent')
    talk('Do you want to send more email?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()


get_email_info()