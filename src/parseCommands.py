import json
import urllib
from globalCommands import commands
from speech import *
from browseMode import BrowseModeTreeInterceptor
import os.path
import sys
sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(__file__)), 'modules'))
import keyboard
import speech_recognition as sr

del sys.path[0]
import time

startTime = time.time()
def speech_rec():
	r = sr.Recognizer()

	print("Speak Now!")
	with sr.Microphone() as source:                # use the default microphone as the audio source
		r.adjust_for_ambient_noise(source, duration = 1)
		print "Time when you spoke:",time.time()-startTime
		audio = r.listen(source)                   # listen for the first phrase and extract it into audio data

	try:
		s=r.recognize_google(audio)					# recognize speech using Google Speech Recognition
		print "Time when Speech is recognized  ", time.time()-startTime
		print("You said " + s)    
		return s

	except LookupError:                           # speech is unintelligible
		print("Could not understand audio")

def start():
	#speech_output_filename="C:\\Users\\hp\\source\\repos\\CPPHelloSpeech\\CPPHelloSpeech\\speech_to_text_out.txt"


	s=speech_rec()		#returns the recognized speech
	'''
	speech_output_filename="speech_text.txt"
	f=open(speech_output_filename,"r")		##reads the text command 
	s=f.readline()
	'''
	#commands.script_say_battery_status(None)
		
	###Fetching the response
	#url_req='https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/90c836a8-52d8-4cd8-8b6d-d7e4060eaeb6?subscription-key=662e5a4e75654f6cadbf143294a5e0a8&verbose=false&timezoneOffset=0&q='
	#url_req+='Go%20to%20the%20fourth%20last%20heading'
	args={"q":s}
	'''
	url_req='https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/90c836a8-52d8-4cd8-8b6d-d7e4060eaeb6?subscription-key=662e5a4e75654f6cadbf143294a5e0a8&verbose=false&timezoneOffset=0&{}'.format(urllib.parse.urlencode(args))'''
	#url_req+='Move to the next line'
	#response = urllib.request.urlopen(url_req)

	##Calls the LUIS end-point with the user command as an argument
	url_req='https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/90c836a8-52d8-4cd8-8b6d-d7e4060eaeb6?subscription-key=662e5a4e75654f6cadbf143294a5e0a8&verbose=false&timezoneOffset=0&{}'.format(urllib.urlencode(args))
	
	response=urllib.urlopen(url_req)
	print "Time to get response from LUIS  ", time.time()-startTime

	data = json.load(response)   
	print("data=",data)
	
	##Dictionary with key as Intents defined in LUIS, and values as the corresponding function calls
	key_commands=	{
	
	"NextLine":next_line,
	"PreviousLine":previous_line,
	"NextWord":next_word,
	"PreviousWord":previous_word,
	"Next character":next_character,
	"Previous character":previous_character,
	"StartLine":start_line,			
	"EndLine":end_line,	

	"Heading":heading,
	"Graphics":graphic,
	"List":list_fn,
	"ListItem":listitem,
	
	"Top page":top,
	"End Page":bottom,
	"CurrentLine":current_line,
	"CurrentWord":current_word,
	"Current character":current_character,

	"Column":column,
	"Row":row,
	"Table":table,
	"Previous Paragraph":previous_paragraph,
	"Next paragraph":next_paragraph,
	"StartParagraph":start_paragraph,
	"StartWord":start_word
	}
	
	intent=data["topScoringIntent"]["intent"]
	print("intent=",intent)
	x=data["entities"]
	key_commands[intent](x)



def next_line(entities):
	
	no_of_jumps=0
	cnt=0
	basic_comm={"next":1,"line":1}
	for x in entities:
		if(x["type"]=="builtin.number" or x["type"]=="builtin.ordinal"):
			no_of_jumps=int(x["resolution"]["value"])		##extracts the number of jumps required
		else:
			if(x["type"] not in basic_comm):
				cnt+=1
	
	#Calls the nextLine function no_of_jumps times
	while(no_of_jumps>0):		
		print("Pressing Down")
		commands.script_review_nextLine(None)	#Calls the NVDA defined function
		pauseSpeech(True)						#Pauses NVDA speech every time the cursor moves to the next line
		no_of_jumps-=1	
	
	commands.script_review_nextLine(None)		#Finally points to the line requested for
	#commands.script_reportCurrentFocus(None)		if uncommented ,starts saying continuously from this line
	print("Finish next line execution=  ",time.time() - startTime)
	
