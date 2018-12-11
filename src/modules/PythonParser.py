import json
import urllib
from globalCommands import commands
from browseMode import BrowseModeTreeInterceptor
#import keyboard

def start():
	speech_output_filename="C:\\Users\\hp\\source\\repos\\CPPHelloSpeech\\CPPHelloSpeech\\speech_to_text_out.txt"
	f=open(speech_output_filename,"r")		##reads the text command 
	s=f.readline()
	commands.script_say_battery_status(None)
		
	###Fetching the response
	#url_req='https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/90c836a8-52d8-4cd8-8b6d-d7e4060eaeb6?subscription-key=662e5a4e75654f6cadbf143294a5e0a8&verbose=false&timezoneOffset=0&q='
	#url_req+='Go%20to%20the%20fourth%20last%20heading'
	args={"q":s}
	'''
	url_req='https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/90c836a8-52d8-4cd8-8b6d-d7e4060eaeb6?subscription-key=662e5a4e75654f6cadbf143294a5e0a8&verbose=false&timezoneOffset=0&{}'.format(urllib.parse.urlencode(args))'''
	#url_req+='Move to the next line'
	#response = urllib.request.urlopen(url_req)
	url_req='https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/90c836a8-52d8-4cd8-8b6d-d7e4060eaeb6?subscription-key=662e5a4e75654f6cadbf143294a5e0a8&verbose=false&timezoneOffset=0&{}'.format(urllib.urlencode(args))
	
	response=urllib.urlopen(url_req)
	data = json.load(response)   
	print("data=",data)
	filename="D:\\MTP1\\AddOnTrial\\JSONResponse.txt"
	with open(filename,'w') as json_file:
		json.dump(data,json_file)
	key_commands=	{
	"Previous Paragraph":previous_paragraph,
	"Next paragraph":next_paragraph,
	"NextLine":next_line,
	"PreviousLine":previous_line,
	"NextWord":next_word,
	"PreviousWord":previous_word,
	"Next character":next_character,
	"Previous character":previous_character,
	"StartLine":start_line,			##check doubts
	"EndLine":end_line,				##check doubts
	"Heading":heading,
	"Column":column,
	"Row":row,
	"Table":table,
	"Graphics":graphic,
	"List":list,
	"ListItem":listitem,
	"StartParagraph":start_paragraph,
	"StartWord":start_word

	}
	
	with open(filename) as f:
		data = json.load(f)
	
	intent=data["topScoringIntent"]["intent"]
	print("intent=",intent)
	x=data["entities"]
	key_commands[intent](x)
	#input("Press enter to exit")
	


def previous_paragraph(entities):
	no_of_jumps=1
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
		no_of_jumps-=1


def next_paragraph(entities):
	no_of_jumps=1
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
		no_of_jumps-=1

def next_line(entities):
	no_of_jumps=1
	cnt=0
	basic_comm={"next":1,"line":1}
	for x in entities:
		if(x["type"]=="builtin.number" or x["type"]=="builtin.ordinal"):
			no_of_jumps=int(x["resolution"]["value"])
		else:
			if(x["type"] not in basic_comm):
				cnt+=1
	while(no_of_jumps>0):
		print("Pressing Down")
		commands.script_review_nextLine(None)
		print("After down")
		no_of_jumps-=1

def previous_line(entities):
	no_of_jumps=1
	cnt=0
	basic_comm={"previous":1,"line":1}
	for x in entities:
		if(x["type"]=="builtin.number" or x["type"]=="builtin.ordinal"):
			no_of_jumps=int(x["resolution"]["value"])
		else:
			if(x["type"] not in basic_comm):
				cnt+=1
	while(no_of_jumps>0):
		print("Pressing UP")
		commands.script_review_previousLine(None)
		no_of_jumps-=1

		
def next_word(entities):
	no_of_jumps=1
	cnt=0
	basic_comm={"next":1,"word":1}
	for x in entities:
		if(x["type"]=="builtin.number" or x["type"]=="builtin.ordinal"):
			no_of_jumps=int(x["resolution"]["value"])
		else:
			if(x["type"] not in basic_comm):
				cnt+=1
	while(no_of_jumps>0):
		print("Pressing Ctrl+RightArrow")
		commands.script_review_nextWord(None)
		no_of_jumps-=1

def previous_word(entities):
	no_of_jumps=1
	cnt=0
	basic_comm={"previous":1,"word":1}
	for x in entities:
		if(x["type"]=="builtin.number" or x["type"]=="builtin.ordinal"):
			no_of_jumps=int(x["resolution"]["value"])
		else:
			if(x["type"] not in basic_comm):
				cnt+=1
	while(no_of_jumps>0):
		print("Pressing Ctrl+LeftArrow")
		commands.script_review_previousWord(None)
		no_of_jumps-=1

