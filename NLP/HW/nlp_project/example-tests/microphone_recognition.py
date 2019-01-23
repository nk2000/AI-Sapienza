#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import os

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("I'm listening")
    audio = r.listen(source)
print("I'm not listening anymore")

# recognize speech using Google Speech Recognition
try:
    text = r.recognize_google(audio)
    print("Google Speech Recognition thinks you said: " + text)
    os.system("echo " + text + " | espeak")
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
