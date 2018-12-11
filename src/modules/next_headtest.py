import globalPluginHandler,tones
from globalCommands import commands
from logHandler import log
import os
from PythonParser import *

	#globalCommands.GlobalCommands.nextHeading()

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	
	def __init__(self,*args,**kwargs): 
		super(GlobalPlugin, self).__init__(*args,**kwargs) 
		log.debug("Hello world")
		#commands.script_review_nextLine(None)
		#commands.script_say_battery_status(None)
		log.debug("world")
		
	
	def script_doBeep(self, gesture):
		tones.beep(440, 1000) # Beep a standard middle A for 1 second.
		#commands.script_say_battery_status(None)
		#os.system('python PythonParser.python')
		start()
		
		

	
	__gestures={
		"kb:W":"doBeep"
	}
	#commands.script_review_nextLine(None)
	