def next_character(entities):
	no_of_jumps=1
	cnt=0
	basic_comm={"next":1,"character":1}
	for x in entities:
		if(x["type"]=="builtin.number" or x["type"]=="builtin.ordinal"):
			no_of_jumps=int(x["resolution"]["value"])
		else:
			if(x["type"] not in basic_comm):
				cnt+=1
	while(no_of_jumps>0):
		print("Pressing RightArrow")
		commands.script_review_nextCharacter(None)
		
		no_of_jumps-=1

def previous_character(entities):
	no_of_jumps=1
	cnt=0
	basic_comm={"previous":1,"character":1}
	for x in entities:
		if(x["type"]=="builtin.number" or x["type"]=="builtin.ordinal"):
			no_of_jumps=int(x["resolution"]["value"])
		else:
			if(x["type"] not in basic_comm):
				cnt+=1
	while(no_of_jumps>0):
		print("Pressing LeftArrow")
		commands.script_review_previousCharacter(None)
		no_of_jumps-=1

def start_line(entities):		##check this
	basic_comm={"start":1,"line":1}
	cnt=0
	for x in entities:
		if(x["type"] not in basic_comm):
			cnt+=1
	#if(cnt==0):		##no other entity
	print("Pressing Up")
	print("Pressing Down")
	commands.script_review_startOfLine(None)

def end_line(entities):
	basic_comm={"end":1,"line":1}
	cnt=0
	for x in entities:
		if(x["type"] not in basic_comm):
			cnt+=1
	if(cnt==0):		##no other entity
		print("Pressing Ctrl+Up")
		print("Pressing Ctrl+Down")
		commands.script_review_endOfLine(None)
		
def heading(entities):	
	basic_comm={"last":1,"previous":1,"next":1,"heading":1}
	cnt=0
	prev_or_next=0 		##0 for next ,1 for prev
	no_of_jumps=1
	ordinal_flag=0
	lastflag=0
	#br=BrowseModeTreeInterceptor()
	
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
				print("Pressing shift+h")
				commands.script_review_previousHeading(None)
				no_of_jumps-=1
		else:
			print("Pressing shift+h")	##if user just says go to last heading
			commands.script_review_previousHeading(None)
			
	if(prev_or_next==1):			##for previous heading	
		while(no_of_jumps>0):
			print("Pressing shift+h")
			executeScript(script_review_previousHeading,None)
			no_of_jumps-=1
	elif(lastflag==0):
		while(no_of_jumps>0):
			print("Pressing h")
			print("Printng in last elif")
			#br=BrowseModeTreeInterceptor()
			#br._BrowseModeTreeInterceptor_quickNavScript(None, "heading", "next", _("no next heading"), None)
			#keyboard.press_and_release('h')
			eval("nextHeading")
			#pyautogui.hotkey("h")
			##BrowseModeTreeInterceptor.addQuickNav("heading", key="h",nextDoc=_("moves to the next heading"),nextError=_("no next heading"),
			##prevDoc=_("moves to the previous heading"),prevError=_("no previous heading"))
			no_of_jumps-=1
			
def graphic(entities):	
	basic_comm={"last":1,"previous":1,"next":1,"graphic":1}
	cnt=0
	prev_or_next=0 		##0 for next ,1 for prev
	no_of_jumps=1
	ordinal_flag=0
	for x in entities:
		if(x["type"]=="builtin.number" ):
				no_of_jumps=int(x["resolution"]["value"])
		elif(x["type"]=="builtin.ordinal"):
			ordinal_flag=1
			no_of_jumps=int(x["resolution"]["value"])
		else:
			if(x["type"]=="previous"):
				prev_or_next=1
			elif(x["type"] not in basic_comm):
				cnt+=1
	if(ordinal_flag==1):
		print("Pressing Ctrl+Home")		##To go to the start of the document
	if(prev_or_next==1):			##for previous heading	
		while(no_of_jumps>0):
			print("Pressing shift+g")
			no_of_jumps-=1
	else:
		while(no_of_jumps>0):
			print("Pressing g")
			no_of_jumps-=1
		
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

def list(entities):
	basic_comm={"last":1,"previous":1,"next":1,"list":1}
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
				print("Pressing shift+l")
				no_of_jumps-=1
		else:
			print("Pressing shift+l")	##if user just says go to last heading
			
	if(prev_or_next==1):			##for previous heading	
		while(no_of_jumps>0):
			print("Pressing shift+l")
			no_of_jumps-=1
	elif(lastflag==0):
		while(no_of_jumps>0):
			print("Pressing l")
			no_of_jumps-=1
			
def listitem(entities):
	basic_comm={"last":1,"previous":1,"next":1,"item":1}
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
			print("Pressing shift+i")
			no_of_jumps-=1
	else:
		while(no_of_jumps>0):
			print("Pressing i")
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
	
	

