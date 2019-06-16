# Directory Structure:

1. main.py- The main file where GlobalPlugin class is defined. It associates the “w” key, to start listening to user’s command.
parseCommands.py- The main.py calls this file, which is responsible for the overall understanding and execution of  user’s command.

2. parseCommands.py- It contains a dictionary of the intents recognized by LUIS and their corresponding function call. Once the intents are identified, the recognized entities are also  analyzed. Information like direction of the navigation (next or previous), a  number (like “Skip 3 lines”) and other useful data is extracted.

3. modules directory- contains the dependencies.

For a command like “Skip 3 lines”, the corresponding function loops thrice calling NVDA’s “next_line” function , but pauses speech inside the loop so that it doesn’t speak while traversing through those 3 lines. Outside the loop, it again calls the “next_line” function, this time without pausing NVDA Speech. It works similarly for other commands as well.


