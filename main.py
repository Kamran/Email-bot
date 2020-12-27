#simple mail transfer protocol library
import smtplib 
#receive voice command
import speech_recognition as sr
#Python text to speech v3
import pyttsx3
#the way structure in the email message
from email.message import EmailMessage

#listening buddy hiding python code
listener = sr.Recognizer()
#speaker engine initialize
engine = pyttsx3.init()

#input paremeter
def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        #listen with microphone
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            #convert voice to text
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


def send_email(receiver, subject, message):
    #smtp server and protocl number
    server = smtplib.SMTP('smtp.gmail.com', 587)
    #transport layer security
    server.starttls()
    # Make sure to give app access in your Google account
    server.login('Sender_Email_Adress', 'Sender_Password')
    email = EmailMessage()
    email['From'] = 'Sender_Email_Adress'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)

#list of email
email_list = {
    'tutl': 'mahitulcse@gmail.com',
    'forhad': 'fakhan544@gmail.com',
    'pink': 'jennie@blackpink.com',
    'lisa': 'lisa34@gmail.com',
    'kamran':'mdkamran058@gmail.com',
    'emon':'aaziz34@gmail.com'
}


def get_email_info():
    talk('To Whom you want to send email')
    name1 = get_info()
    #receiver find the name to email_list
    receiver = email_list[name1]
    print(receiver)   
    #subject of email
    talk('What is the subject of your email?')
    subject = get_info()
    #body of email
    talk('Tell me the text in your email')
    message = get_info()
    send_email(receiver, subject, message)
    talk('Hey  Your email is sent')
    talk('Do you want to send more email?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()


get_email_info()