def previous_line(entities):
	print("TIMe1=  ",time.time() - startTime)
	no_of_jumps=0							
	cnt=0
	basic_comm={"previous":1,"line":1}
	for x in entities:
		if(x["type"]=="builtin.number" or x["type"]=="builtin.ordinal"):
			no_of_jumps=int(x["resolution"]["value"])			##extracts the number of jumps required
		else:
			if(x["type"] not in basic_comm):
				cnt+=1

	#Calls the previousLine function no_of_jumps times
	while(no_of_jumps>0):
		print("Pressing UP")
		commands.script_review_previousLine(None)	#Calls the NVDA defined function
		pauseSpeech(True)							##Pauses NVDA speech every time the cursor moves to the previous line
		no_of_jumps-=1
	commands.script_review_previousLine(None)		#Finally points to the line requested for
	print("Finish previous line execution=  ",time.time() - startTime)

		
def next_word(entities):
	no_of_jumps=0
	cnt=0
	basic_comm={"next":1,"word":1}
	for x in entities:
		if(x["type"]=="builtin.number" or x["type"]=="builtin.ordinal"):
			no_of_jumps=int(x["resolution"]["value"])			##extracts the number of jumps required
		else:
			if(x["type"] not in basic_comm):
				cnt+=1

	#Calls the previousLine function no_of_jumps times
	while(no_of_jumps>0):
		print("Pressing Ctrl+RightArrow")
		#keyboard.press_and_release('shift')
		commands.script_review_nextWord(None)	#Calls the NVDA defined function
		pauseSpeech(True)						##Pauses NVDA speech every time the cursor moves to the previous line
		no_of_jumps-=1
	commands.script_review_nextWord(None)		#Finally points to the line requested for


def previous_word(entities):
	no_of_jumps=0
	cnt=0
	basic_comm={"previous":1,"word":1}
	for x in entities:
		if(x["type"]=="builtin.number" or x["type"]=="builtin.ordinal"):
			no_of_jumps=int(x["resolution"]["value"])			#extracts the number of jumps required
		else:
			if(x["type"] not in basic_comm):
				cnt+=1

	#Calls the previousWord function no_of_jumps times
	while(no_of_jumps>0):
		print("Pressing Ctrl+LeftArrow")
		commands.script_review_previousWord(None)				#Calls the NVDA defined function
		pauseSpeech(True)										#Pauses NVDA speech every time the cursor moves to the previous word
		no_of_jumps-=1
	commands.script_review_previousWord(None)					#Finally points to the word requested for
	print("Finish previous word execution=  ",time.time() - startTime)


def current_word(entities):
	print "Current word"
	commands.script_review_currentWord(None)		#Points to the current word


def next_character(entities):
	no_of_jumps=0
	cnt=0
	basic_comm={"next":1,"character":1}
	for x in entities:
		if(x["type"]=="builtin.number" or x["type"]=="builtin.ordinal"):
			no_of_jumps=int(x["resolution"]["value"])			##extracts the number of jumps required
		else:
			if(x["type"] not in basic_comm):
				cnt+=1

	#Calls the nextCharacter function no_of_jumps times
	while(no_of_jumps>0):
		print("Pressing RightArrow")
		commands.script_review_nextCharacter(None)				#Calls the NVDA defined function
		pauseSpeech(True)										#Pauses NVDA speech every time the cursor moves to the next character
		no_of_jumps-=1
	commands.script_review_nextCharacter(None)					#Finally points to the character requested for
	print("Finish next char execution=  ",time.time() - startTime)


