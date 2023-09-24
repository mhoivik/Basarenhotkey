import pyautogui
import time
import keyboard

loop = True
print("\n\nBassar Hotkey kjører nå")
print("Ny Trekkning = s [start]")
print("Stopp program = e [end] eller kryss ut\n\n")
while True:
	if keyboard.is_pressed("s"):
		temp = pyautogui.locateOnScreen("hentet.png")
		if temp:
			res = pyautogui.center(temp)
			pyautogui.moveTo(res)
			pyautogui.click()
			time.sleep(0.1)
			pyautogui.click()
			print("Action performed successfully")
		else:
			print("Image not found")
	elif keyboard.is_pressed("e"):
		break