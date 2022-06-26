import pyttsx3
from gtts import gTTS
import os

#MALE
engine = pyttsx3.init()
engine.say("Hello there, cannot open shared object file: No such file or directory")
engine.runAndWait()

#FEMALE
mytext = 'You are welcome to Roles Academy Madam. About Company:Roles Academy is a leading institute in Delhi NCR offering computer education courses and foreign languages like Spanish, German, French, etc. Roles Academy also provides web design courses in Delhi, including mobile web design course and content writing courses in Delhi. For more details please call +91-9971110009 or visit the website: www.rolesacademy.com.Roles Academy is a leading institute'
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("welcome.mp3")
os.system("mpg321 welcome.mp3")