def previous_character(entities):
	no_of_jumps=0
	cnt=0
	basic_comm={"previous":1,"character":1}
	for x in entities:
		if(x["type"]=="builtin.number" or x["type"]=="builtin.ordinal"):
			no_of_jumps=int(x["resolution"]["value"])			#extracts the number of jumps required
		else:
			if(x["type"] not in basic_comm):
				cnt+=1

	#Calls the previousCharacter function no_of_jumps times
	while(no_of_jumps>0):
		print("Pressing LeftArrow")
		commands.script_review_previousCharacter(None)				#Calls the NVDA defined function
		pauseSpeech(True)											#Pauses NVDA speech every time the cursor moves to the previousCharacter
		no_of_jumps-=1
	commands.script_review_previousCharacter(None)					#Finally points to the word requested for
	print("Finish previous char  execution=  ",time.time() - startTime)


def current_character(entities):
	print "Current character"
	commands.script_review_currentCharacter(None)					#Points to the current character


def start_line(entities):		
	basic_comm={"start":1,"line":1}
	cnt=0
	for x in entities:
		if(x["type"] not in basic_comm):
			cnt+=1
	print("Pressing Up")
	print("Pressing Down")
	commands.script_review_startOfLine(None)						#Points to the start of the line

def end_line(entities):
	basic_comm={"end":1,"line":1}
	cnt=0
	for x in entities:
		if(x["type"] not in basic_comm):
			cnt+=1
	if(cnt==0):		##no other entity
		print("Pressing Ctrl+Up")
		print("Pressing Ctrl+Down")
		commands.script_review_endOfLine(None)						#Points to the end of the line	
		
def current_line(entities):
	print "current line"
	commands.script_review_currentLine(None)						#Points to the current line

#This item uses keyboard module to send the corresponding key instead of calling the NVDA function
def heading(entities):	
	basic_comm={"last":1,"previous":1,"next":1,"heading":1}
	cnt=0
	prev_or_next=0 		##0 for next ,1 for prev
	no_of_jumps=0
	ordinal_flag=0
	lastflag=0
	#br=BrowseModeTreeInterceptor()
	
	for x in entities:
		if(x["type"]=="builtin.number" ):
			no_of_jumps=int(x["resolution"]["value"])			#extracts the number of jumps required if any
		elif(x["type"]=="builtin.ordinal"):
			ordinal_flag=1
			no_of_jumps=int(x["resolution"]["value"])-1
		else:
			if(x["type"]=="previous"):
				prev_or_next=1									#Marks the flag true, if previous heading is required
			if(x["type"]=="last"):
				lastflag=1										#Marks th flag true, if "last heading" is required
			elif(x["type"] not in basic_comm):
				cnt+=1
	print("No of jumps=",no_of_jumps)

	#Commands involving ordinal number like "Go to the second heading" not functional now
	if(ordinal_flag==1 and lastflag==0):
		print("Pressing Ctrl+Home")								#To go to the start of the document
		#commands.script_review_top(None)
		#keyboard.press_and_release('ctrl+home')
		top(entities)
		#pauseSpeech(True)
	elif(lastflag==1):
		print("Pressing Ctrl+End")
		keyboard.press_and_release('ctrl+end')
		#commands.script_review_bottom(None)
		#pauseSpeech(True)
		
		if(ordinal_flag==1):
			while(no_of_jumps>0):
				print("Pressing shift+h")
				keyboard.press_and_release('shift+h')
				pauseSpeech(True)
				no_of_jumps-=1
			keyboard.press_and_release('shift+h')
		else:
			print("Pressing shift+h")	##if user just says go to last heading
			keyboard.press_and_release('shift+h')
			#commands.script_review_previousHeading(None)
			
	if(prev_or_next==1):										#for previous heading	
		while(no_of_jumps>0):
			print("Pressing shift+h")
			keyboard.press_and_release('shift+h')				#Sends the keys "shift+h"
			pauseSpeech(True)									#Pauses NVDA speech every time the cursor moves to the previous heading
			no_of_jumps-=1
		keyboard.press_and_release('shift+h')
	elif(lastflag==0):											#if last heading is not required, then go to next heading
		while(no_of_jumps>0):
			print("Pressing h")
			print("Printng in last elif")
			#br=BrowseModeTreeInterceptor()
			#br._BrowseModeTreeInterceptor_quickNavScript(None, "heading", "next", _("no next heading"), None)
			keyboard.press_and_release('h')						#Sends the key "h"
			pauseSpeech(True)									#Pauses NVDA speech every time the cursor moves to the next heading
			#eval("script_nextHeading")
			#pyautogui.hotkey("h")
			##BrowseModeTreeInterceptor.addQuickNav("heading", key="h",nextDoc=_("moves to the next heading"),nextError=_("no next heading"),
			##prevDoc=_("moves to the previous heading"),prevError=_("no previous heading"))
			no_of_jumps-=1
		keyboard.press_and_release('h')
	print("Finish heading execution=  ",time.time() - startTime)
			

