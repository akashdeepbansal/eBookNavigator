import globalPluginHandler,tones	#?? What all functions are dependent on this module
from globalCommands import commands	#?? What all functions are dependent on this module
from logHandler import log	#?? What all functions are dependent on this module
import os	#?? What all functions are dependent on this module
from parseCommands import *	#?? What all functions are dependent on this module


#?? What is overall objective of this class? What are inputs and what are outputs?
class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	#?? What is overall objective of this function? What are inputs and what are outputs?	
	def __init__(self,*args,**kwargs): 
		super(GlobalPlugin, self).__init__(*args,**kwargs) 
		log.debug("Hello world")
		

	#?? What is overall objective of this function? What are inputs and what are outputs?
	def script_doBeep(self, gesture):
		tones.beep(440, 1000) # Beep a standard middle A for 1 second. ?? What is standard middle A? What are the input parameters of the function: 440, 1000?		start()					#defined in PythonParser.py file
		
		


	__gestures={
		"kb:W":"doBeep"			#Associates key "W" with the function doBeep
	}
	#commands.script_review_nextLine(None) ??
	
