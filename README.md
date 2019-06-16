# Introduction

This project enables users to navigate through an E-Book by voice commands instead of pressing keystrokes or gestures, using NVDA as a screen reader.

# Installation 

 The following dependencies needs to be installed before using the above module:

  - Python, version 2.7.15
  - NVDA screen reader : This can be downloaded from here https://www.nvaccess.org/download/
  - Python keyboard module- This can be installed using the command 
pip install keyboard
  - Python speech recognition module- This can be installed using the command 
pip install SpeechRecognition
  - Python PyAudio module- This can be installed using the command pip install pyaudio

  - Clone the github repository
  - Since this module is planned to work as an add-on, the files inside src folder need to be copied inside the globalPlugins folder (C:\Users\\[Your System Name]\AppData\Roaming\nvda\globalPlugins) of the NVDA directory.

# Design

The project has three main steps:

1. Convert user’s voice command to text
    - Uses Google speech recognition module which takes in the user’s voice and returns it’s corresponding text form. It has a very high accuracy rate with a microphone.
    - Also tried an offline Java library PocketSphinx but it’s accuracy turns out to be very low in comparison with the online methods.

2. Understand user’s intention behind the command.
    - Language Understanding Intelligent Service(LUIS), is an online machine learning based Microsoft service which can be used in applications to understand valuable information from the text.
    - LUIS is trained with dataset provided in the form of textual commands  for this specific purpose and the possible intents and entities are assigned.
    - The result of the speech recognizer is then sent to the LUIS end-point which recognizes it’s intents and various entities along with their confidence scores.
    - LUIS returns a JSON response.

3. Execute the intended action.
    - The JSON response returned by LUIS is then parsed by the python scripts whose functions are described in the next section.
    - The corresponding functions are identified and appropriate action is being executed by calling NVDA functions.


# Usage

- Turn on the NVDA.
- Currently have been tested on websites. So get the focus on a particular website, or press any NVDA command key to check if it's in focus .
- Press “w” key once and you will hear a beep sound for 1 second.
- Once the beep is over, give your voice command.
- At present, it takes around 6-7 secs to get a command executed, so wait for some time to see the effect.

## Current Possible Navigation 

The current design supports navigating across next/previous or skipping multiple times at one go, among the following items:
- Character		
- Word
- Line
- Heading
- List
- List Item
- Graphics

It also allows navigating to the following items:
- Start of the line
- End of the line
- Top of the page
- Bottom of the page

# Not Supported

Navigation support for following items is not functional in the current design:
- Paragraph
- Table
- Link

	Also doesn’t allow commands like:
  - Go to the third heading (or line or any of the items listed above.)
  - Read the next five lines (or any of the items listed above.)