#This item uses keyboard module to send the corresponding key instead of calling the NVDA function
def graphic(entities):	
	basic_comm={"last":1,"previous":1,"next":1,"graphic":1}
	cnt=0
	prev_or_next=0 											#0 for next ,1 for prev
	no_of_jumps=0
	ordinal_flag=0
	lastflag=0
	for x in entities:
		if(x["type"]=="builtin.number" ):
				no_of_jumps=int(x["resolution"]["value"])	#extracts the no of jumps required
		elif(x["type"]=="builtin.ordinal"):
			ordinal_flag=1
			no_of_jumps=int(x["resolution"]["value"])
		else:
			if(x["type"]=="previous"):
				prev_or_next=1								#Marks the flag set if the command is previous graphic
			if(x["type"]=="last"):
				lastflag=1									#Marks the flag set if "last graphic" is the command
			elif(x["type"] not in basic_comm):
				cnt+=1

	#Commands involving ordinal number like "Go to the second list" not functional now
	if(ordinal_flag==1 and lastflag==0):
		print("Pressing Ctrl+Home")							#To go to the start of the document
	elif(lastflag==1):
		print("Pressing Ctrl+End")
		
		if(ordinal_flag==1):
			while(no_of_jumps>0):
				print("Pressing shift+g")
				keyboard.press_and_release('shift+g')		
				pauseSpeech(True)							
				no_of_jumps-=1
			keyboard.press_and_release('shift+g')
		else:
			print("Pressing shift+g")						#if user just says go to last graphic
			keyboard.press_and_release('shift+g')
			
	if(prev_or_next==1):									#for previous graphic
		while(no_of_jumps>0):
			print("Pressing shift+g")
			keyboard.press_and_release('shift+g')			#Sends the key "shift+g" for previous graphic
			pauseSpeech(True)								#Pauses NVDA speech every time the cursor moves to the previous graphic item
			no_of_jumps-=1
		keyboard.press_and_release('shift+g')
	elif(lastflag==0):
		while(no_of_jumps>0):
			print("Pressing g")
			keyboard.press_and_release('g')					#Sends the key "g" for next graphic
			pauseSpeech(True)								#Pauses NVDA speech every time the cursor moves to theprevious graphic item
			no_of_jumps-=1
		keyboard.press_and_release('g')
	print("Finish list execution=  ",time.time() - startTime)				#Points to the graphic requested for
		


#This item uses keyboard module to send the corresponding key instead of calling the NVDA function
def list_fn(entities):
	basic_comm={"last":1,"previous":1,"next":1,"list":1}
	cnt=0
	prev_or_next=0 										#0 for next ,1 for prev
	no_of_jumps=0
	ordinal_flag=0
	lastflag=0
	for x in entities:
		if(x["type"]=="builtin.number" ):
				no_of_jumps=int(x["resolution"]["value"])	#extracts the no of jumps required
		elif(x["type"]=="builtin.ordinal"):
			ordinal_flag=1
			no_of_jumps=int(x["resolution"]["value"])
		else:
			if(x["type"]=="previous"):
				prev_or_next=1								#Marks the flag set if the command is previous list
			if(x["type"]=="last"):
				lastflag=1									#Marks the flag set if "last list" is the command
			elif(x["type"] not in basic_comm):
				cnt+=1

	#Commands involving ordinal number like "Go to the second list" not functional now
	if(ordinal_flag==1 and lastflag==0):
		print("Pressing Ctrl+Home")							#To go to the start of the document
	elif(lastflag==1):
		print("Pressing Ctrl+End")
		
		if(ordinal_flag==1):
			while(no_of_jumps>0):
				print("Pressing shift+l")
				keyboard.press_and_release('shift+l')		
				pauseSpeech(True)							
				no_of_jumps-=1
			keyboard.press_and_release('shift+l')
		else:
			print("Pressing shift+l")	##if user just says go to last heading
			keyboard.press_and_release('shift+l')
			
	if(prev_or_next==1):									#for previous list
		while(no_of_jumps>0):
			print("Pressing shift+l")
			keyboard.press_and_release('shift+l')			#Sends the key "shift+l" for previous list
			pauseSpeech(True)								#Pauses NVDA speech every time the cursor moves to the previous list item
			no_of_jumps-=1
		keyboard.press_and_release('shift+l')
	elif(lastflag==0):
		while(no_of_jumps>0):
			print("Pressing l")
			keyboard.press_and_release('l')					#Sends the key "l" for next list
			pauseSpeech(True)								#Pauses NVDA speech every time the cursor moves to the next list item
			no_of_jumps-=1
		keyboard.press_and_release('l')
	print("Finish list execution=  ",time.time() - startTime)
			
