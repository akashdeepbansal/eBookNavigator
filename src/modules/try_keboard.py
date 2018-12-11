import keyboard,time

''' TO switch the application I want to read '''
keyboard.press_and_release('alt+tab')
time.sleep(2)

'''To go to the next heading'''
keyboard.press_and_release('h')							##working on browser too

''' To go to the next list item'''
#keyboard.send('i')											##Working on browser too

''' To read battery status '''
#keyboard.press_and_release('caps lock+shift +b')			##Working

''' To go to the previous line	'''
#keyboard.press_and_release('up')							##Not working on browser


keyboard.press_and_release('right')							##Not working on browser

''' To go to the next paragraph'''
#keyboard.send('ctrl+down')									##The cursor moves to the next paragraph but doesn't speak out


