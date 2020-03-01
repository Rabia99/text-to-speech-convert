# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 16:55:22 2020

@author: HP
"""

from gtts import gTTS
import os  
mytext = 'my name is hailu!'
language = 'en'
#slow=false means that audio should havehigh speed
myobj = gTTS(text=mytext, lang=language, slow=False) 
myobj.save("ra.mp3") 
os.system("mpg321 ra.mp3") 

from pygame import mixer
mixer.init()
mixer.music.load("ra.mp3")
mixer.music.play()