def listitem(entities):
	basic_comm={"last":1,"previous":1,"next":1,"item":1}
	cnt=0
	prev_or_next=0 											#0 for next ,1 for prev
	no_of_jumps=0
	ordinal_flag=0
	lastflag=0
	for x in entities:
		if(x["type"]=="builtin.number" ):
				no_of_jumps=int(x["resolution"]["value"])	#extracts the no of jumps required
		elif(x["type"]=="builtin.ordinal"):
			ordinal_flag=1
			no_of_jumps=int(x["resolution"]["value"])
		else:
			if(x["type"]=="previous"):
				prev_or_next=1								#Marks the flag set if the command is previous listitem
			if(x["type"]=="last"):
				lastflag=1									#Marks the flag set if "last listitem" is the command
			elif(x["type"] not in basic_comm):
				cnt+=1

	#Commands involving ordinal number like "Go to the second listitem" not functional now
	if(ordinal_flag==1 and lastflag==0):
		print("Pressing Ctrl+Home")							#To go to the start of the document
	elif(lastflag==1):
		print("Pressing Ctrl+End")
		
		if(ordinal_flag==1):
			while(no_of_jumps>0):
				print("Pressing shift+i")
				keyboard.press_and_release('shift+i')		
				pauseSpeech(True)							
				no_of_jumps-=1
			keyboard.press_and_release('shift+i')
		else:
			print("Pressing shift+i")						#if user just says go to lastitem
			keyboard.press_and_release('shift+i')
			
	if(prev_or_next==1):									#for previous listitem	
		while(no_of_jumps>0):
			print("Pressing shift+i")
			keyboard.press_and_release('shift+i')			#Sends the key "shift+i" for previous list item
			pauseSpeech(True)								#Pauses NVDA speech every time the cursor moves to the previous listitem
			no_of_jumps-=1
		keyboard.press_and_release('shift+i')
	elif(lastflag==0):
		while(no_of_jumps>0):
			print("Pressing i")
			keyboard.press_and_release('i')					#Sends the key "i" for next listitem
			pauseSpeech(True)								#Pauses NVDA speech every time the cursor moves to the next listitem
			no_of_jumps-=1
		keyboard.press_and_release('i')
	print("Finish list execution=  ",time.time() - startTime)		

#To go to the top/start of the page
def top(entities):
	print("Pressing Top")
	commands.script_review_top(None)					#Calls NVDA function to go to the top of the document

#To go to the end/bottom of the document
def bottom(entities):
	print("Pressing Bottom")
	commands.script_review_bottom(None)					#Calls NVDA function to go to the end of the document


def column(entities):	
	basic_comm={"last":1,"previous":1,"next":1,"column":1}
	cnt=0
	prev_or_next=0 		##0 for next ,1 for prev
	no_of_jumps=1
	for x in entities:
		if(x["type"]=="builtin.number" or x["type"]=="builtin.ordinal"):
				no_of_jumps=int(x["resolution"]["value"])
		else:
			if(x["type"]=="previous"):
				prev_or_next=1
			elif(x["type"] not in basic_comm):
				cnt+=1
	if(prev_or_next==1):			##for previous heading	
		while(no_of_jumps>0):
			print("Pressing Ctrl+alt+leftArrow")
			no_of_jumps-=1
	else:
		while(no_of_jumps>0):
			print("Pressing Ctrl+alt+RightArrow")
			no_of_jumps-=1

