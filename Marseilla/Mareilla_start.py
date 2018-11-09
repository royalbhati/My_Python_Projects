import speech_recognition as sr
from gtts import gTTS
import os
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tkinter import *
from tkinter import ttk 
import weatherscrapper
import requests
from tkinter.messagebox import *
import cv2,os
import numpy as np
from PIL import Image 
import pickle


urll=requests.get('https://weather.com/en-IN/weather/today/l/28.66,77.23').text

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "Classifiers/face.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
path = 'dataSet'

cam = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX



with open('hello.txt','r') as f:
	welcome_text=f.read()

with open('bye.txt','r') as g:
	byee_text=g.read()	

with open('general.txt','r') as h:
	general_text =h.read()
def roy():
	ret, im =cam.read()
	gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
	faces=faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
	for(x,y,w,h) in faces:
		nbr_predicted, conf = recognizer.predict(gray[y:y+h,x:x+w])
		cv2.rectangle(im,(x-50,y-50),(x+w+50,y+h+50),(225,0,0),2)
		if(nbr_predicted==47):
		     nbr_predicted='stranger'
		     
		elif(nbr_predicted==57):
		    nbr_predicted='Royal'

		cv2.putText(im, str(nbr_predicted), (x,y-40), font, 1, (255,255,255), 3) #Draw the text
		cv2.imshow('im',im)
		cv2.waitKey(10)

		return nbr_predicted



def greet():
    return 'Hey '+roy()+' how'+' are '+'you'

def Marseilla():
	r = sr.Recognizer()
	stop=0
	while stop<3:
		with sr.Microphone() as source:
			print("Say something")
			print('sfdfds')
			
			audio=r.listen(source)
			print(audio)
			try:
				if r.recognize_google(audio) in 'hello' :
					tts=gTTS(text='Hi How are you',lang='hi')
					tts.save("goo.mp3")
					os.system("mpg321 goo.mp3")	
				elif r.recognize_google(audio) in byee_text:
					bye()
				elif r.recognize_google(audio)==(('reddit') or ('open reddit')):
					google()
				elif r.recognize_google(audio)	=='good':
					reddit()
				elif r.recognize_google(audio)=='hello':
					hello()
				elif r.recognize_google(audio)=='weather':
					weather()	
				else:
					

					# roy()
					# hello(roy())
					print(greet())  
 	


			except sr.UnknownValueError:
				tts=gTTS(text='I can\'t understand what you are saying',lang='hi')	
				tts.save("loo.mp3")
				os.system("mpg321 loo.mp3")	
				stop=stop+1	
				if stop==3:
					tts=gTTS(text='i am afraid but I can not understand you, I am sorry ',lang='en')
					tts.save('stop.mp3')
					os.system('mpg321 stop.mp3')
			except sr.RequestError:
				tts=gTTS(text='Sorry theres a slight problem',lang='en')
				tts.save('prob.mp3')
				os.system('mpg321 prob.mp3')

def stop_Marseilla(event):
	sys.exit()
Marseilla()
# def we(event):

# 	weatherscrapper.weathercheck(urll)
 
# root=Tk()
# root.title("Marseilla")
# frame=Frame(root)
# output_field=Entry(root)
# output_field.grid(row=2, column=1)

# labeltext=StringVar()
# label=Label(frame,textvariable=labeltext)
# labeltext.set("Marseilla")
# button=Button(root,text='Start Marseilla')#.grid(row=200,column=200,padx=200)
# button.place(relx=0.5, rely=0.5, anchor=CENTER)

# button.bind('<Button-1>',Marseilla)

# button2=ttk.Button(root,text='Check weather')
# button2.bind('<Button-1>',we)
# button2.place(relx=0.5,rely=0.89,anchor=CENTER)
# Button(root, text='Quit', command=root.destroy).grid(row=4, column=0, sticky=W, pady=4)
# root.mainloop()
