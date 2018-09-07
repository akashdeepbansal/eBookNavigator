import json
import urllib.request

###Fetching the response
url_req='https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/90c836a8-52d8-4cd8-8b6d-d7e4060eaeb6?subscription-key=662e5a4e75654f6cadbf143294a5e0a8&verbose=false&timezoneOffset=0&q='
url_req+='Skip%20this%20line'
response = urllib.request.urlopen(url_req)
data = json.load(response)   
print(data)
filename="JSONResponse.txt"
with open(filename,'w') as json_file:
	json.dump(data,json_file)

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
		no_of_jumps-=1

def start_line(entities):
	basic_comm={"start":1,"line":1}
	cnt=0
	for x in entities:
		if(x["type"] not in basic_comm):
			cnt+=1
	if(cnt==0):		##no other entity
		print("Pressing Ctrl+Up")
		print("Pressing Ctrl+Down")
	
def end_line(entities):
	basic_comm={"end":1,"line":1}
	cnt=0
	for x in entities:
		if(x["type"] not in basic_comm):
			cnt+=1
	if(cnt==0):		##no other entity
		print("Pressing Ctrl+Up")
		print("Pressing Ctrl+Down")
		
def heading(entities):	
	basic_comm={"last":1,"previous":1,"next":1,"heading":1}
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
			print("Pressing shift+h")
			no_of_jumps-=1
	else:
		while(no_of_jumps>0):
			print("Pressing h")
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
			print("Pressing shift+t")
			no_of_jumps-=1
	else:
		while(no_of_jumps>0):
			print("Pressing t")
			no_of_jumps-=1

def list(entities):
	basic_comm={"last":1,"previous":1,"next":1,"list":1}
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
			print("Pressing shift+l")
			no_of_jumps-=1
	else:
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
"ListItem":listitem

}
with open('JSONResponse.txt') as f:
	data = json.load(f)
intent=data["topScoringIntent"]["intent"]
print("intent=",intent)
x=data["entities"]
key_commands[intent](x)