def row(entities):	
	basic_comm={"last":1,"previous":1,"next":1,"row":1}
	cnt=0
	prev_or_next=0 		##0 for next ,1 for prev
	no_of_jumps=0
	for x in entities:
		if(x["type"]=="builtin.number" or x["type"]=="builtin.ordinal"):
				no_of_jumps=int(x["resolution"]["value"])
		else:
			if(x["type"]=="previous"):
				prev_or_next=1
			elif(x["type"] not in basic_comm):
				cnt+=1
	if(prev_or_next==1):			##for previous heading	
		while(no_of_jumps>0):
			print("Pressing Ctrl+alt+upArrow")
			no_of_jumps-=1
	else:
		while(no_of_jumps>0):
			print("Pressing Ctrl+alt+DownArrow")
			no_of_jumps-=1
		
def table(entities):	
	basic_comm={"last":1,"previous":1,"next":1,"table":1}
	cnt=0
	prev_or_next=0 		##0 for next ,1 for prev
	no_of_jumps=1
	ordinal_flag=0
	lastflag=0
	for x in entities:
		if(x["type"]=="builtin.number" ):
				no_of_jumps=int(x["resolution"]["value"])
		elif(x["type"]=="builtin.ordinal"):
			ordinal_flag=1
			no_of_jumps=int(x["resolution"]["value"])
		else:
			if(x["type"]=="previous"):
				prev_or_next=1
			if(x["type"]=="last"):
				lastflag=1
			elif(x["type"] not in basic_comm):
				cnt+=1
	if(ordinal_flag==1 and lastflag==0):
		print("Pressing Ctrl+Home")		##To go to the start of the document
	elif(lastflag==1):
		print("Pressing Ctrl+End")
		
		if(ordinal_flag==1):
			while(no_of_jumps>0):
				print("Pressing shift+t")
				no_of_jumps-=1
		else:
			print("Pressing shift+t")	##if user just says go to last heading
			
	if(prev_or_next==1):			##for previous heading	
		while(no_of_jumps>0):
			print("Pressing shift+t")
			no_of_jumps-=1
	elif(lastflag==0):
		while(no_of_jumps>0):
			print("Pressing t")
			no_of_jumps-=1

def start_paragraph(entities):
	basic_comm={"start":1,"paragraph":1}
	cnt=0
	for x in entities:
		if(x["type"] not in basic_comm):
			cnt+=1
	#if(cnt==0):		##no other entity
	print("Pressing Ctrl+Up")
	print("Pressing Ctrl+Down")
	
def start_word(entities):
	basic_comm={"start":1,"word":1}
	cnt=0
	for x in entities:
		if(x["type"] not in basic_comm):
			cnt+=1
	#if(cnt==0):		##no other entity
	print("Pressing Ctrl+LeftArrow")
	print("Pressing Ctrl+RightArrow")


def previous_paragraph(entities):
	no_of_jumps=0
	cnt=0
	basic_comm={"previous":1,"paragraph":1}
	for x in entities:
		if(x["type"]=="builtin.number" or x["type"]=="builtin.ordinal"):
			no_of_jumps=int(x["resolution"]["value"])
		else:
			if(x["type"] not in basic_comm):
				cnt+=1
	while(no_of_jumps>0):
		print("Pressing Ctrl+UP")
		keyboard.press_and_release('ctrl+up')
		no_of_jumps-=1
	keyboard.press_and_release('ctrl+up')


def next_paragraph(entities):
	no_of_jumps=0
	cnt=0
	basic_comm={"next":1,"paragraph":1}
	for x in entities:
		if(x["type"]=="builtin.number" or x["type"]=="builtin.ordinal"):
			no_of_jumps=int(x["resolution"]["value"])
		else:
			if(x["type"] not in basic_comm):
				cnt+=1
	while(no_of_jumps>0):
		print("Pressing Ctrl+Down")
		keyboard.press_and_release('ctrl+down')
		no_of_jumps-=1
	keyboard.press_and_release('ctrl+down')
