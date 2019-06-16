import globalPluginHandler,tones
from globalCommands import commands
from logHandler import log
import os
from parseCommands import *



class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	
	def __init__(self,*args,**kwargs): 
		super(GlobalPlugin, self).__init__(*args,**kwargs) 
		log.debug("Hello world")
		


	def script_doBeep(self, gesture):
		tones.beep(440, 1000) # Beep a standard middle A for 1 second.
		start()					#defined in PythonParser.py file
		
		


	__gestures={
		"kb:W":"doBeep"			#Associates key "W" with the function doBeep
	}
	#commands.script_review_nextLine(None)
	