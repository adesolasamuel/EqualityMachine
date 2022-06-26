import pyttsx3
from gtts import gTTS
import os

#MALE
engine = pyttsx3.init()
engine.say("Hello there")
engine.runAndWait()

#FEMALE
mytext = 'You are welcome to Roles Academy Madam.'
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("welcome.mp3")
os.system("mpg321 welcome.mp3")

