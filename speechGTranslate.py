# This is a program to recognise speech 
# from the microphone and translate it into another language
# Here the source is kannada ( spoken audio through microphone)
# and then translating to english


# Uses Translator, Speech Recognition and PyAudio
import speech_recognition as sr
from googletrans import Translator

# Initiate the recognizer
r = sr.Recognizer()

# Listen audio from the micrrophone
with sr.Microphone() as source:
	print("Speak a sentence...")
	audio = r.listen(source)
	print("Got it. Thanks....")

# Using a hardtype 
try:
	texta = r.recognize_google(audio, language = "kn-IN")
	print("Text-in-Tamil : " + texta)
except:
	pass

# From the recorded audio source, print the text and then transalate to English
translator = Translator()

try:
	transtext = translator.translate(texta, dest='en').text
	print("Translated text: ", transtext)
except:
	pass