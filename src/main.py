import globalPluginHandler,tones	#Since this is a globinPlugin, we need to import globalPluginHandler,tones- to hear the beeps
from globalCommands import commands	#All the NVDA functions are defined in this file
from logHandler import log	#We need this to write to log file of NVDA
import os	#to call OS related functions
from parseCommands import *	#to call the start function defined in parseCommands file

#The main class where your plugin code needs to be written
class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	# The routine to do when the global plugin loads.
	def __init__(self,*args,**kwargs): 
		super(GlobalPlugin, self).__init__(*args,**kwargs) 
		log.debug("Hello world")
		

	#The function associated with the key "W"
	def script_doBeep(self, gesture):
		tones.beep(440, 1000) # Beep a tone for 1 second. 		
		start()			#defined in PythonParser.py file
		
		


	__gestures={
		"kb:W":"doBeep"			#Associates key "W" with the function doBeep
	}
	
